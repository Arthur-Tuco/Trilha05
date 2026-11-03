def metaPessoal():
    meta = input("Qual a meta que deseja alcançar?: ")
    return meta
pass

def valorMeta():
    valor = float(input("Qual o valor da meta?: "))
    return valor
pass

def salarioMensal():
    salario = float(input("Qual seu salário mensal?: "))
    return salario
pass

def despesasMensais():
    despesas = float(input("Quanto você gasta por mês?: "))
    return despesas
pass

def CalcularFimDoMes(salario, despesas):
    restante = salario - despesas
    fixo = restante * 0.30
    bruto = restante - fixo
    return restante, fixo, bruto
pass

def CalcularTempoMeta(valor, bruto):
    if bruto <= 0:
        return 0
    tempo = valor / bruto
    return tempo
pass

def exibirResultado(meta, valor, restante, fixo, bruto, tempo):
    print(f"Saldo após despesas: R${restante:.2f}")
    print(f"Reserva fixa de 30%: R${fixo:.2f}")
    print(f"Valor disponível para a meta: {bruto:.2f}")

    if tempo == 0:
        print("Com o orçamento atual, não sobra dinheiro para alcançar a meta...")
    else:
        print(f"Para alcançar a meta '{meta}', no valor de R${valor:.2f} serão necessários {tempo:.1f} meses")

def main():
    nomeMeta = metaPessoal()
    custoMeta = valorMeta()
    ganhoMensal = salarioMensal()
    gastosMensais = despesasMensais()

    sobrou, reserva, livre = CalcularFimDoMes(custoMeta, ganhoMensal)

    mesesNecessarios = CalcularTempoMeta(ganhoMensal, gastosMensais)

    exibirResultado(nomeMeta, custoMeta, sobrou, reserva, livre, mesesNecessarios)

if __name__ == "__main__":
    main()
