from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file("home.html")

@app.route('/results/')
def results():
    return app.send_static_file("results.html")

if __name__ == '__main__':
    app.run(debug=True)
