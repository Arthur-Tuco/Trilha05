def mostrarMenu():
    print("--- Menu de Opções ---"
          "\n1 - Consultar Saldo"
          "\n2 - Realizar Depósito"
          "\n3 - Realizar Saque"
          "\n0 - Sair")


def escolherMenu():
    while True:
        escolha = input("Escolha uma opção: ")

        if escolha not in ["0", "1", "2", "3"]:
            print("Valor inválido!")
            continue

        return escolha


def consultarSaldo(saldo):
    print(f"Seu saldo é de: R${saldo:.2f}")
    return saldo


def realizarDeposito(saldo):
    valor = float(input("Valor do deposito: "))

    if valor <= 0:
        print("Valor inválido!")
        return saldo

    saldo += valor
    return saldo


def realizarSaque(saldo):
    valor = float(input("Valor do saque: "))

    if valor > saldo:
        print("Saldo insuficiente!")
        return saldo

    if valor <= 0:
        print("Valor inválido!")
        return saldo

    saldo -= valor
    return saldo


def acabarProcesso(escolha):
    print("Saindo!")


def main():
    saldo = 0.0

    while True:
        mostrarMenu()

        escolhaUsuario = escolherMenu()

        if escolhaUsuario == "1":
            saldo = consultarSaldo(saldo)

        elif escolhaUsuario == "2":
            saldo = realizarDeposito(saldo)

        elif escolhaUsuario == "3":
            saldo = realizarSaque(saldo)

        elif escolhaUsuario == "0":
            print("Saindo!")
            break

if __name__ == "__main__":
    main()