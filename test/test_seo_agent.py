from config import API_KEY
from services.excel_io import ExcelIO
from services.gemini_client import GeminiClient
from agents.seo_agent import SEOAgent



def main():
    ruta = "../files/indexKeywords.xlsx"
    excel = ExcelIO(ruta)

    print("Leyendo keywords\n")
    keywords = excel.keyword_reader()
    print("KW Encontradas:\n")
    print(keywords)

    print("\nProbando escritura:-:")
    test_estructura = {
        "h1":"Catálogo exclusivo de zapatillas deportivas mujer al por mayor.",
        "h2":[
            "Subtitulo 1",
            "Subtitulo 2",
            "Subtitulo 3",
            "Subtitulo 4",
            "Subtitulo 5",
    ]
    }
    print("\n",test_estructura,"\n")
    excel.structure_writer(test_estructura)
    print("Escritura correcta.")


if __name__ == "__main__":
    main()