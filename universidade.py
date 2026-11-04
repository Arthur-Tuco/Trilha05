def siglaCurso():

    siglasValidas = ["SI", "ADS", "CS", "EC", "ES"]

    print(
        "As siglas dos cursos são:\n"
        "SI - Sistemas de Informação\n"
        "ADS - Análise e Desenvolvimento de Sistemas\n"
        "CS - Ciências da Computação\n"
        "EC - Engenharia da Computação\n"
        "ES - Engenharia de Software"
        )
    while True:
            curso = input("Qual seu curso? ").strip().upper()
            if curso not in siglasValidas:
                print("Curso não encontrado!")
            else:
                return curso

def valorCurso(curso):

    preco = 0.0

    if curso == "SI":
        preco = 900.00
    elif curso == "ADS":
        preco = 750.00
    elif curso == "CS":
        preco = 1150.00
    elif curso == "EC":
        preco = 1300.00
    elif curso == "ES":
        preco = 950.00

    return preco

def isencaoMensalidade(preco):

    while True:
        respostas = ["sim", "s", "nao", "não", "n"]
        respostasPositivas = ["sim", "s"]

        isento = input("Você está isento da mensalidade? (S/N): ").strip().lower()
        if isento not in respostas:
            print("Resposta inválida!")
            continue

        if isento in respostasPositivas:
            preco = 0.0

        return preco, isento

def descontoMensalidade(isento, preco):

    if isento in ["s", "sim"] or preco == 0.0:
        return preco

    while True:
        desconto = int(input("Você possui desconto? (%) (0 para não)"))

        if desconto < 0 or desconto > 100:
            print("Resposta inválida")
        else:
            return desconto

def calcularMensalidade(preco, desconto):

    if preco == 0.0:
        return 0.0

    precoFinal = preco - (preco * (desconto / 100))

    return precoFinal

def mostrarResultado(curso, preco, isento):

    if isento in ["s", "sim"]:
        print("Aluno isento")
    else:
        print(f"O valor da mensalidade do {curso} é de R${preco:.2f}")

    return preco, isento

def main():

    sigla = siglaCurso()

    valor = valorCurso(sigla)

    valor, isento = isencaoMensalidade(valor)

    desconto = descontoMensalidade(isento, valor)

    valorFinal = calcularMensalidade(valor, desconto)

    mostrarResultado(sigla, valorFinal, isento)

if __name__ == "__main__":
    main()