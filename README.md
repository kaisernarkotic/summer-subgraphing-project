This is a subgraphing project designed to test the efficiences of the Networkx and Graph-Tool packages.

# Input data:
The input datasets are from https://ogb.stanford.edu/docs/linkprop/#ogbl-ppa. The programs input each node and edge of a default weight 1. The ddi dataset has around 4000 nodes and 3 million edges. The ppa dataset has around half a million nodes and 30 million edges. The subgraphing programs could be tested against the ppa dataset, but the run times were impractically large.

# Algorithm:
To subgraph, there must be a start node and a data structure that contains the shortest path from the start node to every other node in the graph. The built-in shortest path APIs in the packages were used to determine the shortest paths. Every node in the dataset ddi was used as a start node for each trial. Changing the number of hops limits the size of the subgraph, and the total depth of the ddi dataset graph was 5. 

# Results:
The results of numerous trials can be accessed through this link: https://docs.google.com/spreadsheets/d/1kxnQmdiIQ_n4dIblkwokuyO2BknXrOGe4PF0q4laA2A/edit?usp=sharing