import agents.writer_agent
from services.docx_export import docx_export
from services.gemini_client import GeminiClient
from services.excel_io import ExcelIO
from agents.seo_agent import SEOAgent
from pathlib import Path
from config import GEMINI_MODEL, API_KEY, EXCEL_PATH


def main():
    print("========== GENERADOR SEO BLOG ==========")

    gemini_client = GeminiClient(
        api_key=API_KEY,
        model=GEMINI_MODEL
    )

    #INCICIALIZAR AGENTES
    writer_agent = agents.writer_agent.WriterAgent(gemini_client)
    seo_agent = SEOAgent(gemini_client)

    #pedir excel
    excel_name = input("Nombre del archivo Excel (con .xlsx):")
    excel_file_path = Path(EXCEL_PATH) / excel_name
    excelio = ExcelIO(str(excel_file_path))

    #Lectura keywords
    keywords = excelio.keyword_reader()

    print("\n Keywords detectadas:\n")
    for kw in keywords:
        print("-", kw)

    #generar estructura SEO
    estructura = seo_agent.generate_structure(keywords)

    print("\n === ESTRUCTURA PROPUESTA ===")
    print("H1: ", estructura["h1"])
    print("\nH2:")
    for h2 in estructura["h2"]:
        print("-",h2)

    confirmacion_estructura = input("\n Confirmas la estructura generada? s/n")

    if confirmacion_estructura.lower() != "s":
        print("Proceso cancelado.")
        return

    #Escritura de estructura en excel
    excelio.structure_writer(estructura)
    print("\n Estructura escrita en excel.")

    #Numero de palabras, def 500
    numero_palabras = input("\n Introduce un numero aproximado de palabras para el post: ")

    #Generacion del post
    post = writer_agent.generate_post(
        h1=estructura["h1"],
        h2_list=estructura["h2"],
        keywords=keywords,
        numero_palabras=numero_palabras
    )

    print("\n POST Generado:\n")
    print(post)

    #Carpeta de destino del docx fija
    docx_folder = Path("files/docx")
    docx_folder.mkdir(parents=True, exist_ok=True)

    nombre_documento = input("Nombre del Post: ")

    ruta_docx = docx_folder / f"{nombre_documento}.docx"

    docx_export(post, ruta_docx)
    print("\n Documento Word generado con éxito en: ",ruta_docx.resolve())


if __name__ == "__main__":
    main()