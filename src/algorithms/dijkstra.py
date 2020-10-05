
INFINITY = float('inf')

parents = {}
processed = []
weights = {}


def get_best_path(graph, weights, parents):

    v = get_best_child_vertex_not_processed(weights)

    while v is not None:
        current_vertex_weight = weights[v]
        neighbors = graph[v]

        for neighbor in neighbors.keys():
            new_weight = current_vertex_weight + neighbors[neighbor]

            if neighbor not in weights or new_weight < weights[neighbor]:

                weights[neighbor] = new_weight

                parents[neighbor] = v
        
        processed.append(v)
        v = get_best_child_vertex_not_processed(weights)

    return create_best_path_from_parents(parents)


def create_best_path_from_parents(parents):

    best_path = []
    parents_end = parents['END']
    best_path.append('END')

    while parents_end != 'BEGIN':
        best_path.append(parents_end)
        parents_end = parents[parents_end]
    
    best_path.append('BEGIN')

    best_path.reverse()
    
    return best_path
     

def get_best_child_vertex_not_processed(vertex):

    best_weight = INFINITY
    best_vertex = None

    for child in vertex.keys():
        if vertex[child] < best_weight and child not in processed :            
            best_weight = vertex[child]
            best_vertex = child

    return best_vertex


def set_initial_values_and_start(graph):

    vertex_inicial = graph['BEGIN']

    weights = {i: vertex_inicial[i] for i in vertex_inicial.keys()}

    weights['END'] = INFINITY

    parents = {i: 'BEGIN' for i in vertex_inicial.keys()}

    parents['END'] = None

    best_path = get_best_path(graph, weights, parents)

    return best_path


graph = {
    'BEGIN': {
        'A': 6,
        'B': 2,
    },
    'A': {
        'END': 1
    },
    'B': {
        'A': 3,
        'END': 5,
    },
    'END': {}
}
#           [A]
#          / | \
#        6   |   1
#      /     |     \
# [INI]      3       [END]
#      \     |     /
#        2   |   5
#          \ | /
#           [B]


print(set_initial_values_and_start(graph))