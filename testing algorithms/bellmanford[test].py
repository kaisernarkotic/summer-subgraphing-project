from ogb.linkproppred import LinkPropPredDataset
import networkx as nx
import sys
import time as time

def sortdictvalue(dictionary):
    curdict = sorted(dictionary.items(), key=lambda x: x[1]) 
    retdict = {}
    for x in range(len(curdict)):
        key = curdict[x][0]
        value = curdict[x][1]
        retdict[key] = value
    return retdict

current_time = time.time()

G = nx.Graph()

dataset = LinkPropPredDataset(name = "ogbl-ddi")

graph = dataset[0]

datatable = {} # stores nodes as keys and their shortest path to the start node as values
#datatable2 = {} # stores nodes as keys and the previous node that led to them from the start node
datatable3 = {} # stores nodes as keys and the time it took to run the subgraph algorithm starting from such node

#hardcoded testing data
"""
datatable = {
    "4266": 0,
    "4014": sys.maxsize,
    "3953": sys.maxsize,
    "3514": sys.maxsize,
    "2813": sys.maxsize,
    "592": sys.maxsize
}
datatable2 = {
    "4266": "",
    "4014": "",
    "3953": "",
    "3514": "",
    "2813": "",
    "592": ""
}

G.add_edge("4266", "4014", weight = 1)
G.add_edge("4266", "3953", weight = 1)
G.add_edge("4266", "3514", weight = 1)
G.add_edge("3514", "3953", weight = 1)
G.add_edge("3514", "2813", weight = 1)
G.add_edge("3514", "592", weight = 1)
G.add_edge("2813", "4266", weight = 1)
"""

total_edges = int(graph.get("edge_index").size / 2)
for i in range(0, total_edges):
    node1 = str(graph.get("edge_index")[0][i])
    node2 = str(graph.get("edge_index")[1][i])
    G.add_edge(node1, node2, weight=1)

total_nodes = graph.get("num_nodes") #used to initialize each node, their distance from 'start', and their previous node
for i in range(0,total_nodes):
    #G.add_node(str(i))
    datatable[str(i)] = sys.maxsize
    #datatable2[str(i)] = ""
    #datatable3[str(i)] = 0

total_time = 0

for i in range(0,3):
    datatable[str(i)] = 0
    datatable = sortdictvalue(datatable)
    for j in range(total_nodes):
        snode = list(datatable.keys())[j]
        sdist = datatable[snode]
        for cnode in G.neighbors(snode):
            cdist = datatable[cnode]
            if sdist + G[snode][cnode]["weight"] < cdist:
                datatable[cnode] = sdist + G[snode][cnode]["weight"]
                #datatable2[cnode] = snode
        datatable = sortdictvalue(datatable)
            
    khop = 1
    subgraphnodes = 0
    for k in list(datatable.keys()):
        if datatable[k] <= khop:
            subgraphnodes = subgraphnodes + 1

    final_time = time.time()
    elapsed_time = final_time-current_time
    datatable3[str(i)] = elapsed_time
    total_time+=elapsed_time

    for j in range(0,total_nodes): #resets all the nodes back to infinite distance for another cycle
        datatable[str(j)] = sys.maxsize

avg_time = total_time / 3
print("---%s seconds---" % (avg_time))
print(datatable3)