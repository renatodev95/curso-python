# O método utilizado anteriormente (com o módulo `calendar`) para verificar o último dia de cada mês pode não funcionar corretamente quando o ano for bissexto.

# Você também pode utilizar a função monthrange de calendar para pegar o número do dia na semana (entre 0-6) e último dia do mês (entre 28-31), exemplo:

from datetime import datetime
from calendar import monthrange

# Retorna uma tupla contendo o número do dia na semana (0-6)
# e último dia de fevereiro de 2020
print(monthrange(2020, 2))

# Saída - (5, 29)
# O 5 significa que é um sábado
# O 29 significa que este é o último dia do mês

# O número do dia na semana vai de 0 a 6 (segunda é 0, domingo é 6).

# Caso queira retornar apenas um valor, você pode fazer o desempacotamento, assim:
dia_semana, ultimo_dia = monthrange(2020, 2)
print(ultimo_dia)  # Saída: 29 (último dia de fevereiro de 2020)

# Você também pode criar uma lista, assim como mdays, contendo todos os últimos dias de meses do ano atual:

ultimos_dias_de_meses_do_ano_atual = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
]
print(ultimos_dias_de_meses_do_ano_atual)
# Saída: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Isso deve solucionar os problemas do ano bissexto.



