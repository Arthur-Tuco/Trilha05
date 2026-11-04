def quantidadeIngressos():
    while True:
        inteiras = int(input("Quantos ingressos inteiros?: "))
        meias = int(input("Quantos ingressos de meia entrada?: "))

        if inteiras >= 0 and meias >= 0:
            return inteiras, meias
        else:
            print("Valor negativo!")

def diaSemana():

    while True:
        dia = int(input("Qual o dia da semana? (1-7): "))
        if 1 <= dia <= 7:
            return dia
        else:
            print("Dia inválido!")

def origemFilme():

    while True:
        origem = input("Qual o origem do filme? (Nacional/Internacional): ").capitalize()
        if origem not in ["Nacional", "Internacional", "I", "N"]:
            print("Resposta inválida")
        else:
            return origem

def precoIngressos(inteiras, meias, dia, origem):

    precoInteira = 28.50 * inteiras
    precoMeia = 14.25 * meias

    if dia == 4:
        precoInteira = 14.50 * inteiras
        precoMeia = 14.50 * meias

    if origem == "Nacional":
        precoInteira = 5.00 * inteiras
        precoMeia = 5.00 * meias

    return precoInteira, precoMeia

def mostrarResultado(inteiras, meias, precoInteira, precoMeia):

    print(f"Total de ingressos cheios: {inteiras}."
                       f"\nTotal de meio ingressos: {meias}."
                       f"\nTotal à pagar: {precoInteira + precoMeia:.2f}")

def main():

    ingressoCheio, ingressoMeio = quantidadeIngressos()

    dia = diaSemana()

    local = origemFilme()

    valorInteiro, valorMeia = precoIngressos(ingressoCheio, ingressoMeio, dia, local)

    mostrarResultado(ingressoCheio, ingressoMeio, valorInteiro, valorMeia)

if __name__ == "__main__":
    main()
