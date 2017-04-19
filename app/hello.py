from flask import Flask, request



from flask import Flask, render_template

app = Flask(__name__, template_folder='template')  # still relative to module
# webcode = open('webcode.html').read() - not needed

@app.route('/')
def home():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
