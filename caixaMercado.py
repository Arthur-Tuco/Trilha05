def valorCompras():
    compras = []

    while True:
        valor = float(input("Qual o valor da compra? "))

        if valor == 0:
            break

        if valor < 0:
            print("Valor inválido")
            continue

        compras.append(valor)

    return compras

def calcularTotal(compras):

    total = sum(compras)

    return total

def pegarParcelas():

    while True:
        parcelas = int(input("Quantas vezes deseja parcelar? "))

        if parcelas >= 0:
            return parcelas

        print("Valor inválido")

def calcularParcelas(total, parcelas):

    if parcelas == 0 or parcelas == 1:
        return None
    else:
        valorParcela = total / parcelas

    return valorParcela

def mostrarResultado(total, parcelas, valorParcela):

    if valorParcela is None:
        print(f"Pagamento à vista: R${total:.2f}")
    else:
        print(f"Total da compra: R${total:.2f}")
        print(f"Parcelado em {parcelas} vezes de R${valorParcela:.2f}")

def main():

    valor = valorCompras()

    totalCompras = calcularTotal(valor)

    qntdParcelas = pegarParcelas()

    totalParcelas = calcularParcelas(totalCompras, qntdParcelas)

    mostrarResultado(totalCompras, qntdParcelas, totalParcelas)

if __name__ == "__main__":
    main()