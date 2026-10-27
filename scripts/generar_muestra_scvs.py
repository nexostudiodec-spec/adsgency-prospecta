#!/usr/bin/env python3
"""Genera una muestra reproducible de empresas ecuatorianas desde el CSV público de la SCVS.
No afirma que una empresa necesite marketing; crea candidatos para investigación manual.
"""
import csv
import hashlib
import io
import os
import sys
import subprocess
import tempfile
import urllib.request
from datetime import datetime, timezone

SOURCE = "https://appscvsmovil.supercias.gob.ec/ranking/recursos/bi_compania.csv"
LIMIT = int(os.environ.get("PROSPECTA_LIMIT", "50"))
OUTPUT = os.environ.get("PROSPECTA_OUTPUT", "prospectos_piloto.csv")
USER_AGENT = "AdsgencyProspectaPilot/1.0 (manual public-data sampling)"

def fetch(url):
    # La web de la SCVS puede rechazar la negociación TLS de urllib en runners
    # de GitHub. Primero intentamos curl con HTTP/1.1 y TLS 1.2; después,
    # como alternativa, usamos la biblioteca estándar de Python.
    with tempfile.NamedTemporaryFile(prefix="scvs-", suffix=".csv", delete=False) as tmp:
        path = tmp.name
    try:
        result = subprocess.run(
            [
                "curl", "--location", "--fail", "--silent", "--show-error",
                "--http1.1", "--tlsv1.2", "--retry", "3",
                "--retry-all-errors", "--connect-timeout", "20",
                "--max-time", "240", "--user-agent", USER_AGENT,
                "--output", path, url,
            ],
            capture_output=True, text=True, timeout=260,
        )
        if result.returncode == 0 and os.path.getsize(path) > 0:
            with open(path, "r", encoding="utf-8-sig", errors="replace", newline="") as f:
                return f.read()
        print(f"curl no pudo descargar la fuente ({result.stderr.strip() or result.returncode}); probando urllib.", flush=True)
    finally:
        try:
            os.unlink(path)
        except OSError:
            pass
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=90) as response:
        return response.read().decode("utf-8-sig", errors="replace")

def parse_rows(text):
    sample = text[:10000]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
    except csv.Error:
        dialect = csv.excel
    reader = csv.DictReader(io.StringIO(text), dialect=dialect)
    if not reader.fieldnames:
        raise RuntimeError("El archivo de la SCVS no contiene encabezados reconocibles.")
    rows = []
    for raw in reader:
        row = {str(k or "").strip().lower(): str(v or "").strip() for k, v in raw.items()}
        name = next((row[k] for k in ("nombre", "razon_social", "razón_social", "razon social", "nombre_compania") if row.get(k)), "")
        if not name:
            continue
        province = next((row[k] for k in ("provincia", "province") if row.get(k)), "")
        ruc = next((row[k] for k in ("ruc", "numero_ruc") if row.get(k)), "")
        expediente = next((row[k] for k in ("expediente", "numero_expediente") if row.get(k)), "")
        kind = next((row[k] for k in ("tipo", "tipo_compania", "tipo de compañía") if row.get(k)), "")
        rows.append({"empresa": name, "provincia": province, "ruc": ruc, "expediente": expediente, "tipo_compania": kind})
    return rows

def main():
    print(f"Descargando directorio público de la SCVS: {SOURCE}", flush=True)
    text = fetch(SOURCE)
    rows = parse_rows(text)
    if not rows:
        raise RuntimeError("No se encontraron registros. Puede haber cambiado el formato de la fuente.")
    # Deduplicar por RUC; si falta, usar expediente + nombre.
    unique = {}
    for row in rows:
        key = row["ruc"] or row["expediente"] or row["empresa"].casefold()
        unique.setdefault(key, row)
    rows = list(unique.values())
    # Muestra reproducible, distribuida por provincia cuando el campo está disponible.
    def rank(row):
        key = "|".join((row["ruc"], row["expediente"], row["empresa"]))
        return hashlib.sha256(key.encode("utf-8")).hexdigest()
    by_province = {}
    for row in rows:
        by_province.setdefault(row["provincia"] or "Provincia no informada", []).append(row)
    for group in by_province.values():
        group.sort(key=rank)
    provinces = sorted(by_province)
    selected = []
    while len(selected) < min(LIMIT, len(rows)):
        added = False
        for province in provinces:
            if by_province[province] and len(selected) < min(LIMIT, len(rows)):
                selected.append(by_province[province].pop(0))
                added = True
        if not added:
            break
    today = datetime.now(timezone.utc).date().isoformat()
    fields = ["empresa", "provincia", "ruc", "expediente", "tipo_compania", "servicio_potencial", "senal_observada", "nivel_de_confianza", "estado_revision", "fuente_url", "fecha_consulta"]
    with open(OUTPUT, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in selected:
            writer.writerow({
                **row,
                "servicio_potencial": "Por determinar",
                "senal_observada": "Candidato de registro público; presencia web y redes aún no investigadas.",
                "nivel_de_confianza": "Bajo",
                "estado_revision": "Pendiente de investigación manual",
                "fuente_url": SOURCE,
                "fecha_consulta": today,
            })
    print(f"Registros disponibles: {len(rows)}; candidatos exportados: {len(selected)}; archivo: {OUTPUT}", flush=True)
    if not selected:
        sys.exit("La muestra quedó vacía.")

if __name__ == "__main__":
    main()
