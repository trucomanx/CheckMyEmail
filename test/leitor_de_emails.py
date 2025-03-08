import sys
sys.path.append('../src')


import check_my_email.lib_credentials as lib_credentials
import check_my_email.lib_emails as lib_emails


import os
import getpass

if __name__ == "__main__":
    file_path = os.path.expanduser("~/credenciais.enc")
    
    master_password = getpass.getpass("Digite sua password mestra: ")
    
    email_user = "fpujaico.drive@gmail.com"
    
    credentials = lib_credentials.load_credentials(file_path, master_password)
    
    password_app = credentials.get(email_user)
    
    mail,messages = lib_emails.get_data_emails(email_user, password_app)

    if len(messages) == 0:
        print("Não há e-mails não lidos.")
    else:
        print(f"Você tem {len(messages)} e-mail(s) não lido(s).")
        emails = lib_emails.get_subject_and_body(mail, messages)
        
        for email in emails:
            print("")
            print(email)
        
