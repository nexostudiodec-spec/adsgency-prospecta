# Evaluación de fuentes y costes

Fecha de revisión: 2026-10-27

## Resumen ejecutivo

GitHub Actions puede ejecutar trabajos manuales y guardar un CSV como artefacto, pero el repositorio privado consume la cuota de minutos incluida en el plan y puede generar cargos al excederla. Antes de activar workflows, revisar la cuota de la cuenta.

No asumir que una fuente pública es gratuita para uso comercial ni que cubre todo Ecuador. La primera versión debe mantener un presupuesto cero y detenerse si una fuente requiere tarjeta, clave de pago o suscripción.

## Fuentes evaluadas

### OpenStreetMap / Overpass API pública

- Ventaja: acceso sin clave y datos de negocios etiquetados en el mapa.
- Limitaciones: cobertura desigual de empresas, teléfonos, correos y páginas web; no es una base exhaustiva de empresas.
- Política: la documentación de Overpass advierte que sus servidores públicos son recursos compartidos y recomienda servidores propios o de pago para uso comercial. No usar el endpoint público como fuente automática recurrente de prospección comercial.
- Decisión: no usar el endpoint público de Overpass como motor comercial recurrente.

Referencia: https://wiki.openstreetmap.org/wiki/Overpass_API

### Google Places API

- Ventaja: búsqueda de establecimientos y datos estructurados.
- Limitaciones: requiere un proyecto, clave y facturación habilitada; el coste depende del SKU y de los campos solicitados. No asumir crédito gratuito.
- Decisión: no conectar ni activar sin revisar la facturación y aprobar un presupuesto.

Referencias:
- https://developers.google.com/maps/documentation/places/web-service/usage-and-billing
- https://developers.google.com/maps/billing-and-pricing/pricing

### GitHub Actions

- Ventaja: ejecución manual en la nube y posibilidad de entregar el CSV como artefacto descargable.
- Limitaciones: los repositorios privados consumen minutos y almacenamiento de la cuota de la cuenta; el uso por encima de la cuota puede facturarse.
- Decisión: apto para procesar lotes pequeños si se confirma la cuota y se configura un disparador manual; no tratarlo como servidor persistente ni como motor que corre continuamente.

Referencias:
- https://docs.github.com/en/actions/concepts/billing-and-usage
- https://docs.github.com/en/billing/concepts/product-billing/github-actions

### Fuentes públicas oficiales y directorios abiertos

- Ventaja: pueden aportar nombres, actividad y ubicación sin comprar una base de contactos.
- Limitaciones: suelen carecer de sitios web, correos de contacto y señales comerciales recientes; cada portal tiene condiciones propias.
- Decisión: evaluar fuente por fuente y conservar URL y fecha de consulta. No automatizar formularios ni eludir medidas de acceso.

## Arquitectura recomendada para el piloto de coste cero

1. No usar el motor autónomo completo de Harvey; no iniciar el ciclo autónomo.
2. Recibir una lista inicial de resultados de fuentes públicas verificadas.
3. Normalizar y deduplicar nombres, dominios, ciudad y URL de origen.
4. Visitar solo sitios públicos de forma limitada para detectar presencia web y señales técnicas sencillas.
5. Clasificar oportunidades con reglas transparentes, sin afirmar que una empresa necesita un servicio si no hay evidencia.
6. Exportar CSV y revisar manualmente antes de cualquier contacto.

## Campos mínimos del CSV

- empresa
- ciudad
- provincia
- actividad
- sitio_web
- redes_sociales
- teléfono_empresarial_publicado
- correo_empresarial_publicado
- servicio_potencial
- señal_observada
- fuente_url
- fecha_consulta
- nivel_de_confianza
- notas

No recolectar datos personales sensibles. Un correo o teléfono no debe etiquetarse como verificado sin una comprobación real.

## Criterio para pasar a automatización

No crear una ejecución automática recurrente hasta que:
- exista una fuente de datos con términos compatibles con uso comercial;
- se conozcan sus límites y coste;
- se haya comprobado la cuota de GitHub Actions;
- el piloto de 30–50 empresas muestre cobertura y calidad suficientes;
- el workflow sea manual, acotado y no tenga secretos innecesarios;
- se mantengan desactivados todos los envíos de correo y WhatsApp.

## Estado

Evaluación documental completada. No se han ejecutado búsquedas de empresas ni workflows; no se han conectado APIs ni activado servicios de pago.
