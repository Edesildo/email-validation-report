import requests as req
import re

# Função para validar o e-mail
def validar_email(email):
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(padrao, email) is not None

# Requisição para obter os usuários
users = req.get("https://jsonplaceholder.typicode.com/users")

# Verifica se a requisição foi bem-sucedida
if users.status_code == 200:
    lista_usuarios = users.json()
    info_usuario = []

    # Itera sobre os usuários e coleta as informações
    for usuario in lista_usuarios:
        nome = usuario.get("name", "N/A")
        empresa = usuario.get("company", {}).get("name", "N/A")
        cidade = usuario.get("address", {}).get("city", "N/A")
        email = usuario.get("email", "N/A")

        # Verifica se o e-mail é válido
        status = "Válido" if validar_email(email) else "Inválido"

        # Formata as informações do usuário
        usuario_info = (
            f"Nome: {nome}\n"
            f"Empresa: {empresa}\n"
            f"Cidade: {cidade}\n"
            f"E-mail: {email} ({status})\n\n"
        )

        # Adiciona as informações formatadas à lista
        info_usuario.append(usuario_info)

    nome_arquivo = "relatorio_usuarios.txt"

    # Escreve as informações no arquivo
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(info_usuario)

    print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
else:
    print("Erro na requisição")
