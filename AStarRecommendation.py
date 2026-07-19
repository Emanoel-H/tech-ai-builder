import heapq

class Produto:
    def __init__(self, nome, categoria, conversao_probabilidade):
        self.nome = nome
        self.categoria = categoria
        self.conversao_probabilidade = conversao_probabilidade

    def __repr__(self):
        return f"{self.nome} ({self.categoria})"

class AStarRecommendation:
    def __init__(self, produtos, heuristica):
        self.produtos = produtos
        self.heuristica = heuristica
        self.grafo = self.criar_grafo()

    def criar_grafo(self):
        grafo = {}
        for produto in self.produtos:
            grafo[produto] = [p for p in self.produtos if p != produto]
        return grafo

    def a_star(self, inicio, objetivo):
        fila_prioridade = []
        heapq.heappush(fila_prioridade, (0 + self.heuristica(inicio), 0, inicio))
        visitados = set()
        caminhos = {}

        while fila_prioridade:
            _, g, atual = heapq.heappop(fila_prioridade)

            if atual in visitados:
                continue

            visitados.add(atual)
            if atual == objetivo:
                break

            for vizinho in self.grafo[atual]:
                if vizinho not in visitados:
                    h = self.heuristica(vizinho)
                    heapq.heappush(fila_prioridade, (g + 1 + h, g + 1, vizinho))
                    caminhos[vizinho] = atual

        caminho = []
        produto = objetivo
        while produto in caminhos:
            caminho.insert(0, produto)
            produto = caminhos[produto]
        return caminho

def heuristica(produto):
    return -produto.conversao_probabilidade

produtos = [
    Produto("Produto A", "Categoria 1", 0.9),
    Produto("Produto B", "Categoria 1", 0.8),
    Produto("Produto C", "Categoria 2", 0.7),
    Produto("Produto D", "Categoria 2", 0.6),
]

recomendador = AStarRecommendation(produtos, heuristica)

inicio = produtos[0]
objetivo = produtos[2]

caminho_recomendado = recomendador.a_star(inicio, objetivo)

print("Caminho recomendado:")
for p in caminho_recomendado:
    print(p)