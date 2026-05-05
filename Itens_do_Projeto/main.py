from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Meu primeiro site Flask</h1>
    <p>Rodando no navegador!</p>
    '''

app.run(debug=True)