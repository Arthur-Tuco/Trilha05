def quantidadeMeses():
    while True:
        meses = int(input("Quantos meses deseja analisar? "))
        if meses <= 0:
            print("No mínimo 1 mês!")
            continue
        return meses


def valorFaturamento(qntdMeses):
    faturamentos = []
    for i in range(qntdMeses):
        valor = float(input(f"Digite o faturamento do mês {i + 1}: R$ "))
        faturamentos.append(valor)
    return faturamentos

def analisarTendencia(faturamentos):
    if len(faturamentos) == 1:
        return "Constante"

    crescimento = True
    queda = True
    constante = True

    for i in range(1, len(faturamentos)):
        if faturamentos[i] > faturamentos[i -1]:
            queda = False
            constante = False

        elif faturamentos[i] < faturamentos[i -1]:
            crescimento = False
            constante = False

    if constante:
        return "Constante"
    elif crescimento:
        return "Crescimento"
    elif queda:
        return "Queda"
    else:
        return "Sem padrão"

def exibirResultado(resultado):
    print("\n--- Relatório de Faturamento ---")
    print(f"O comportamento do faturamento está: {resultado}")


def main():
    qntd = quantidadeMeses()
    listaFaturamentos = valorFaturamento(qntd)

    padrao = analisarTendencia(listaFaturamentos)

    exibirResultado(padrao)

if __name__ == "__main__":
    main()