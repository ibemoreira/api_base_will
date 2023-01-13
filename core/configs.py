from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """

    API_V1_SRT: str = '/api/v1'
    DB_URL: str = "__mysql+aiomysql://admin:fpcontrol@fpcontrol.c8n91v7dxgjo.us-east-1.rds.amazonaws.com:3306/FPCONTROL_TESTE"
    DB_URL_SYNC: str = "__mysql+mysqlconnector://admin:fpcontrol@fpcontrol.c8n91v7dxgjo.us-east-1.rds.amazonaws.com:3306/FPCONTROL_TESTE"
    DBBaseModel = declarative_base()

    JWT_SECRET: str = 'EGv5VMnXKHbYQiEHibN7qybzzxVY23dDbqm1jm_EPxM'
    
    #Para criar o token usei os seguintes comendos
    #import secrets 
    #token: str = secrets.token_urlsafe(32)
    
    ALGORITHM: str =  'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    #60 minutos * 24 horas * 7 dias => 1 semana
    class Config:
        case_sensitive = True

settings: Settings = Settings()
