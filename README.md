# Niveis de Acesso, com rotinas - Django Rest Framework

>Este projeto é uma aplicação web desenvolvida com Django para gerenciar níveis de acesso de usuários em um sistema.
>Ele oferece funcionalidades para listar diferentes níveis de acesso, além de associar esses níveis aos usuários.

## Funcionalidades Principais
> - Cadastro de usuários com diferentes níveis de acesso.
> - Associação de níveis de acesso aos usuários.
> - Visualização detalhada dos usuários e seus respectivos níveis de acesso.

## Requisitos
> - Python 3.11 ou superior
> - Django 5
> - Postgres
> - Outras dependências podem ser encontradas no arquivo requirements.txt.

## Configuração
> Banco de dados com postgresql,
   - configure o arquivo .env;
   - certifique-se de configurar o settings.py
   
```bash
    'NAME': 'nomedobanco',
    'USER' : 'seuuser',
    'PASSWORD': ' ',
    'HOST': 'localhost',
    'PORT': '5432',

```
>- Faça o migrate

```bash
python manage.py makemigrate
python manage.py migrate
