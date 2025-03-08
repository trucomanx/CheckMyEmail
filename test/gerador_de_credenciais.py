import sys
sys.path.append('../src')


import check_my_email.lib_credentials as lib_credentials
import getpass
import os

if __name__ == "__main__":
    file_path = os.path.expanduser("~/credenciais.enc")

    master_password = getpass.getpass("Crie uma password mestra para proteger suas credenciais: ")
    
    email_user = "fpujaico.drive@gmail.com"
    password_app = getpass.getpass("Digite sua password de aplicativo do Gmail: ")
    
    lib_credentials.add_to_credentials_file(file_path,email_user,password_app,master_password)

    print("✅ Arquivo de credenciais criado com sucesso!")
    
