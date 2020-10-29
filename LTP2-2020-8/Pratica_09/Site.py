
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/ola')
def ola():
    return 'ola mundo! Meu nome é Euller Felix'

@app.route('/pagina')
def primeira_pagina():
    return"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>

            <h1>This is a Heading</h1>
            <p>This is a paragraph.</p>

        </body>
    </html>
    """

@app.route('/pagina2')
def segunda_pagina():
    return"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Meu site um pouco melhor</title>
        </head>
        <body>

            <h1>informações</h1>
            <p>Isto é um teste.</p>
            <p>Teste 1,2 teste 1,2, som 1, 2</p>

        </body>
    </html>
    """

@app.route('/pagina3')
def terceira_pagina():
    return """
     <!DOCTYPE html>
     <html>
        <head>
            <title>Meu Site um Pouco Melhor</title>
        </head>
        <body>

            <h1>Informações</h1>
            <p>Este texto é sobre informações gerais.</p>
            <p>Mias detalhes serão apresentados no futuro!</p>
            <iframe width="560" height="315" src="https://www.youtube.com/embed/b3nEaIPNx6Y" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        </body>
     </html>
    """
