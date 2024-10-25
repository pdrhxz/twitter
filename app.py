# importando a biblioteca do Flask para fazer um site
from flask import Flask, render_template, request

app=Flask(__name__)
usuarios= [
    'admin' : 'admin';
    'usuario' : 'senha';
    'pedro' : '1234';
    
]


@app.route('/') #rota para a pagina inicial
def home():
    return render_template('index.html')

@app.route('/login')  #rota para a pagina de login 
def login(): 
    return render_template('login.html')


        
@app.route('/cadastro') #rota para criar conta
def cadastro():
    return render_template('cadastro.html')

#parte principal do programa 
if __name__ =='__main__':
    app.run(debug=True)

