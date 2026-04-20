from flask import Flask, render_template, request, redirect
from app import adicionar_gasto, listar_gastos, criar_tabela
from analise import gasto_por_categoria
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
criar_tabela()

@app.route("/")
def index():
    gastos = listar_gastos()
    return render_template("index.html", gastos=gastos)

@app.route("/add", methods=["POST"])
def add():
    desc = request.form["descricao"]
    valor = float(request.form["valor"])
    cat = request.form["categoria"]

    adicionar_gasto(desc, valor, cat)
    return redirect("/")

@app.route("/grafico")
def grafico():
    dados = gasto_por_categoria()

    categorias = list(dados.keys())
    valores = list(dados.values())

    if not os.path.exists("static"):
        os.makedirs("static")

    caminho = "static/grafico.png"

    plt.figure()
    plt.bar(categorias, valores)
    plt.title("Gastos por Categoria")
    plt.savefig(caminho)
    plt.close()

    return render_template("grafico.html", imagem=caminho)

if __name__ == "__main__":
    app.run(debug=True)