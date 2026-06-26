import networkx as nx

def symmetric_pair_graph(n_pairs=8):
    G = nx.Graph()
    for n in range(1, n_pairs + 1):
        G.add_edge(-n, n, relation="symmetric_pair")
    return G

def pair_positions(n_pairs=8):
    pos = {}
    for idx, n in enumerate(range(1, n_pairs + 1)):
        y = n_pairs - idx
        pos[-n] = (-1, y)
        pos[n] = (1, y)
    return pos

def graph_metrics(G):
    components = list(nx.connected_components(G))
    return {
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "connected_components": nx.number_connected_components(G),
        "largest_component": max((len(c) for c in components), default=0),
    }
