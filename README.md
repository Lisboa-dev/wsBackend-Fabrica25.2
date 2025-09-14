<h1 align="center" style="font-weight: bold;">Project name 💻</h1>

<p align="center">
 <a href="#tech">Technologies</a> • 
 <a href="#started">Getting Started</a> • 
  <a href="#routes">API Endpoints</a> •
 <a href="#contribute">Contribute</a>
</p>

<p align="center">
    <b>uma descrição simples do projeto</b>
</p>

<h2 id="technologies">💻 tecnologias</h2>

- Django 
- Pythoon
- mysql
  

<h2 id="started">🚀 iniciando o projeto</h2>

<h3>Prerequisitos</h3>

- django: 5.2.6
- djangorestframework==3.16.1
- mysqlclient==2.2.7
- requests==2.32.5

<h3>Clone</h3>

```bash
git clone https://github.com/Lisboa-dev/wsBackend-Fabrica25.2.git
```

<h3>Config .env variables</h2>

existe um arquivo env.py dentro do projeto, configure as infornações do seu banco nele

<h3>iniciar o projeto</h3>

How to start your project

```bash
rode sua venv com: py venv <venvNamed>
active:  venvNamed/Scrips/activate
para consumir dependencias em reqquirements: pip install -r requirements.txt
depois vá para a pasta que contem o manage.py
rode py manage.py makemigrations
rode py manage.py migrate
rode py manage.py runserver

bem, agora ja deve estar rodando
```

<h2 id="routes">📍 API Endpoints</h2>


​
| route               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>user/token/ </kbd>            |   [response details](#get-auth-detail)
| <kbd>user/Post/ </kbd>             |   [request details](#post-auth-detail)
| <kbd>user/token/refresh</kbd>      |   [request details](#pos / user/token)
| <kbd>books/GET/ </kbd>             |   [request details](#post-auth-detail)
| <kbd>books/Post/ </kbd>            |   [request details](#post-auth-detail)
| <kbd>bookd/Delete/<int:id> </kbd>  |   [request details](#post-auth-detail)
| <kbd> collection/clusters </kbd>   |   [request details](#post-auth-detail)
| <kbd> collection/Get  </kbd>       |   [request details](#post-auth-detail)
| <kbd> / </kbd>                     |   [request details](#post-auth-detail)
| <kbd> / </kbd>                     |   [request details](#post-auth-detail)
| <kbd> / </kbd>                     |   [request details](#post-auth-detail)


<h3 id="get-auth-detail"> post /user/Post/</h3>

**RESPONSE**
```json
{
  "username": "Matheus Lira",
  "email": "her-email@gmail.com"
}
```
**REQUEST**
{
"username":"nome",
"email":"seu emails" opcional,
"password":"seu Password"
}

<h3 id="post-auth-detail">post /user/tokrn/</h3>

**resposne**
```json
{
"refresh":"refrash-token"
"access":"token"
}
```

**request**
```json
{
  "username":"you username",
 "pasxword":"your pass")
}
```

