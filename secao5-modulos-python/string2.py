# Criando templates HTML com o módulo string em Python

# Enviando e-mails com Python
from string import Template
from datetime import datetime

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib


destinatario = 'EMAIL_DESTINO@EMAIL.COM'
remetente = 'EMAIL_REMETENTE@EMAIL.COM'
senha = 'SUASENHA'


with open('string2.html', 'r', encoding='utf-8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(
        nome='NOME DO DO DESTINARARIO', data=data_atual)

# CRIANDO CABEÇALHO DO EMAIL
msg = MIMEMultipart()
# informando o remetente da mensagem
msg['from'] = 'NOME DE QUEM ESTÁ ENVIANDO A MENSAGEM'
# informando o destinatário da mensagem
# (variavel contendo a string com o email do destinatario)
msg['to'] = destinatario
# informando o assunto do e-mail
msg['subject'] = 'Atenção! Este é um e-mail de teste.'

# CORPO DO EMAIL
# abaixo é necessário informar o tipo de documento no segundo parâmetro
corpo = MIMEText(corpo_msg, 'html')

# inserindo o corpo do email na MENSAGEM
msg.attach(corpo)

# Envio de imagem em anexo
# Abrindo arquivo de imagem em modo de 'leitura de bytes' (`rb`).
with open('IMAGEM.JPG', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        # variáveis contendo as strings com o email e senha do remetente
        smtp.login(remetente, senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)
