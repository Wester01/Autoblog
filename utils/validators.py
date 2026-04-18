from typing import Any, Dict, List
from config import H2_COUNT
from utils.types import EstructuraSEO


# validación 
def _validate(data: Dict[str, Any]) -> bool:
    print("Debug:: data in _validate: ", data)
    if not isinstance(data, dict):
        return False

    #Validación H1
    h1 = data.get("h1")
    if not isinstance(h1, str) or not h1.strip():
        #raise ValueError("Faltan claves 'h1' o 'h2' en la respuesta")
        return False

    #Validación H2
    h2 = data.get("h2")
    if not isinstance(h2, list):
        #raise ValueError("El h1 no es válido")
        return False

    if len(h2) != H2_COUNT:
        #raise ValueError("Debe haber exactamente 5 titulos H2")
        return False


    for titulo in h2:
        if not isinstance(titulo, str) or not titulo.strip():
            return False

    return True

def confirm_structure(data: Dict[str, Any]) -> EstructuraSEO:
    """
    Lanza except si la estructura es inválida
    Devuelve el tipado Estructura SEO si es valida
    """
    #print("DEBUG::raw-data-confirm_structure:: ",data)
    if not _validate(data):
        raise ValueError("Estructura SEO invalida.")

    return data

def validar_estructura_post(data: dict):
    if not isinstance(data, dict):
        raise ValueError("El post no es un diccionario.")

    if "h1" not in data or not isinstance(data["h1"], str):
        raise ValueError("El post no contiene H1 válido.")

    if "secciones" not in data or not isinstance(data["secciones"], list):
        raise ValueError("El post no contiene secciones válidas")

    if len(data["secciones"]) != 5:
        raise ValueError("El post debe contener 5 secciones H2.")

    for seccion in data["secciones"]:
        if "h2" not in seccion or not isinstance(seccion["h2"], str):
            raise ValueError("Una sección contiene un H2 no válido.")

        if "contenido" not in seccion or not isinstance(seccion["contenido"], str):
            raise ValueError("Una sección no tiene contenido válido.")
