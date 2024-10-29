# Importanto a biblioteca do flask para fazer um site dinamico
from flask import Flask, render_template, request

app = Flask(__name__)

# Definindo a rota principal do site
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/esqueci')
def esqueci():
    return render_template('esqueci.html')

@app.route('/novaSenha')
def novaSenha():
    return render_template('novaSenha.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/configuração')
def configuração():
    return render_template('configuração.html')

# Parte principal do programa em Python
if __name__=='__main__':
    app.run(debug=True)

@app.route('/verificar-login', methods=['POST'])
def verificar_login();

username = request.form['username']
password = request.form['password']

if username in usuarios and usuarios [username] == password:
    return f"Bem Vindo, {username}!"
    else:
        return "Usuário ou senha inválidos."