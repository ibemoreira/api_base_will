
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from core.get_metadados import extrair_metadados_pdf
from schemas.pdf_schama import PdfSchemaBase, PdfSchemaRes

router = APIRouter()

#Post Posto
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PdfSchemaRes)
async def post_pdf(pdf: PdfSchemaBase):
    
    pdf_metadados = extrair_metadados_pdf(pdf.url)

    try:
        n_producer = str(pdf_metadados.producer)
    except:
        n_producer = '###'

    try:
        n_creationDate = str(pdf_metadados.creation_date)
    except:
        n_creationDate = '###'

    try:
        n_modDate = str(pdf_metadados.modification_date)
    except:
        n_modDate = '###'

    try:
        n_title = str(pdf_metadados.title)
    except:
        n_title = '###'

    try:
        n_creator = str(pdf_metadados.creator)
    except:
        n_creator = '###'
        
    try:
        n_author = str(pdf_metadados.author)
    except:
        n_author = '###'


    novo_pdf = PdfSchemaRes(producer = n_producer,
                                creationDate = n_creationDate,
                                modDate = n_modDate,
                                title = n_title,
                                creator = n_creator,
                                author = n_author,
                                url = pdf.url)
    print(novo_pdf)
    return novo_pdf
