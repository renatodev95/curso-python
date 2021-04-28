from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

# Inicialmente o padrão de saída da variável `formatacao` estava em inglês. Mas com a função `setlocale` e a constante LC_ALL é possível configurar o padrão de saída para o lugar onde a máquina (computador) se encontra.

setlocale(LC_ALL, 'pt_BR.utf-8')

# Não esquecer das aspas vazias após o primeiro parâmetro.
# Caso queira ser explícito quanto ao idioma que deseja padronizar, pode usar a string 'pt_BR.utf-8' (padrão do país desejado).

# atribuindo a data atual à variável dt.
dt = datetime.now()
# Definindo o mês atual para depois verificar quantos dias tem esse mês, ou sabser qual o  último dia desse mês com o módulo `calendar`.
mes_atual = int(dt.strftime('%m'))
# utilizando o método strftime para formatar a data.
formatacao1 = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao1)
print(formatacao2)

# `mdays` é uma lista contendo a quantidade de dias correspondente a cada mês do ano, se acessarmos essa lista no índice do `mês_atual`, encontramos a quantidade de dias desse mês.
print(mes_atual)
print(mdays[mes_atual])
