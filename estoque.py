def mostrarMenu():
    print("--- Menu de Opções ---")
    print("1 - Adicionar produto"
          "\n2 - Realizar entrada de estoque"
          "\n3 - Realizar saída de estoque"
          "\n4 - Listar estoque"
          "\n0 - Sair")


def escolherMenu():
    while True:
        escolha = input("Escolha uma opção: ")

        if escolha not in ["0", "1", "2", "3", "4"]:
            print("Valor inválido!")
            continue

        return escolha


def adicionarProduto(nomes, quantidades):
    if len(nomes) >= 1000:
        print("Erro: Limite de 1000 produtos atingido!")
        return

    produto = input("Digite o produto que deseja adicionar: ")

    nomes.append(produto)

    quantidades.append(0)

    print("Produto cadastrado com sucesso!")


def entradaEstoque(nomes, quantidades):
    if len(nomes) == 0:
        print("Nenhum produto cadastrado!")
        return

    numero = int(input("Digite número do produto: "))

    if numero < 0 or numero >= len(nomes):
        print("Produto não encontrado!")
        return

    valor = int(input(f"Quantidade para adicionar ao produto '{nomes[numero]}': "))

    if valor <= 0:
        print("A quantidade deve ser maior que zero!")
        return

    quantidades[numero] += valor
    print(f"Entrada registrada! Novo estoque de {nomes[numero]}: {quantidades[numero]}!")


def saidaEstoque(nomes, quantidades):
    if len(nomes) == 0:
        print("Nenhum produto cadastrado!")
        return

    numero = int(input("Digite o número do produto: "))

    if numero < 0 or numero >= len(nomes):
        print("Produto não encontrado!")
        return

    valor = int(input(f"Quantidade para retirar do produto '{nomes[numero]}': "))

    if valor <= 0:
        print("A quantidade deve ser maior que zero!")
        return

    if valor > quantidades[numero]:
        print("Erro: saldo insuficiente no estoque!")
        return

    quantidades[numero] -= valor
    print(f"Saída registrada! Novo estoque de {nomes[numero]}: {quantidades[numero]}")


def listarEstoque(nomes, quantidades):
    if len(nomes) == 0:
        print("Nenhum produto cadastrado!")
        return

    print("\n--- Produtos em estoque ---")

    for i in range(len(nomes)):
        print(f"Produto {i} - {nomes[i]} | Quantidade: {quantidades[i]}")


def main():
    listaNomes = []
    listaQuantidades = []

    while True:
        mostrarMenu()
        escolhaUsuario = escolherMenu()

        if escolhaUsuario == "1":
            adicionarProduto(listaNomes, listaQuantidades)

        elif escolhaUsuario == "2":
            entradaEstoque(listaNomes, listaQuantidades)

        elif escolhaUsuario == "3":
            saidaEstoque(listaNomes, listaQuantidades)

        elif escolhaUsuario == "4":
            listarEstoque(listaNomes, listaQuantidades)

        elif escolhaUsuario == "0":
            print("Saindo!")
            break


if __name__ == "__main__":
    main()
