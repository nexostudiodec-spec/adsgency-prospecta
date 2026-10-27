# Adsgency Prospecta

Herramienta independiente para investigar y clasificar empresas potenciales para Adsgency Digital en Ecuador.

## Objetivo del piloto

- Descubrir entre 30 y 50 empresas para una primera evaluación.
- Cubrir Ecuador y los servicios de páginas web, marketing digital, gestión de redes sociales y publicidad digital.
- Registrar fuentes, fecha de consulta, sitio web, redes sociales, datos empresariales disponibles y oportunidades potenciales.
- Exportar resultados a CSV para revisión humana.

## Límites de seguridad

- No enviar correos, mensajes de WhatsApp ni campañas automáticamente.
- No conectar con el CRM ni con Supabase.
- No guardar secretos, claves API ni credenciales en el repositorio.
- No desplegar servicios públicos sin revisión y autorización explícita.
- Medir costes y límites de las fuentes antes de ejecutar búsquedas amplias.

## Estado

Repositorio inicial. La arquitectura, las fuentes de datos y el método de ejecución deben revisarse antes de implementar o ejecutar el motor de prospección.


## Interfaz web y GitHub Pages

La interfaz está en `site/index.html`. El flujo `.github/workflows/pages.yml` permite desplegarla manualmente; no se ejecuta en cada commit. El artefacto de Pages contiene solo el directorio `site/`, no los documentos internos.

### Activación pendiente en GitHub

1. Abre Settings → Pages.
2. En Build and deployment, selecciona `GitHub Actions` como Source.
3. Comprueba la opción de visibilidad de Pages disponible para tu plan antes de publicar. Si el sitio será público, no incluir datos reales de prospectos, secretos ni información interna.
4. Abre Actions → Publish Adsgency Prospecta to GitHub Pages → Run workflow.
5. Revisa el resultado del workflow y la URL que GitHub entrega.

Este workflow solo publica la interfaz estática. No ejecuta Harvey, no busca empresas y no conecta con el CRM ni Supabase.
