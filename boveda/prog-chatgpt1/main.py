import imaplib
import email
from email.header import decode_header

# Suas credenciais
# https://myaccount.google.com/apppasswords
username = "fpujaico.drive@gmail.com" # "fernando.pujaico.rivera@gmail.com"
password = input("senha Gmail APP")  


# Conectar ao servidor IMAP do Gmail
mail = imaplib.IMAP4_SSL("imap.gmail.com")
try:
    mail.login(username, password)
except Exception as e:
    print(f"Ocorreu um erro ao tentar fazer login: {e}")
    exit(1)

# Selecionar a caixa de entrada
mail.select("inbox")

# Procurar por e-mails não lidos
status, messages = mail.search(None, 'UNSEEN')

if status != "OK":
    print("Erro ao buscar e-mails não lidos.")
    exit(1)

# Obter as IDs das mensagens não lidas
messages = messages[0].split()

# Verificar se há e-mails não lidos
if len(messages) == 0:
    print("Não há e-mails não lidos.")
else:
    print(f"Você tem {len(messages)} e-mail(s) não lido(s).")

    # Exibir o assunto dos e-mails não lidos
    for msg_num in messages:
        try:
            # Usar mail.fetch sem marcar os e-mails como lidos
            status, msg_data = mail.fetch(msg_num, "(BODY.PEEK[HEADER.FIELDS (SUBJECT)])")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    # Parse o e-mail
                    msg = email.message_from_bytes(response_part[1])
                    # Decodificar o assunto
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    # Exibir o assunto
                    print(f"📩 Assunto: {subject}")
            
            # A chave de "UNSEEN" não foi modificada, então o e-mail permanece não lido
        except Exception as e:
            print(f"Ocorreu um erro ao processar a mensagem: {e}")
