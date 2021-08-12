<h1 align="center">
  Challenge
</h1>

## 💻 Projeto
Aplicativo para desafio e estudos.


## :hammer_and_wrench: Features 

-   [ ] Autenticação JWT.
-   [ ] Cadastrar um usuário.
-   [ ] Obtém lista de clientes;
-   [ ] Cadastrar Cliente;
-   [ ] Editar Cliente;
-   [ ] Deletar Cliente;
-   [ ] Detalhar Clientes;
-   [ ] Disponibiliza a função de Logout.


## ✨ Tecnologias

-   [ ] Django
-   [ ] Django-Rest-Framework
-   [ ] Django-Rest-Framework-SimpleJWT
-   [ ] Postgres

## Configurando o banco de dados

-Instale ou rode um container com postgres com as seguintes credenciais:


```cl
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '5432'
```

## Executando o projeto

faça um clone do projeto e logo em seguida inicie um ambiente virtual, tendo o python instalado.
Em seguida, siga o passo a passo:
- Rode o comando abaixo, dentro da raiz do projeto -

```cl
  python3 -m venv env
```

- Rode o comando abaixo, para ativar o ambiente, dentro da raiz do projeto -

```cl
  source env/bin/activate #linux
  env\Scripts\activate #windows
```
- Rode os comando abaixo, dentro da raiz do projeto, para instalar as dependências na vm -

```cl
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install psycopg2-binary
pip install django-cors-headers
```
- ou mais simples

```cl
pip install -r requirements.txp
```
- Rode os comando abaixo, para migrar as alterações ao banco -

```cl
python manage.py migrate 
python manage.py makemigrations #se necessário, depois rode o comando acima desse
```
- Rode a api -

```ts
    python manage.py runserver 
```

<br />

<div align="center">
  <small>Desenvolvido por Ailton de Sena Pinheiro - Agosto/2021</small>

  [![GitHub Badge](https://img.shields.io/badge/Ailton_Sena-000?style=for-the-badge&logo=github&logoColor=white&link=https://www.linkedin.com/in/ailtonsenap)](https://github.com/Sena32/)
    [![Linkedin Badge](https://img.shields.io/badge/Ailton_Sena-000?style=for-the-badge&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/ailtonsenap)](https://www.linkedin.com/in/ailtonsenap/) 
</div>
