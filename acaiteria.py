def lerQuantidade():
    qntd_p = int(input("Quantos açaís pequenos você quer?: "))
    qntd_m = int(input("Quantos açaís médios você quer?: "))
    qntd_g = int(input("Quantos açaís grandes você quer?: "))

    return qntd_p, qntd_m, qntd_g
pass

def lerDesconto():
    cupom = float(input("Possui cupom de desconto(%)?: "))
    desconto = cupom / 100
    return desconto
pass

def calcularTotal(qntd_p, qntd_m, qntd_g, desconto):
    acai_p = qntd_p * 13.50
    acai_m = qntd_m * 15.00
    acai_g = qntd_g * 17.50
    total = (acai_p + acai_m + acai_g) * (1 - desconto)
    return total
pass

def exibirResultado(total):
    print(f"O valor total a ser pago é de: R$ {total:.2f}")
    pass

def main():
    qntd_p, qntd_m, qntd_g = lerQuantidade()
    desconto = lerDesconto()

    total = calcularTotal(qntd_p, qntd_m, qntd_g, desconto)

    exibirResultado(total)

pass

if __name__ == "__main__":
    main()