import base64
import json
from cryptography.fernet import Fernet


# Função para gerar uma chave com base na password mestra
def generate_key(master_password):
    return base64.urlsafe_b64encode(master_password.ljust(32).encode()[:32])




# Função para carregar credenciais criptografadas
def load_credentials(file_path, master_password):
    chave = generate_key(master_password)
    cipher = Fernet(chave)

    try:
        with open(file_path, "rb") as arquivo:
            dados_criptografados = arquivo.read()
        
        dados = json.loads(cipher.decrypt(dados_criptografados).decode())
        
        return dados
        
    except Exception:
        print("❌ You have an incorrect file or corrupt file.")
        return None

# Criar credenciais criptografadas
def add_to_credentials_file(file_path,email,password_app,master_password):
    
    dados = load_credentials(file_path, master_password)
    if dados is None:
        dados = dict()

    chave = generate_key(master_password)
    cipher = Fernet(chave)

    dados[email] = password_app
    
    dados_criptografados = cipher.encrypt(json.dumps(dados).encode())

    with open(file_path, "wb") as arquivo:
        arquivo.write(dados_criptografados)

