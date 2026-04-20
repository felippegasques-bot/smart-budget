from app import criar_tabela, adicionar_gasto, listar_gastos
from analise import total_gasto, gasto_por_categoria, gerar_alertas, grafico_categorias

criar_tabela()

while True:
    print("\n=== SISTEMA DE GASTOS ===")
    print("1 - Adicionar gasto")
    print("2 - Ver gastos")
    print("3 - Ver resumo")
    print("4 - Ver gráfico")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        desc = input("Descrição: ")
        valor = float(input("Valor: "))
        cat = input("Categoria: ")

        adicionar_gasto(desc, valor, cat)
        print("Gasto adicionado!")

    elif opcao == "2":
        for g in listar_gastos():
            print(f"ID:{g[0]} | {g[1]} | R${g[2]} | {g[3]} | {g[4]}")

    elif opcao == "3":
        print("\n💰 Total gasto:", total_gasto())
        print("📊 Por categoria:", gasto_por_categoria())

        alertas = gerar_alertas()
        if alertas:
            print("\n🚨 ALERTAS:")
            for a in alertas:
                print(a)
        else:
            print("\n✅ Tudo sob controle!")

    elif opcao == "4":
        grafico_categorias()

    elif opcao == "5":
        break

    else:
        print("Opção inválida")