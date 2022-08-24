from ogb.linkproppred import LinkPropPredDataset
from graph_tool.all import *
import time as time

f = open("gtdijkstra1.txt", "w")

trialtimes = 0

for trials in range(0,5):
  
  current_time = time.time()
  
  G = Graph(directed=False)

  dataset = LinkPropPredDataset(name = "ogbl-ppa")

  graph = dataset[0]

  total_edges = int(graph.get("edge_index").size / 2)
  for i in range(0, total_edges):
      node1 = graph.get("edge_index")[0][i]
      node2 = graph.get("edge_index")[1][i]
      G.add_edge_list([[node1, node2]])

  totalnodes = graph.get("num_nodes")
  khop = 1
  subgraphnodes = 0

  for i in range(0, totalnodes):
      shortestpaths = graph_tool.topology.shortest_distance(G, source=i)
      shortestpaths = shortestpaths.a
      for j in range(0, totalnodes):
          if shortestpaths[j] <= khop:
              subgraphnodes+=1
      #f.write("start node: " + str(i) + " number of nodes in subgraph: " + str(subgraphnodes) + "\n")
      subgraphnodes = 0

  final_time = time.time()
  trial_time = final_time-current_time
  f.write("trial " + str(trials) + ":%s seconds" % (trial_time) + "\n")

  trialtimes+=trial_time

f.write(str(trialtimes/5))
f.close()
