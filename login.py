from flask import Flask, request, render_template_string

app = Flask(__name__)

# Rota para exibir o formulário
@app.route('/')
def formulario():
    with open("formulario.html", "r", encoding="utf-8") as file:
        return file.read()

# Rota para processar o formulário
@app.route('/registrar', methods=['POST'])
def registrar():
    nome = request.form['nome']
    return f"<h1>Você foi registrado com sucesso, {nome}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)