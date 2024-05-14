from flask import Flask, render_template


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/video')
def video():
    return render_template('video.html')
@app.route('/manga.html')
def manga():
    return render_template('manga.html')
@app.route('/cadastro.html')
def cadastro():
    return render_template('cadastro.html')


if __name__ == "__main__":
    app.run(debug=True)