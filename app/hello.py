from flask import Flask, request



from flask import Flask, render_template

app = Flask('hello')
# webcode = open('webcode.html').read() - not needed

@app.route('/')
def webprint():
    return render_template('result.html') 

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
