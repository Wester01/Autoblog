from config import WORD_COUNT
from services.gemini_client import GeminiClient
from utils.validators import validar_estructura_post

class WriterAgent:
    def __init__(self, gemini_client: GeminiClient):
        self.gemini_client = gemini_client

    def generate_post(
            self,
            h1: str,
            h2_list: list[str],
            keywords: list[str],
            numero_palabras = WORD_COUNT
    ) -> dict:

        prompt = self._build_prompt(h1, h2_list, keywords, numero_palabras)

        data = self.gemini_client.generate_json(prompt)

        validar_estructura_post(data)

        return data

    def _build_prompt(
            self,
            h1: str,
            h2_list: list[str],
            keywords: list[str],
            numero_palabras: int = WORD_COUNT
    ) -> str:
        return f"""
Eres un redactor SEO profesional.
        
Genera un post de blog en CASTELLANO  con la siguiente estructura:

H1:
{h1}

H2:
{chr(10).join(h2_list)}  

Requisitos estrictos:

- El texto debe tener aproximadamente {numero_palabras} palabras.
- Mantener coherencia y fluidez.
- Evitar redundancias y repeticiones innecesarias.
- Usar las siguientes palabras clave de forma natural:
{", ".join(keywords)}
- Cada palabra clave debe aparecer en ngrita usando formato markdown. EJ: **palabra clave**
- No inventar datos técnicos específicos si no se conocen.
- No incluir introducciones, instrucciones, saludos o despedidas de la IA ni cosas tipo "Aqui tienes el artículo".
- No añadir comentarios fuera de la estructura solicitada ni dentro.

Devuelve EXCLUSIVAMENTE un JSON válido con la siguiente estructura:

{{
    "h1":"string",
    "secciones": [
        {{
            "h2": "string",
            "contenido":"string"
        }}
    ]
}}
"""