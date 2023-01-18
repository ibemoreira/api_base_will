from PIL import Image
import numpy as np


def alterar_cor(corDesejada, corSubstituida, tolerance):
    im = Image.open('teste_verde.jpeg').convert('RGB')
    data = np.array(im)
    vermelho, verde, azul = data.T
    condition = (vermelho >= corSubstituida[0]-tolerance) & (vermelho <= corSubstituida[0]+tolerance) & (verde >= corSubstituida[1]-tolerance) & (verde <= corSubstituida[1]+tolerance) & (azul >= corSubstituida[2]-tolerance) & (azul <= corSubstituida[2]+tolerance)
    data[condition.T] = corDesejada
    im2 = Image.fromarray(data)
    im2.save("nome_da_imagem_modificada.jpg", "JPEG")