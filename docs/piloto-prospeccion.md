# Piloto de prospección — primera extracción

## Qué hace
El workflow manual `Generar muestra piloto de prospectos Ecuador` descarga el CSV público de compañías de la Superintendencia de Compañías, Valores y Seguros (SCVS), deduplica registros y selecciona una muestra reproducible distribuida entre las provincias que aparecen en la fuente. Entrega un CSV como artefacto descargable por 7 días.

Fuente: https://appscvsmovil.supercias.gob.ec/ranking/reporte.html
Descarga CSV: https://appscvsmovil.supercias.gob.ec/ranking/recursos/bi_compania.csv

## Límites importantes
- Este paso crea una lista de candidatos; **no confirma** que estén activos ni que necesiten servicios digitales.
- La web y las redes sociales aún no se investigan en esta primera extracción.
- El servicio potencial queda como "Por determinar" y cada fila requiere investigación manual.
- No envía mensajes, no llama APIs de pago y no se conecta al CRM ni a Supabase.
- El workflow es manual y solo publica un artefacto privado de ejecución, no publica los prospectos en GitHub Pages.
- La fuente y sus términos deben revisarse antes de escalar o reutilizar masivamente los datos.

## Ejecución
1. Abre Actions.
2. Selecciona "Generar muestra piloto de prospectos Ecuador".
3. Pulsa Run workflow y elige 30, 40 o 50.
4. Cuando termine, descarga el artefacto `adsgency-prospecta-piloto`.
5. Importa el CSV en la interfaz de Adsgency Prospecta para ver la muestra.

El orden de muestra es reproducible con los mismos datos de origen, pero puede cambiar cuando la SCVS actualice su directorio.
