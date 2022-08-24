from ogb.linkproppred import LinkPropPredDataset
import sys
import time
import networkx as nx

def get_current_node(unv,dictionary):
    for key in dictionary.keys():
        if(key in unv):
            return key
def sortdictvalue(dictionary):
    curdict = sorted(dictionary.items(), key=lambda x: x[1]) 
    retdict = {}
    for x in range(len(curdict)):
        key = curdict[x][0]
        value = curdict[x][1]
        retdict[key] = value
    return retdict
def dijkstra(datatable, datatable2, unvisitednodes):
    snode = get_current_node(unvisitednodes, datatable)
    sdist = datatable[snode]
    for cnode in G.neighbors(snode):
        cdist = datatable.get(cnode)
        if ((G[snode][cnode]["weight"] + sdist) < cdist) and cnode!="4266" and cnode!=datatable2[snode]:
            datatable[cnode] = G[snode][cnode]["weight"] + sdist
            datatable2[cnode] = snode
    datatable = sortdictvalue(datatable)
    unvisitednodes.remove(snode)

current_time = time.time()

G = nx.Graph()

dataset = LinkPropPredDataset(name = "ogbl-ddi")

graph = dataset[0]

datatable = {}
datatable2 = {}
allnodes = []
unvisitednodes = []

total_edges = int(graph.get("edge_index").size / 2) #adds nodes to graph with weight of 1
for i in range(0, total_edges):
    node1 = str(graph.get("edge_index")[0][i])
    node2 = str(graph.get("edge_index")[1][i])
    G.add_edge(node1, node2, weight=1)

total_nodes = graph.get("num_nodes") #used to initialize each node, their distance from 'start', and their previous node
for i in range(0,total_nodes):
    datatable[str(i)] = sys.maxsize
    datatable2[str(i)] = ""
    allnodes.append(str(i))
    unvisitednodes.append(str(i))

unvisitednodes.remove("4266")
datatable["4266"] = 0 #uses 4266 as start node

#initializes dijkstra algorithm
for cnode in G.neighbors("4266"):
    cdist = datatable.get(cnode)
    if G["4266"][cnode]["weight"] < cdist:
        datatable[cnode] = G["4266"][cnode]["weight"]
        datatable2[cnode] = "4266"
datatable = sortdictvalue(datatable)

while unvisitednodes:
    dijkstra(datatable, datatable2, unvisitednodes)

khop = 1
subgraphnodes = 0
for i in list(datatable.keys()):
    if datatable[i] <= khop:
        subgraphnodes = subgraphnodes + 1
        print(i + " " + str(datatable[i]))
print(str(subgraphnodes))

final_time = time.time()
print("---%s seconds---" % (final_time-current_time))
