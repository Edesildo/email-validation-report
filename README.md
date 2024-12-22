Validação de E-mails de Usuários
Este script em Python realiza a validação de e-mails dos usuários a partir de uma API pública (https://jsonplaceholder.typicode.com). Ele verifica se o e-mail de cada usuário está no formato correto e gera um relatório com o status de cada e-mail, seja ele válido ou inválido.

Funcionalidades
Requisição HTTP: O script faz uma requisição para a API de usuários (JSONPlaceholder).
Validação de E-mails: Utiliza uma expressão regular para validar se o e-mail de cada usuário está no formato adequado.
Geração de Relatório: O script gera um arquivo de texto (relatorio_usuarios.txt) com as informações de cada usuário e o status do seu e-mail.
Pré-requisitos
Python 3.x

Biblioteca requests para fazer a requisição HTTP. Caso não tenha a biblioteca instalada, você pode instalá-la executando:

bash
Copiar código
pip install requests
Como Usar
Clone ou baixe o repositório para o seu computador.

Execute o script Python:

bash
Copiar código
python validar_emails.py
O script fará uma requisição para a API de usuários e verificará se os e-mails estão no formato correto.

O resultado será gravado em um arquivo de texto chamado relatorio_usuarios.txt.

Estrutura do Relatório
O arquivo gerado terá o seguinte formato para cada usuário:

vbnet
Copiar código
Nome: [Nome do Usuário]
Empresa: [Nome da Empresa]
Cidade: [Cidade do Usuário]
E-mail: [E-mail do Usuário] (Válido/Inválido)
Exemplo:

makefile
Copiar código
Nome: Leanne Graham
Empresa: Romaguera-Crona
Cidade: Gwenborough
E-mail: Sincere@april.biz (Válido)
Como Funciona
O script faz uma requisição HTTP para a API pública jsonplaceholder.typicode.com para obter uma lista de usuários.
Para cada usuário, ele extrai as informações: Nome, Empresa, Cidade e E-mail.
A função validar_email() é chamada para verificar se o formato do e-mail está correto, usando uma expressão regular.
O status de cada e-mail (Válido/Inválido) é adicionado ao relatório.
O relatório é gerado no formato de um arquivo de texto, relatorio_usuarios.txt, e salvo no diretório de execução.
Exemplo de Execução
bash
Copiar código
$ python validar_emails.py
Arquivo 'relatorio_usuarios.txt' gerado com sucesso!