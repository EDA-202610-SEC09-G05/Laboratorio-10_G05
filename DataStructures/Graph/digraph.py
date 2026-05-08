from DataStructures.Map import map_linear_probing as map

def new_graph(order):
    """
    Crea un grafo dirigido vacio con un mapa de vertices de tamaño inicial 'order'.
    """
    return {
        'vertices': map.new_map(order), 
        'num_edges': 0                  }

def insert_vertex(my_graph, key_u, info_u):
    """
    Agrega un nuevo vertice o reemplaza la informacion si ya existe.
    """
    if map.contains(my_graph['vertices'], key_u):
        vertex = map.get(my_graph['vertices'], key_u)
        vertex['value'] = info_u
    else:
        new_v = {
            'key': key_u,
            'value': info_u,
            'adjacents': map.new_map(2) 
        }
        map.put(my_graph['vertices'], key_u, new_v)
    return my_graph

def add_edge(my_graph, key_u, key_v, weight=1.0):
    """
    Agrega un arco dirigido de key_u a key_v.
    """
    if not map.contains(my_graph['vertices'], key_u):
        raise Exception("El vertice u no existe") 
    if not map.contains(my_graph['vertices'], key_v):
        raise Exception("El vertice v no existe")

    u_vertex = map.get(my_graph['vertices'], key_u)
    
    if not map.contains(u_vertex['adjacents'], key_v):
        my_graph['num_edges'] += 1

    map.put(u_vertex['adjacents'], key_v, {'to': key_v, 'weight': weight})
    return my_graph

def contains_vertex(my_graph, key_u):
    """
    Retorna True si el vertice esta presente, False en caso contrario.
    """
    return map.contains(my_graph['vertices'], key_u)

def order(my_graph):
    """
    Retorna el numero de vertices del grafo.
    """
    return map.size(my_graph['vertices'])

def size(my_graph):
    """
    Retorna el numero de arcos del grafo.
    """
    return my_graph['num_edges']