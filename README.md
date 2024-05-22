# Financial Control

Este é um sistema para gerenciamento de fluxo de caixa de uma barbearia, desenvolvido em Django.

## Tecnologias Utilizadas

- Python
- Django

## Como Rodar o Projeto Localmente

### Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- Python >= 3.6
- pip (gerenciador de pacotes do Python)

### Passos

1. Clone este repositório para o seu computador:
git clone https://github.com/seu-usuario/financial-control.git


2. Navegue até o diretório do projeto:
cd financial-control


3. Crie um ambiente virtual (recomendado):
python -m venv venv


4. Ative o ambiente virtual:
- No Windows:
  ```
  venv\Scripts\activate
  ```
- No Linux/macOS:
  ```
  source venv/bin/activate
  ```

5. Instale as dependências do projeto:
pip install -r requirements.txt


6. Execute as migrações do banco de dados:
python manage.py migrate


7. Crie um superusuário para acessar a área de administração:
python manage.py createsuperuser


8. Inicie o servidor de desenvolvimento:
python manage.py runserver


9. Abra seu navegador e acesse o seguinte endereço:
http://localhost:8000/


10. Para acessar a área de administração, vá para:
 ```
 http://localhost:8000/admin/
 ```

 Faça login com as credenciais do superusuário criado anteriormente.

11. Pronto! Agora você pode explorar e utilizar o sistema de gerenciamento de fluxo de caixa da barbearia localmente.

## Contribuição

Se você quiser contribuir para este projeto, por favor, abra uma issue ou envie um pull request.
