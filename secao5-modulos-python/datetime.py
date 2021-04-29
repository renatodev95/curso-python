# https://docs.python.org/3/library/datetime.html
from datetime import datetime, timedelta

# Utilizando diretivas
# formato -> 'dia/mês/ano hora:minuto:segundo'
data = datetime(2021, 4, 28, 13, 30, 20)
print(data.strftime('%d/%m/%Y %H:%M:%S'))


# datetime.strptime(date_string, format)
# O primeiro parâmetro recebe o datetime como string e o segundo parâmetro recebe o formato em que deverá ser convertido o datetime.
data = datetime.strptime('28/04/2021', '%d/%m/%Y')
print(data)
print(data.timestamp())  # exibindo a data como timstamp


# Convertendo um timestamp em uma data padrão
# O método recebe o timestamp como parâmetro para conversão
data = datetime.fromtimestamp(1618887600.0)
print(data)


# Acrescentando/Diminuindo a data original com a classe timedelta
# Nesse exemplo o timedelta recebe o valor 5 como parâmetro de dias.
data = datetime.strptime('15/03/1995 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(days=5, seconds=59*60) # o parâmetro de segundos está recebendo um cálculo simples que resulta em 59 minutos.
print(data.strftime('%d/%m/%Y %H:%M:%S'))


# Calculando a diferença entre a data inicial e a data final
d1 = datetime.strptime('15/03/1995 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('20/03/1995 22:33:00', '%d/%m/%Y %H:%M:%S')
print(d1.time()) # exibindo apenas a HORA da data informada
dif = d2 - d1
print(dif) # exibição padrão da diferença
print(dif.seconds) # exibição dos segundos da diferença de horas (2:33:00)
print(dif.total_seconds()) # exibição dos segundos totais da diferença
print(dif.days) # exibição da quantidade de dias da diferença
print(d2 > d1) # comparação lógica entre as datas
