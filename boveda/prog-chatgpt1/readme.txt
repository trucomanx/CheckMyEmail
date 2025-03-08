Esse erro ocorre porque o Google está solicitando uma senha de aplicativo específica para autenticar a conexão IMAP. Isso acontece porque você está tentando fazer login com sua senha normal, mas o Google exige uma senha de aplicativo quando a autenticação de dois fatores (2FA) está ativada.
Como corrigir o problema:

    Ativar a autenticação de dois fatores (2FA), caso ainda não tenha feito.

    Gerar uma senha de aplicativo:
        Vá até Página de segurança da sua conta Google.
        Na seção "Acesso a Google", clique em "Senhas de app".
        Selecione o dispositivo e o tipo de aplicativo (no caso, "Outro" e insira algo como "IMAP Python").
        O Google gerará uma senha de aplicativo, que será uma sequência de 16 caracteres (sem espaços).

    Usar a senha de aplicativo no código:
        Ao invés de usar a sua senha normal, substitua no código a linha:

password = "sua_senha_de_app"  # Ou sua senha normal, se 2FA não estiver ativado

pela senha de aplicativo que você gerou.
