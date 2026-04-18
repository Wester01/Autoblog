# AI AutoBlog Generator 🚀
### Automatización de Contenidos mediante Agentes de IA (Gemini) y Python

Este proyecto optimiza la creación de artículos para blogs mediante un flujo de trabajo automatizado que utiliza múltiples agentes de Inteligencia Artificial para garantizar la calidad y el SEO del contenido.

## 🛠️ Tecnologías utilizadas
* **Lenguaje:** Python 3.14.3
* **IA:** Google Gemini API (Modelo Flash)
* **Arquitectura:** Orquestación de agentes independientes.

## 🤖 ¿Cómo funciona?
El sistema utiliza una estructura de agentes especializados:
1. **Agente Redactor:** Genera el cuerpo del artículo basándose en keywords.
2. **Agente SEO/Editor:** Revisa el contenido, optimiza los encabezados y asegura que cumple con las directrices de posicionamiento.

## 📂 Estructura del Proyecto
* `/agents`: Lógica individual de cada agente de IA.
* `/services`: Conexiones con servicios externos (API de Gemini).
* `/utils`: Funciones auxiliares y de soporte.

## 🚀 Instalación y Uso
1. Clonar el repositorio.
2. Configurar las variables de entorno en un archivo `.env` (requiere `GEMINI_API_KEY`).
3. Ejecutar `python main.py`.
