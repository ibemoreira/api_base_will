from fastapi import FastAPI

from core.configs import settings
from api.V1.api import api_router

app = FastAPI(title='Tinto Max')
app.include_router(api_router, prefix=settings.API_V1_SRT)

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
    log_level='info', reload=True)


'''
token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjYzMjg2MTgyLCJpYXQiOjE2NjI2ODEzODIsInN1YiI6IjMifQ.C4r95GuDI0m5TEkxjAGInjvxWp6IcPQZs3QaC4cmy3c
Type: bearer
'''