# Plan técnico — Adsgency Prospecta

## Objetivo

Crear un sistema independiente para descubrir y clasificar empresas potenciales para Adsgency Digital en Ecuador. El primer piloto debe producir un CSV de 30–50 empresas para revisión humana.

## Restricciones del piloto

- No modificar el repositorio original de Harvey.
- No modificar ni conectar el CRM de Adsgency ni Supabase.
- No enviar correos, WhatsApp ni mensajes.
- No ejecutar el ciclo autónomo completo de Harvey.
- No desplegar una interfaz pública sin autorización explícita.
- No guardar claves API, credenciales ni tokens en el código.
- Evitar servicios de pago hasta conocer la cobertura y estimar el coste.

## Hallazgos de compatibilidad

El repositorio original de Harvey requiere Python 3.11 o superior y sus llamadas al modelo dependen de un proveedor autenticado mediante Claude Code o Codex. Por ello, un workflow estándar de GitHub Actions no debe considerarse una ejecución gratuita y lista para usar sin diseñar primero la autenticación, el almacenamiento persistente y los límites de ejecución.

Harvey incluye funcionalidades de descubrimiento, análisis de sitios web, detección de tecnología, verificación de correos y exportación. La primera prueba debe reutilizar solo los componentes necesarios y mantener desactivados el escritor de campañas y el envío.

## Secuencia propuesta

1. Evaluar fuentes de descubrimiento gratuitas y sus límites de uso.
2. Diseñar un comando de ejecución manual con límites estrictos de resultados y tiempo.
3. Guardar resultados como artefacto CSV descargable, sin almacenar datos sensibles innecesarios.
4. Incluir fuente y fecha de consulta, ubicación, web, datos empresariales públicos disponibles, oportunidad potencial y estado de verificación.
5. Ejecutar primero una prueba pequeña y revisar calidad, duplicados y costes.
6. Solo después decidir si se implementa la extensión de Chrome y dónde alojar un motor persistente.

## Estado actual

Este documento es un plan de implementación. No se ha instalado Harvey, no se han ejecutado búsquedas, no se ha creado ningún workflow de ejecución y no se ha desplegado ningún servicio.
