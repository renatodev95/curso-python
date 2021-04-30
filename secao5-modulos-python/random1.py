import random
import string

# Gera um número inteiro entre A e B
inteiro = random.randint(10, 20)

# Gera um número inteiro aleatório usando a função range(start, stop, step)
inteiro2 = random.randrange(900, 1000, 10)

# Gera um número flutuante entre A e B
flutuante = random.uniform(10, 20)

# Gera um número flutuante entre 0 e 1
flutuante2 = random.random()

# Usando o `random` para fazer seleções aleatórias em listas
lista = ['Joao', 'Pedro', 'Rose', 'Maria']
# 1º `choice`: seleciona um item aleatório da lista
ganhador = random.choice(lista)

# 2º `choices`: retorna o fatiamento aleatório da lista (recebendo o número de itens desejados na nova lista como parâmetro). Neste caso a nova lista pode conter VALORES REPETIDOS.
ganhador2 = random.choices(lista, k=2)

# 3º `sample`: executa a mesma tarefa de `choices`, mas não repete valores.
ganhador3 = random.sample(lista, k=2)

# Embaralhando os itens em uma lista com a função `shuffle()`
random.shuffle(lista)


# Gerando uma senha aleatória (com os módulos `random` e `string`)
# definindo as variaveis letras, digitos e caracteres que irão compor a senha
letras = string.ascii_letters  # letras maiusculas e minusculas do alfabeto
digitos = string.digits  # caracteres de 0-9 (0123456789)
caracteres = '!@#$%&*._-'
# acumulando todos os valores possíveis dentro das variáveis acima em uma só
geral = letras + digitos + caracteres
# criando a senha a partir do fatiamento da string formada em `geral`, passando como parâmetro o número de dígitos desejados.
senha = ''.join(random.choices(geral, k=6))

print(senha)
