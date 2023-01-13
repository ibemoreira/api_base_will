from fastapi import APIRouter, File, UploadFile
from PIL import Image
import numpy as np

router = APIRouter()

#Envia ft devolve RGB predominante. 
@router.post("/cor-predominante")
async def cor_predominante(file: UploadFile):
    # Abre a imagem
    im = Image.open(file.file)

    # Converte para o espaço de cores RGB
    rgb_im = im.convert('RGB')

    # Obtém os dados da imagem
    rgb_data = np.array(rgb_im)

    # Cria um histograma com as cores da imagem
    histogram = np.histogramdd(rgb_data.reshape(-1, 3), bins=(8, 8, 8), range=((0, 255), (0, 255), (0, 255)))[0]

    # Encontra o índice da cor com maior frequência no histograma
    most_common_color = np.unravel_index(np.argmax(histogram, axis=None), histogram.shape)

    # Obtém a cor predominante
    mode_rgb = (most_common_color[0]*32, most_common_color[1]*32, most_common_color[2]*32)


    return {
        "cor_predominante": str(mode_rgb)
        }
