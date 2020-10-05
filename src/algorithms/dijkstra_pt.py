
INFINITO = float('inf')

pais = {}
processados = []
custos = {}


def pegar_caminho_mais_barato(grafo, custos, pais):

    v = pegar_vertice_filho_mais_barato_nao_processado(custos)

    while v is not None:
        custo_vertice_atual = custos[v]
        vizinhos = grafo[v]

        for vizinho in vizinhos.keys():
            novo_custo = custo_vertice_atual + vizinhos[vizinho]

            if vizinho not in custos or novo_custo < custos[vizinho]:

                custos[vizinho] = novo_custo

                pais[vizinho] = v
        
        processados.append(v)
        v = pegar_vertice_filho_mais_barato_nao_processado(custos)

    return gerar_caminho_pela_lista_de_pais(pais)


def gerar_caminho_pela_lista_de_pais(pais):

    lista = []
    pai_do_fim = pais['FIM']
    lista.append('FIM')

    while pai_do_fim != 'INICIO':
        lista.append(pai_do_fim)
        pai_do_fim = pais[pai_do_fim]
    
    lista.append('INICIO')

    lista.reverse()
    
    return lista
     

def pegar_vertice_filho_mais_barato_nao_processado(vertice):

    menor_custo = INFINITO
    vertice_mais_barato = None

    for filho in vertice.keys():
        if vertice[filho] < menor_custo and filho not in processados :            
            menor_custo = vertice[filho]
            vertice_mais_barato = filho

    return vertice_mais_barato


def preparar_variaveis_e_iniciar(grafo):

    vertice_inicial = grafo['INICIO']

    custos = {i: vertice_inicial[i] for i in vertice_inicial.keys()}

    custos['FIM'] = INFINITO

    pais = {i: 'INICIO' for i in vertice_inicial.keys()}

    pais['FIM'] = None

    lista = pegar_caminho_mais_barato(grafo, custos, pais)


grafo = {
    'INICIO': {
        'A': 6,
        'B': 2,
    },
    'A': {
        'FIM': 1
    },
    'B': {
        'A': 3,
        'FIM': 5,
    },
    'FIM': {}
}
#           [A]
#          / | \
#        6   |   1
#      /     |     \
# [INI]      3       [FIM]
#      \     |     /
#        2   |   5
#          \ | /
#           [B]


grafo_7_1_a = {
    'INICIO': {
        'A': 5,
        'B': 2,
    },
    'A': {
        'C': 4,
        'D': 2,
    },
    'B': {
        'A': 8,
        'D': 7,
    },
    'C': {
        'D': 6,
        'FIM': 3,
    },
    'D': {
        'FIM': 1
    },
    'FIM': {}
}


grafo_7_1_b = {
    'INICIO': {
        'A': 10,
    },
    'A': {
        'C': 20,
    },
    'B': {
        'A': 1,
    },
    'C': {
        'B': 1,
        'FIM': 30,
    },
    'FIM': {}
}

grafo_7_1_c = {
    'INICIO': {
        'A': 2,
        'B': 2
    },
    'A': {
        'B': 2,
    },
    'B': {
        'C': 2,
        'FIM': 2,
    },
    'C': {
        'FIM': 2,
        'A': -1,
    },
    'FIM': {}
}


preparar_variaveis_e_iniciar(grafo_7_1_c)