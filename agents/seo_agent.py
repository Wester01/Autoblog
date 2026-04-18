from typing import Dict, List
from services.gemini_client import GeminiClient
from utils.types import EstructuraSEO
from utils.validators import confirm_structure


class SEOAgent:
    def __init__(self, gemini_client: GeminiClient):
        self.client = gemini_client

    #Prompt base
    def _build_prompt(self, keywords: List[str]) ->str:
        keywords_text = ", ".join(keywords)
        return f"""
Eres un experto en SEO y redacción de blogs en castellano.

OBJETIVO:
Generar una estructura de artículo con un unico H1 y 5 H2 optimizada para SEO.

PALABRAS CLAVE:
{keywords_text}

REQUISITOS ESTRICTOS:
- Escribe SIEMPRE en castellano natural.
- Evita redundancias, repeticiones y frases vacías.
- El H1 debe ser atractivo y contener la temática principal.
- Los 5 H2 deben cubrir el tema de forma lógica y ordenada.
- Usa las palabras clave de forma natural en los títulos.
- No inventes titulación innecesaria.
- NO uses ":" en los títulos.
- Capitaliza SOLO la PRIMERA letra de cada frase.

FORMATO DE RESPUESTA:
Devuelve SOLO un JSON válido con esta estructura exacta:

{{
    "h1":"Título principal",
    "h2":["Subtítulo","Subtítulo","Subtítulo","Subtítulo","Subtítulo"]
}}    
"""


    #metodo publico
    def generate_structure(self, keywords: List[str]) -> EstructuraSEO:
        prompt = self._build_prompt(keywords)
        data = self.client.generate_json(prompt)
        #print("DEBUG generate_structure: ", prompt)
        return confirm_structure(data)