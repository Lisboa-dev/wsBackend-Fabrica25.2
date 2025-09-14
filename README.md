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

insira um arquivo env.py dentro do libary-project, configure as infornações do seu banco nele. se baseie no env.exemple, mas ponha dentro do library-project

<h3>iniciar o projeto</h3>

How to start your project

```bash
rode sua venv com: py venv <venvNamed>
active:  venvNamed/Scrips/activate
para consumir dependencias em reqquirements: pip install -r requirements.txt
pip install rest_framework_simplejwt
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
| <kbd>books/Delete/<int:id>/ </kbd>  |   [request details](#post-auth-detail)
| <kbd> collection/clusters </kbd>   |   [request details](#post-auth-detail)
| <kbd> collection/Get/int id  </kbd>       |   [request details](#post-auth-detail)



<h3 id="get-auth-detail"> post /user/Post/</h3>

**RESPONSE**
```json
{
  "username": "Matheus Lira",
  "email": "her-email@gmail.com"
}
```
**REQUEST**
```json
{
"username":"nome",
"email":"seu emails" opcional,
"password":"seu Password"
}
```
<h3 id="post-auth-detail">post /user/token/</h3>

**RESPONSE**
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


<h3 id="post-auth-detail">get books/GET/</h3>

**RESPONSE**
```json
{
{
 {
	"data": [
		{
			"title": "Saber não saber",
			"author": "Alcides Buss",
			"genres": "Indefinido",
			"date_publi": 2009,
			"number_pages": 141,
			"publisher": "Caminho de Dentro Edições",
			"language": "por",
			"urls": "https://openlibrary.org/works/OL15573019W",
			"image_url": null,
			"availability": "Indefinido",
			"format": "Indefinido"
		},
		{
			"title": "Saber Ser, Saber Estar (Spanish Edition)",
			"author": "Monste Soler, Montse Soler",
			"genres": "Indefinido",
			"date_publi": 1999,
			"number_pages": null,
			"publisher": "Planeta Pub Corp",
			"language": "Indefinido",
			"urls": "https://openlibrary.org/works/OL33703897W",
			"image_url": null,
			"availability": "Indefinido",
			"format": "Indefinido"
		},
		

	]
}
}
```

**REQUEST**
```
GET http//localhost:Port/books/Get/?q=saber&limit=2&page=5
```

<h3 id="post-auth-detail">Post books/Post/</h3>

<h2>Atenção</h2>

Para efetuar requisições Pust, o individuo devera ter no header os seguntes paametros : tag: *Authorization*  com valor *Bearer <token>*

Você deverá ter ao menos um cluster para vincular

**REQUEST**
```jason

{
	  "title": "Saber não saber",
			"author": "Alcides Buss",
			"genres": "Indefinido",
			"date_publi": 2009,
			"number_pages": 141,
			"publisher": "Caminho de Dentro Edições",
			"language": "por",
			"urls": "https://openlibrary.org/works/OL15573019W",
			"image_url": null,
			"availability": "Indefinido",
			"format": "Indefinido",
   "cluster"> cluster_id
}
```

**RESPONSE**
```jason
{
   Data:{
      "title": "Saber não saber",
   			"author": "Alcides Buss",
   			"genres": "Indefinido",
   			"date_publi": 2009,
   			"number_pages": 141,
   			"publisher": "Caminho de Dentro Edições",
   			"language": "por",
   			"urls": "https://openlibrary.org/works/OL15573019W",
   			"image_url": null,
   			"availability": "Indefinido",
   			"format": "Indefinido",
      "cluster"> cluster_id
   }

}
```


<h3 id="post-auth-detail">post books/Delete/<int:id>/</h3>
 
<h2>Atenção</h2>
Para efetuar requisições Delete, o individuo devera ter no header os seguintes parametros : tag: *Authorization*  com valor *Bearer <token>*

**REQUEST**
Delete books/Delete/1/

**RESPONSE**
```json
  {'data':'Book 1 deletado com sucesso'}
```

<h3 id="post-auth-detail">all /collection/cluster/</h3>
Para efetuar requisições o individuo devera ter no header os seguintes parametros : tag: *Authorization*  com valor *Bearer <token>*

**REQUEST**

pode ser feito em qualquer formato, segue o modelo generico do views set

dados para requisição post: "name", "genres", "description"


<h3 id="post-auth-detail">GET /collection/Get/id/</h3>
Para efetuar requisições o individuo devera ter no header os seguintes parametros : tag: *Authorization*  com valor *Bearer <token>*

**REQUEST**
   GET http//localhost:Port/collection/Get/id/
**RESPONSE**
```json
   {data : [
       		{
			"title": "Saber não saber",
			"author": "Alcides Buss",
			"genres": "Indefinido",
			"date_publi": 2009,
			"number_pages": 141,
			"publisher": "Caminho de Dentro Edições",
			"language": "por",
			"urls": "https://openlibrary.org/works/OL15573019W",
			"image_url": null,
			"availability": "Indefinido",
			"format": "Indefinido"
   "cluster":"1"
		},
		{
			"title": "Saber Ser, Saber Estar (Spanish Edition)",
			"author": "Monste Soler, Montse Soler",
			"genres": "Indefinido",
			"date_publi": 1999,
			"number_pages": null,
			"publisher": "Planeta Pub Corp",
			"language": "Indefinido",
			"urls": "https://openlibrary.org/works/OL33703897W",
			"image_url": null,
			"availability": "Indefinido",
			"format": "Indefinido"
    "cluster":"3"
		},
		
]}
```













