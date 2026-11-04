def mostrarMenu():

    print("--- Menu de Opções ---"
          "\n1 - Consultar Saldo"
          "\n2 - Realizar Depósito"
          "\n3 - Realizar Saque"
          "\n0 - Sair")

def escolherMenu():

    while True:
        escolha = int(input("Escolha uma opção: "))

        if escolha < 0 or escolha > 3:
            print("Valor inválido!")

        if escolha == 0:
            break
        elif escolha == 1:
            saldo = 0.0
        elif escolha == 2:

