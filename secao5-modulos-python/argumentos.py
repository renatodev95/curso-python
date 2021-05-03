#!/usr/bin/env python3
import sys
import os

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Faltam argumentos:')
    print('-a', 'Para listar todos os arquivos nesta pasta', sep='\t')
    print('-d', 'Para listar todos os diretórios nesta pasta', sep='\t')
    # Se não houverem argumentos a linha abaixo vai finalizar o script
    sys.exit()


so_arquivos = False
if '-a' in argumentos:
    so_arquivos = True

so_diretorios = False
if '-d' in argumentos:
    so_diretorios = True


# Listagem dos arquivos e diretórios na pasta atual.
# Esse '.' que está sendo passado como parâmetro é referente ao DIRETÓRIO ATUAL
for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if so_diretorios:
        if os.path.isfile(arquivo):
            print(arquivo)

# No topo do algoritmo temos um cabeçalho para eliminar a necessidade de informar a versão do python que deve ser executada no terminal linux quando for rodar o arquivo '.py'.
