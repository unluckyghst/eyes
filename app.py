from flask import Flask, render_template, request, redirect, flash, url_for
app = Flask(__name__)
app.secret_key = "cheve_muito_segura"

@app.route('/esqueci-minha-senha')
def esquecisenha1():
    return render_template ('esqueci-minha-senha.html')

@app.route('/esqueci-minha-senha2')
def esquecisenha2():
    return render_template('esqueci-minha senha2.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

if __name__== '__main__':
    app.run(debug=True)

@app.route("/verificar-login", methods=["post"]) 
def verificar_login():
    username = request.form['username']
    password = request.form['password']

    if username in usuarios and usuarios[username] == password :
        return redirect(url_for('galeria'))
    else:
        flash('usuário')






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

if __name__=='__main__':
    app.run(debug=True)

usuarios={
    'unlucky' : 'mari1234'
}

@app.route('/verificar-login', methods=['POST'])
def verificar_login():
    username = request.form['username']
    password = request.form['password']

    if username in usuarios and usuarios [username] == password:
       return f"Bem Vindo, {username}!"
    else:
       return "Usuário ou senha inválidos."