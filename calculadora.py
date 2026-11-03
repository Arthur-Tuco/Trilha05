def primeiroNumero():
    n1 = float(input("Digite o primeiro numero: "))
    return n1

def segundoNumero():
    n2 = float(input("Digite o segundo numero: "))
    return n2

def selecionarOperacao():
    operacao = input("Escolha uma operação (+, -, *, /, %, ^): ").lower().strip()

    if operacao in ["+", "adição", "adicao"]:
        return "+"
    elif operacao in ["-", "subtração", "subtracao"]:
        return "-"
    elif operacao in ["*", "multiplicação", "multiplicacao"]:
        return "*"
    elif operacao in ["/", "divisão", "divisao"]:
        return "/"
    elif operacao in ["%", "resto"]:
        return "%"
    elif operacao in ["^", "potência", "potencia"]:
        return "^"
    else:
        print("Operação não suportada!")
        return None

def realizarConta(n1, n2, operacao):
    if operacao is None:
        return None

    if operacao == "+":
        resultado = n1 + n2

    elif operacao == "-":
        resultado = n1 - n2

    elif operacao == "*":
        resultado = n1 * n2

    elif operacao == "/":
        if n2 == 0:
            print("Não é possível dividir por zero!")
            return None
        resultado = n1 / n2

    elif operacao == "%":
        resultado = n1 % n2

    elif operacao == "^":
        resultado = n1 ** n2

    return resultado

def exibirResultado(resultado):
    if resultado is not None:
        print(f"O resultado da operação é: {resultado}")

def main():
    numero1 = primeiroNumero()
    numero2 = segundoNumero()
    sinal = selecionarOperacao()

    fim = realizarConta(numero1, numero2, sinal)

    exibirResultado(fim)

if __name__ == "__main__":
    main()