import networkx as nx
import sys

def bellman_ford(datatable, datatable2):
    for i in range(G.number_of_nodes()):
        for j in range(G.number_of_nodes()):
            snode = list(datatable.keys())[j]
            sdist = datatable[snode]
            for cnode in G.neighbors(snode):
                cdist = datatable[cnode]
                if sdist + G[snode][cnode]["weight"] < cdist:
                    datatable[cnode] = sdist + G[snode][cnode]["weight"]
                    datatable2[cnode] = snode

G = nx.DiGraph()
G.add_edge("A", "B", weight = 5)
G.add_edge("B", "C", weight = 20)
G.add_edge("B", "G", weight = 60)
G.add_edge("B", "F", weight = 30)
G.add_edge("C", "D", weight = 10)
G.add_edge("D", "C", weight = -15)
G.add_edge("C", "E", weight = 75)
G.add_edge("F", "E", weight = 25)
G.add_edge("F", "G", weight = 5)
G.add_edge("G", "H", weight = -50)
G.add_edge("H", "I", weight = -10)
G.add_edge("F", "I", weight = 50)
G.add_edge("E", "J", weight = 100)

datatable = { #node distance from start
    "A": 0,
    "B": sys.maxsize,
    "C": sys.maxsize,
    "D": sys.maxsize,
    "E": sys.maxsize,
    "F": sys.maxsize,
    "G": sys.maxsize,
    "H": sys.maxsize,
    "I": sys.maxsize,
    "J": sys.maxsize
}
datatable2 = { #previous node in shortest path
    "A": "",
    "B": "",
    "C": "",
    "D": "",
    "E": "",
    "F": "",
    "G": "",
    "H": "",
    "I": "",
    "J": ""
}

bellman_ford(datatable, datatable2)

for i in range(G.number_of_nodes()): #testing for negative weights
    for j in range(G.number_of_nodes()):
        snode = list(datatable.keys())[j]
        sdist = datatable[snode]
        for cnode in G.neighbors(snode):
            cdist = datatable[cnode]
            if sdist + G[snode][cnode]["weight"] < cdist:
                datatable[cnode] = -sys.maxsize 

khop = 8
for i in list(datatable.keys()):
    if datatable[i] <= khop:
        print(i + " " + str(datatable[i]))

print(datatable)
print(datatable2)