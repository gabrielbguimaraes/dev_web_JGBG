from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

app = Flask(__name__, static_url_path='/static')

MYSQL_HOST: os.getenv("MYSQL_HOST")
MYSQL_USER: os.getenv("MYSQL_USER")
MYSQL_PASSWORD: os.getenv("MYSQL_PASSWORD")
MYSQL_DB: os.getenv("MYSQL_DB")

conexao = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password="MYSQL_PASSWORD,
    database=MYSQL_DB
)
cursor = conexao.cursor()

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/video.html')
def video():
    return render_template('/video.html')

@app.route('/manga.html')
def manga():
    return render_template('/manga.html')

@app.route('/cadastro.html', methods=['GET','POST'])
def cadastro():
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) FROM users_opb")
    count = cursor.fetchone()["COUNT(*)"]

    if count >= 15:
        cursor.execute("DELETE FROM users_opb")
        conexao.commit()

    if request.method == 'POST':
        nome = request.form["username"]
        email = request.form["email"]
        senha = request.form["password"]

        # Criar um cursor para executar consultas
        cursor = conexao.cursor()

        # Consulta SQL para inserir um novo registro na tabela
        consulta = "INSERT INTO users_opb (nome_usuario, email, senha) VALUES (%s, %s, %s)"
        valores = (nome, email, senha)

        cursor.execute(consulta, valores)
        conexao.commit()

        cursor.close()
        return redirect(url_for('lista_usuarios'))  # Redirecionar para a página de usuários após o cadastro
    else:
        return render_template('/cadastro.html')

@app.route('/users.html')
def lista_usuarios():
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users_opb")
    users = cursor.fetchall()
    return render_template('/users.html', users=users)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
