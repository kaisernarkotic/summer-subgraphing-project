import networkx as nx
import sys
import time

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
        if ((G[snode][cnode]["weight"] + sdist) < cdist) and cnode!="Start" and cnode!=datatable2[snode]:
            datatable[cnode] = G[snode][cnode]["weight"] + sdist
            datatable2[cnode] = snode
    datatable = sortdictvalue(datatable)
    unvisitednodes.remove(snode)

currenttime = time.time()

G = nx.DiGraph()
G.add_edge("Start","B", weight=5)
G.add_edge("Start","C", weight=7)
G.add_edge("B","C", weight=1)
G.add_edge("B","D", weight=5)
G.add_edge("C","D", weight=3)
G.add_edge("D","End", weight=6)
G.add_edge("D","F", weight=1)
G.add_edge("End","F", weight=4)

datatable = { #nodes
    "Start": 0,
    "B": sys.maxsize,
    "C": sys.maxsize,
    "D": sys.maxsize,
    "End": sys.maxsize,
    "F": sys.maxsize
}
datatable2 = { #previous node in shortest path
    "Start": "",
    "B": "",
    "C": "",
    "D": "",
    "End": "",
    "F": ""
}
allnodes = ["Start", "B", "C", "D", "End", "F"] 
unvisitednodes = ["B", "C", "D", "End", "F"]

#initializes dijkstra algorithm
for cnode in G.neighbors("Start"):
    cdist = datatable.get(cnode)
    if G["Start"][cnode]["weight"] < cdist:
        datatable[cnode] = G["Start"][cnode]["weight"]
        datatable2[cnode] = "Start"
datatable = sortdictvalue(datatable)

while unvisitednodes: #dijkstra implementation
    dijkstra(datatable, datatable2, unvisitednodes)

khop = 8
for i in list(datatable.keys()):
    if datatable[i] <= khop:
        print(i + " " + str(datatable[i]))

finishtime = time.time()
print("---%s seconds---" % (finishtime-currenttime))