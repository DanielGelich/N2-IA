import heapq

mapa = {
    "A": {"B": 10, "C": 15},
    "B": {"A": 10, "C": 12, "D": 18, "E": 22},
    "C": {"A": 15, "B": 12, "D": 14, "E": 16},
    "D": {"B": 18, "C": 14, "E": 10},
    "E": {"B": 22, "C": 16, "D": 10}
}

def heuristica (nodo, destino):
    return 0

def percurso (mapa, inicio, destino):
    filaPrioridade = [(0, inicio)]
    custo_c = {inicio: 0}
    caminho = {}

    while filaPrioridade:
        custoAtual, localAtual = heapq.heappop(filaPrioridade)

        if localAtual == destino:
            caminhoCompleto = [localAtual]

            while localAtual in caminho:
                localAtual = caminho[localAtual]
                caminhoCompleto.append(localAtual)

            return caminhoCompleto[::-1]

        for vizinho, custo in mapa[localAtual].items():
            novoCusto = custo_c[localAtual] + custo

            if vizinho not in custo_c or novoCusto < custo_c[vizinho]:
                custo_c[vizinho] = novoCusto
                prioridade = novoCusto + heuristica(vizinho, destino)
                heapq.heappush(filaPrioridade, (prioridade, vizinho))
                caminho[vizinho] = localAtual

    return None


melhorRota = percurso(mapa, "A", "E")

if melhorRota:
    print("Melhor rota:", melhorRota)
else:
    print("Não foi possível calcular a rota.")