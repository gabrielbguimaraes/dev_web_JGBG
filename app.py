from flask import Flask, render_template


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/video')
def video():
    return render_template('video.html')

if __name__ == "__main__":
    app.run(debug=True)