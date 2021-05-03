import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/tagged/python?tab=Newest'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')
    votos = pergunta.select_one('.vote-count-post ')
    tempo_relativo = pergunta.select_one('.relativetime')

    print(f'Título: {titulo.text}')
    print(f'Votos: {votos.text}')
    print(f'Tempo relativo: {tempo_relativo.text}\n')
    
# Acima temos um algoritmo de webscraping para extrair as informações de titulo das perguntas, quantidade de votos de cada pergunta e tempo relativo de postagem diretamente do site 'stackoverflow.com'.