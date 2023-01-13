from pydantic import BaseModel



class PdfSchemaBase(BaseModel):
    url: str

class PdfSchemaRes(PdfSchemaBase):
    producer: str
    creationDate: str
    modDate: str
    title: str
    producer: str
    creator:str
    author: str