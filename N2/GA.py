import random

destinos = [
    "Destino A", 
    "Destino B", 
    "Destino C", 
    "Destino D", 
    "Destino E"
]

distancias = {
    ("Destino A", "Destino B"): 10,
    ("Destino A", "Destino C"): 15,
    ("Destino A", "Destino D"): 20,
    ("Destino A", "Destino E"): 25,
    ("Destino B", "Destino C"): 12,
    ("Destino B", "Destino D"): 18,
    ("Destino B", "Destino E"): 22,
    ("Destino C", "Destino D"): 14,
    ("Destino C", "Destino E"): 16,
    ("Destino D", "Destino E"): 10,
}

distanciaDeVoltas = {}

for origem, destino in distancias:
    distanciaDeVoltas[(destino, origem)] = distancias[(origem, destino)]

distancias.update(distanciaDeVoltas)

capacidadeVeiculo = 3

tamanhoPopulacao = 50
taxaMutacao = 0.2
geracoes = 100

def calcularCustoRota (rota):
    custoTotal = 0

    for i in range(len(rota) - 1):
        origem, destino = rota[i], rota[i + 1]
        custoTotal += distancias[(origem, destino)]

    return custoTotal

def gerarRotaAleatoria ():
    rota = destinos.copy()
    random.shuffle(rota)
    
    return rota

def cruzamento (pai1, pai2):
    pontoCorte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:pontoCorte] + [gene for gene in pai2 if gene not in pai1[:pontoCorte]]
    filho2 = pai2[:pontoCorte] + [gene for gene in pai1 if gene not in pai2[:pontoCorte]]

    return filho1, filho2

def mutacao(rota):
    if random.random() < taxaMutacao:
        gene1, gene2 = random.sample(rota, 2)
        indice1, indice2 = rota.index(gene1), rota.index(gene2)
        rota[indice1], rota[indice2] = rota[indice2], rota[indice1]

    return rota

populacao = [gerarRotaAleatoria() for _ in range(tamanhoPopulacao)]

for geracao in range(geracoes):
    populacao.sort(key=calcularCustoRota)
    novaPopulacao = []

    elite = int(0.1 * tamanhoPopulacao)
    novaPopulacao.extend(populacao[:elite])

    for _ in range(tamanhoPopulacao - elite):
        pai1, pai2 = random.choices(populacao[:elite], k=2)
        filho1, filho2 = cruzamento(pai1, pai2)
        filho1 = mutacao(filho1)
        filho2 = mutacao(filho2)
        novaPopulacao.extend([filho1, filho2])

    populacao = novaPopulacao

melhorRota = min(populacao, key=calcularCustoRota)
custoMelhorRota = calcularCustoRota(melhorRota)

print("Melhor rota:", melhorRota)
print("Custo da melhor rota:", custoMelhorRota)