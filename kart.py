def tamanhoPista():
    tamanho = float(input("Digite o tamanho da pista em metros: "))
    return tamanho
pass

def qntdVoltas():
    voltas = int(input("Digite a quantidade de voltas: "))
    return voltas
pass

def primeiraVolta():
    voltaPrimeira = float(input("Digite o tempo da primeira volta em segundos: "))
    return voltaPrimeira
pass

def calcularDistancia(tamanho, voltas):
    total = (tamanho * voltas) / 1000
    return total
pass

def calcularTempo(voltaPrimeira, voltas):
    tempo = (voltaPrimeira * voltas) / 60
    return tempo
pass

def exibirPerformance(total, tempo):
    print(f"Distância total de: {total:.2f} km")
    print(f"Previsão de tempo: {tempo:.2f} minutos")
pass

def main():
    pista = tamanhoPista()
    circuito = qntdVoltas()
    tempo_volta = primeiraVolta()

    distancia = calcularDistancia(pista, circuito)
    tempo_total = calcularTempo(tempo_volta, circuito)

    exibirPerformance(distancia, tempo_total)

if __name__ == "__main__":
    main()