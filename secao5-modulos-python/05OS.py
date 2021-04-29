import os
import shutil

# Este algoritmo atende o propósito simples de mover os arquivos de uma pasta para outra.


caminho_original = input("Informe o caminho original: ")
caminho_novo = input("Informe o novo caminho: ")

# Abaixo o algoritmo tenta criar um novo diretório com o caminho especificado na variável `caminho_novo`. Caso já exista essa pasta, será apresentada uma mensagem de aviso (se quiser pode apenas configurar um `pass` no `except` para que o erro não seja exibido)
try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

# O primeiro loop for vai caminhar pelo caminho_original
# O segundo loop vai tratar apenas os arquivos e realizar os procedimentos desejados.
for root, dirs, files in os.walk(caminho_original):
    for file in files:
        # transferindo cada arquivo de files para a nova pasta
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        
        # movendo o arquivo do antigo caminho para o novo caminho;
        shutil.move(old_file_path, new_file_path)
        print(f'Arquivo {file} movido com sucesso!')

        # também é possível fazer a CÓPIA dos arquivos do caminho antigo
        # para o novo caminho, para isso, basta substituir o método `move`
        # (do `shutil`) para `copy`.
        # Exemplo de cópia apenas com arquivos `.srt`:

        # if '.srt' in file:
            # shutil.copy(old_file_path, new_file_path)
            # print(f'Arquivo {file} copiado com sucesso!')

        # Exemplo de exclusão dos arquivos copiados:
        # basta substituir o método `move` (do `shutil`) para `remove`.

        # MUITO CUIDADO COM A EXCLUSÃO, NÃO TEM RETORNO!
        # IMPORTANTE: na LINHA 18, o parâmetro para os.walk() DEVE SER O `caminho_novo` e não o `caminho_original`, pois são os arquivos da nova pasta que serão excluídos.

            # if '.srt' in file:
            # shutil.remove(old_file_path, new_file_path)
            # print(f'Arquivo {file} copiado com sucesso!')


