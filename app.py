from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Usuário admin hardcoded
admin_username = "admin"
admin_password = "admin"

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para lidar com o login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Verificar se as credenciais correspondem ao usuário admin
    if username == admin_username and password == admin_password:
        # Redirecionar para a página de boas-vindas
        return redirect(url_for('welcome'))
    else:
        return "Invalid username or password"

# Página de boas-vindas após o login bem-sucedido
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)
