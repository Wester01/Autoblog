import json
import time
from json import JSONDecodeError
from typing import Any, Dict, Optional

from google import genai

from config import GEMINI_MODEL


class GeminiClient:
    def __init__(
            self,
            api_key: str,
            model: str = GEMINI_MODEL,
            temperature: float = 0.3,
            max_retries: int = 3,
            retry_delay: float = 2.0
    ):
        self.client = genai.Client(api_key=api_key)

        self.model_name = model
        self.temperature = temperature
        self.max_retries = max_retries
        self.retry_delay = retry_delay


        #self.model = genai.GenerativeModel(
        #    model_name=self.model_name,
        #    generation_config={"temperature":self.temperature}
        #)


    #Llamada que exige JSON valido
    def generate_json(self, prompt: str) -> Dict[str, Any]:
        try:
            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config={
                    "response_mime_type":"application/json",
                    "temperature":0.3
                }
            )

            if not response.text:
                raise ValueError("Gemini no ha devuelto contenido")

            texto = response.text.strip()

            try:
                return json.loads(texto)
            except JSONDecodeError:

                if "```" in texto:
                    texto_limpio = texto.replace("```json", "").replace("```","").strip()
                    return json.loads(texto_limpio)

            raise ValueError("La respuesta de Gemini no tiene formato válido.")


        except Exception as e:
            raise RuntimeError(f"Error llamando a Gemini: {e}")

