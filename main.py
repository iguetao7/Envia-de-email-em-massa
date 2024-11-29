from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail



chave_api_sendgrid = 'SUA CHAVE'

conta_sendgrid = SendGridAPIClient(chave_api_sendgrid)

email = Mail(from_email='EMAIL DE ENVIO', to_emails=['EMAIL DE DESTINO', 'EMAIL DE DESTINO'], subject='Email enviado pelo sendgrid',
             html_content="""<p>Email enviado com sucesso,</p> <p>Até o próximo.</p> """)

resposta = conta_sendgrid.send(email)

print(resposta.status_code)
