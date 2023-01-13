
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from core.configs import settings



class PdfModel():
    __tablename__ = 'A1_PDF'

    producer = Column(String(256))
    creationDate = Column(String(256))
    modDate = Column(Integer)
    title = Column(String(256))
    creator = Column(String(256))
    author = Column(String(256))
