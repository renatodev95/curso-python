import os

# Algoritmo para percorrer os arquivos dentro de um caminho de diretórios e localizar um ou mais arquivos a partir do termo procurado.

caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo: ')


def formata_tamanho(size):
    base = 1024
    kilo = base
    mega = base**2
    giga = base**3
    tera = base**4
    peta = base**5

    if size < kilo:
        # na primeira verificação não é necessário manipular o valor de `size`
        texto = 'B'
    elif size < mega:
        size /= kilo
        texto = 'K'
    elif size < giga:
        size /= mega
        texto = 'M'
    elif size < tera:
        size /= giga
        texto = 'G'
    elif size < peta:
        size /= tera
        texto = 'T'
    else:
        size /= peta
        texto = 'P'
    size = round(size, 2)
    return f'{size}{texto}'.replace('.', ',')


contador_de_arquivos = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                contador_de_arquivos += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print(f'Encontrei o arquivo: {arquivo}')
                print(f'Caminho: {caminho_completo}')
                print(f'Nome: {nome_arquivo}')
                print(f'Extensão: {ext_arquivo}')
                print(f'Tamanho: {tamanho}')
                print(f'Tamanho formatado: {formata_tamanho(tamanho)}')
            except PermissionError as e:
                print('Sem permissão.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido: ', e)

print()
print(f'{contador_de_arquivos} arquivo(s) encontrado(s).')


# Quando houver barras invertidas no caminho informado (no caso do Windows) é necessário urilizar o `r` antes da string com o caminho:

# caminho_windows = r'C:\programs\anything'
