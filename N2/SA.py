import math
import random

destinos = [
    "Origem", 
    "Destino A", 
    "Destino B", 
    "Destino C", 
    "Destino D", 
    "Destino E"
    ]

distancias = {
    ("Origem", "Destino A"): 5,
    ("Origem", "Destino B"): 10,
    ("Origem", "Destino C"): 15,
    ("Origem", "Destino D"): 20,
    ("Origem", "Destino E"): 25,
    ("Destino A", "Destino B"): 13,
    ("Destino A", "Destino C"): 19,
    ("Destino A", "Destino D"): 23,
    ("Destino A", "Destino E"): 26,
    ("Destino B", "Destino C"): 14,
    ("Destino B", "Destino D"): 16,
    ("Destino B", "Destino E"): 19,
    ("Destino C", "Destino D"): 10,
    ("Destino C", "Destino E"): 13,
    ("Destino D", "Destino E"): 7,
    
    
    ("Destino A", "Origem"): 5,
    ("Destino B", "Origem"): 10,
    ("Destino C", "Origem"): 15,
    ("Destino D", "Origem"): 20,
    ("Destino E", "Origem"): 25,
    ("Destino B", "Destino A"): 13,
    ("Destino C", "Destino A"): 19,
    ("Destino D", "Destino A"): 23,
    ("Destino E", "Destino A"): 26,
    ("Destino C", "Destino B"): 14,
    ("Destino D", "Destino B"): 16,
    ("Destino E", "Destino B"): 19,
    ("Destino D", "Destino C"): 10,
    ("Destino E", "Destino C"): 13,
    ("Destino E", "Destino D"): 7
}

temperaturaInicial = 100.0
taxaResfriamento = 0.95
interacoesResfriamento = 100

def calcularCustoRota (rota):
    custo_total = 0
    
    for i in range(len(rota) - 1):
        origem, destino = rota[i], rota[i + 1]
        custo_total += distancias[(origem, destino)]

    return custo_total

def simulatedAnnealing (destinos):
    solucaoAtual = destinos[:]
    melhorSolucao = destinos[:]
    temperatura = temperaturaInicial

    while temperatura > 1.0:
        
        for _ in range(interacoesResfriamento):
            posicao1, posicao2 = random.sample(range(1, len(destinos) - 1), 2)
            solucaoVizinha = solucaoAtual[:]
            solucaoVizinha[posicao1], solucaoVizinha[posicao2] = solucaoVizinha[posicao2], solucaoVizinha[posicao1]
            
            custoAtual = calcularCustoRota(solucaoAtual)
            custoVizinho = calcularCustoRota(solucaoVizinha)

            preCusto = custoVizinho - custoAtual

            if preCusto < 0 or random.random() < math.exp(-preCusto / temperatura):
                solucaoAtual = solucaoVizinha

                if custoAtual < calcularCustoRota(melhorSolucao):
                    melhorSolucao = solucaoAtual

        temperatura *= taxaResfriamento

    return melhorSolucao, calcularCustoRota(melhorSolucao)

melhorRota, custoMelhorRota = simulatedAnnealing(destinos)
print("Melhor rota:", melhorRota)
print("Custo da melhor rota:", custoMelhorRota)