#bibliotecas a serem importadas
from flask import Flask, render_template, request, redirect, url_for 
import json, os

#constante de busca
ARQUIVO_USUARIOS = "data/usuarios.json"
app = Flask(__name__)

#funções auxiliares
def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        try:
            with open(ARQUIVO_USUARIOS, "r") as f:
                return json.load(f) 
        except json.JSONDecodeError:
            return{}
        return{}
    
def salvar_usuarios(usuarios):
    os.makedirs(os.path.dirname(ARQUIVO_USUARIOS), exist_ok=True)
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

#estabelecendo rotas do flask
@app.route("/")
def home():
    return render_template ("login.html")

@app.route("/login", methods= ["POST"])
def login():
    usuario = request.form["usuario"]
    senha = request.form["senha"]
    usuarios = carregar_usuarios
    
    if usuarios.get(usuario) == senha:
        return f"<h1>Bem vindo, {usuario}!</h1>"
    else: 
        return "<h1>Usuário ou senha incorretos.</h1> <a href='/'>Tentar novamente</a>"

@app.route("/cadastro")
def cadastro():
    return render_template ("cadastro.html")

@app.route("/cadastro", methods=["POST"])
def cadastrar():
    usuario = request.form["usuario"].strip()
    senha = request.form["senha"]
    confirma = request.form["confima"]
    
    usuarios = carregar_usuarios()
    
    if not usuario:
        return "Nome de usuário vazio."
    if usuario in usuarios:
        return "Usuário já cadastrado."
    if senha != confirma:
        return "As senhas não coincidem."

    usuarios[usuario] = senha
    salvar_usuarios(usuarios)
    return f"Usuário {usuario} criado com sucesso! <a href='/'>Ir para login</a>"

if __name__ == "__main__":
    app.run(debug=True)