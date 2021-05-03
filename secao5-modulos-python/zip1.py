# ZIP - Compactando/Descompactando arquivos

from zipfile import ZipFile
import os

caminho = 'O CAMINHO DO ARQUIVO VEM AQUI!'
# usando o context manager da classe ZipFile para criar uma pasta zip e incluir arquivos dentro dela.
with ZipFile('arquivo.zip', 'w') as zip:
    # o `for` abaixo está listando apenas os arquivos dentro da pasta com o caminho informado na variável acima.
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        # incluindo os arquivos do caminho completo para dentro do arquivo .zip
        zip.write(caminho_completo, arquivo)

# Leitura dos dados dentro da pasta zip.
with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Extraindo os arquivos da pasta zip.
with ZipFile('arquivo.zip', 'r') as zip:
    # a pasta `descompactado` foi criada automaticamente.
    zip.extractall('descompactado')