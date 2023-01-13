import requests
import PyPDF2
import io

def extrair_metadados_pdf(url: str) -> dict:
  # Usar o requests para baixar o arquivo PDF a partir da URL
  response = requests.get(url)

  temp_file = io.BytesIO(response.content)

  # Criar um objeto PDF a partir do conteúdo da resposta
  pdf = PyPDF2.PdfReader(temp_file)

  # Obter os metadados do PDF
  metadata = pdf.metadata
  # Retornar os metadados como um dicionário
  return metadata
