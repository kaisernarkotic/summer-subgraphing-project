from ogb.linkproppred import LinkPropPredDataset
import networkx as nx
import time as time

f = open("nxbellmanford5.txt", "w")

def subgraph(subgraphnodes, khop):
    shortestpaths = nx.shortest_path_length(G, source=i, method='bellman-ford')
    for j in list(shortestpaths.keys()):
        if shortestpaths[j] <= khop:
            subgraphnodes+=1
    subgraphnodes = 0

trialtimes = 0

for trials in range(0,5):

  current_time = time.time()

  G = nx.Graph()

  dataset = LinkPropPredDataset(name = "ogbl-ddi")

  graph = dataset[0]

  total_edges = int(graph.get("edge_index").size / 2)
  for i in range(0, total_edges):
      node1 = graph.get("edge_index")[0][i]
      node2 = graph.get("edge_index")[1][i]
      G.add_edge(node1, node2, weight=1)

  totalnodes = graph.get("num_nodes")
  khop = 5
  subgraphnodes = 0

  for i in range(0, totalnodes):
    subgraph(subgraphnodes, khop)

  final_time = time.time()
  trial_time = final_time-current_time
  f.write("trial " + str(trials) + ":%s seconds" % (trial_time) + "\n")
  trialtimes+=trial_time

f.write(str(trialtimes/5) + "\n")
f.close()