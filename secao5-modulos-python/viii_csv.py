"""
CSV -> Comma Separated Values (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de dados, clientes de ee-mail, etc...
"""
import csv

with open('clientes.csv', 'r') as file:
    dados = csv.reader(file)
    # caso não queira que a primeira linha do arquivo seja exibida, pode utilizar o método `next` no objeto dados (já que ele é um iterador).
    # Exemplo:
    next(dados)
    for dado in dados:
        print(dado)

# -----------------------------------------------------------------------

# Utilizando o módulo `csv` para retornar os dados no formato de `dictionary`

with open('clientes.csv', 'r') as file:
    dados = csv.DictReader(file)

    for dado in dados:
        print(dado['Nome'], dado['Sobrenome'],
              dado['E-mail'], dado['Telefone'])

# Utilizando list comprehension para jogar os dados do arquivo dentro de uma variável e conseguir acessar as informações fora do escopo do `with`.

with open('clientes.csv', 'r') as file:
    dados = [x for x in csv.DictReader(file)]


# Criando um novo arquivo com os mesmos dados de `clientes.csv` a partir da variável dados (criada com list comprehension).

with open('clientes2.csv', 'w+') as arquivo:
    # configurações de escrita do arquivo csv
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    # processo de escrita de linhas no arquivo (`writerow`)

    # da linha 23 até 32, estamos adicionando as colunas da tabela
    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    # a partir daqui estão sendo adicionados os registros
    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
