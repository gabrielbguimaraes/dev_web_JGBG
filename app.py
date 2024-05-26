from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__, static_url_path='/static')

# Configurações do banco de dados diretamente no código
db_config = {
    'host': 'mysql',
    'user': 'root',
    'password': '#Ovelha354',
    'database': 'registro_onepiece'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video.html')
def video():
    return render_template('video.html')

@app.route('/manga.html')
def manga():
    return render_template('manga.html')

@app.route('/cadastro.html', methods=['GET', 'POST'])
def cadastro():
    try:
        conexao = mysql.connector.connect(**db_config)
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT COUNT(*) FROM users_opb")
            count = cursor.fetchone()["COUNT(*)"]

            if count >= 15:
                cursor.execute("DELETE FROM users_opb")
                conexao.commit()

            if request.method == 'POST':
                nome = request.form["username"]
                email = request.form["email"]
                senha = request.form["password"]

                consulta = "INSERT INTO users_opb (nome_usuario, email, senha) VALUES (%s, %s, %s)"
                valores = (nome, email, senha)
                cursor.execute(consulta, valores)
                conexao.commit()

                return redirect(url_for('lista_usuarios'))  # Redirecionar para a página de usuários após o cadastro
            else:
                return render_template('cadastro.html')
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return "Erro ao conectar ao banco de dados."
    finally:
        if conexao.is_connected():
            conexao.close()

@app.route('/users.html')
def lista_usuarios():
    try:
        conexao = mysql.connector.connect(**db_config)
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM users_opb")
            users = cursor.fetchall()
            return render_template('users.html', users=users)
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return "Erro ao conectar ao banco de dados."
    finally:
        if conexao.is_connected():
            conexao.close()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
