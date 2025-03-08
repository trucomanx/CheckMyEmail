import imaplib
import email
from email.header import decode_header


# Conectar ao Gmail via IMAP
def get_data_emails(email_user, password_app, url="imap.gmail.com", email_type='UNSEEN'):
    
    mail = imaplib.IMAP4_SSL(url)
    
    try:
        mail.login(email_user, password_app)
    
    except Exception as e:
        print(f"Error logging in: {e}")
        return mail, None

    mail.select("inbox")
    status, messages = mail.search(None, email_type)

    if status != "OK":
        print("Error searching for emails")
        return mail, None

    messages = messages[0].split()

    return mail,messages


def get_subject_and_body(mail, messages):
    Emails = []
    
    for msg_num in messages:
        # Buscar o e-mail sem marcá-lo como lido
        status, msg_data = mail.fetch(msg_num, "(BODY.PEEK[])")
        
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                # Parse o e-mail
                msg = email.message_from_bytes(response_part[1])
                
                # Decodificar o assunto
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                
                # Obter a data
                date = msg["Date"]
                
                # Estrutura para armazenar os dados do e-mail
                email_data = {"subject": subject, "body": "", "date": date}

                # Obter o corpo do e-mail
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        
                        if "attachment" not in content_disposition:
                            try:
                                email_data["body"] = part.get_payload(decode=True).decode()
                                break  # Pega o primeiro corpo de texto encontrado
                            except:
                                pass
                else:
                    email_data["body"] = msg.get_payload(decode=True).decode()
                    
                Emails.append(email_data)
    
    return Emails
    
def gett_subject_messages(mail, messages):
    Emails = []
    
    for msg_num in messages:
        # Usar mail.fetch sem marcar os e-mails como lidos
        status, msg_data = mail.fetch(msg_num, "(BODY.PEEK[HEADER.FIELDS (SUBJECT DATE)])")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                # Parse o e-mail
                msg = email.message_from_bytes(response_part[1])
                
                # Decodificar o assunto
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                
                # Obter a data
                date = msg["Date"]
                
                # Adicionar ao array de e-mails
                Emails.append({"subject": subject, "body": "", "date": date})

    return Emails
