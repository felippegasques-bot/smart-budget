from app import listar_gastos

def gasto_por_categoria():
    gastos = listar_gastos()
    categorias = {}

    for g in gastos:
        categoria = g[3]
        valor = g[2]

        if categoria in categorias:
            categorias[categoria] += valor
        else:
            categorias[categoria] = valor

    return categorias
