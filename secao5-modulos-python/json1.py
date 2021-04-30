"""
JavaScript Object Notation - JSON
JSON é um formato de troca de dados entre sistemas e programas que se destaca por ser muito leve e de fácil utilização. É muito utilizado é APIs.

DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
False	        false
None	        null

LOADS / Load
######################
JSON	        Python

object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None
"""

"""
https://exchangeratesapi.io/
https://api.exchangeratesapi.io/latest
"""

# Exemplos abaixo


import json
clientes_dicionario = {
    1: {
        'nome': 'Renato Pereira',
        'sobrenome': 'Santos',
        'idade': 25,
        'altura': 1.80,
        'peso': 80.53,
    },
    2: {
        'nome': 'Maria',
        'sobrenome': 'Oliveira',
        'idade': 52,
        'altura': 1.67,
        'peso': 57,
    },
    3: {
        'nome': 'Pedro',
        'sobrenome': 'Faria',
        'idade': 32,
        'altura': 1.95,
        'peso': 113,
    },
}

clientes_json = """
{
    "1": {
        "nome": "Renato Pereira",
        "sobrenome": "Santos",
        "idade": 25,
        "altura": 1.8,
        "peso": 80.53
    },
    "2": {
        "nome": "Maria",
        "sobrenome": "Oliveira",
        "idade": 52,
        "altura": 1.67,
        "peso": 57
    },
    "3": {
        "nome": "Pedro",
        "sobrenome": "Faria",
        "idade": 32,
        "altura": 1.95,
        "peso": 113
    }
}
"""

# Converte um dicionário em JSON
# útil para salvar informações de qualquer tipo
dados = json.dumps(clientes_dicionario, indent=4)

# Converte JSON em um dicionário
# útil para carregar informações de qualquer tipo
dados = json.loads(clientes_json)
print(dados)

# Exporta dicionário para arquivo JSON
with open('clientes.json', 'w') as file:
    json.dump(clientes_dicionario, file, indent=4)

# Importa string de um arquivo JSON e converte em dicionário
with open('clientes.json', 'r') as file:
    data = json.load(file)

print(data)
