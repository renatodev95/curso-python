# Criando templates HTML com o módulo string em Python

from string import Template
from datetime import datetime

# abaixo foi repassado o parâmetro `enconding='utf-8` para evitar possíveis erros de apresentação de caracteres específicos no email.
with open('string1.html', 'r', encoding='utf-8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(
        nome='user', data=data_atual)

print(corpo_msg)


# `SUBSTITUTE` vs `SAFE_SUBSTITUTE` (métodos da classe Template)
# Na linha 10, o método `substitute` espera receber todos os placeholders do documento HTML como parâmetro, caso não sejam informados todos, será levantada uma excessão de KeyError no programa. Mas é possível contornar esse problema com o método `safe_substitute`, onde os placeholders que não forem informados serão exibidos da mesma forma como se encontram no template html.


# NOTA SOBRE O DOCUMENTO HTML:
# Enquanto havia um comentário dentro do documento HTML, o script estava retornando erro, então foi necessário removê-lo.
# A nota sobre o comentário removido do documento html original esclarece sobre o uso do símbolo de `$` para identificar os "placeholders" (strings que vão receber os valores das variáveis do algoritmo python no documento HTML).
