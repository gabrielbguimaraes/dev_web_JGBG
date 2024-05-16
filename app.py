from flask import Flask, render_template, request
import mysql.connector
from dotenv import load_dotenv

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/video.html')
def video():
    return render_template('/video.html')

@app.route('/manga.html')
def manga():
    return render_template('/manga.html')

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="#Ovelha354",
    database="registro_onepiece"
)
cursor = conexao.cursor()

@app.route('/cadastro.html', methods=['GET','POST'])
def cadastro():
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
        return render_template('/cadastro.html')
    else:
        return render_template('/cadastro.html')

if __name__ == "__main__":
    app.run(debug=True)
