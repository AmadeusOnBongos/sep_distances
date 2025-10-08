from codebase import mixed_graph as mg
from codebase import metrics as metrics
import tests.Graphs_for_testing as G_testing

# create two simple DAGs
G1 = mg.LabelledMixedGraph(nodes={"A", "B", "C"})
G1.add_directed("A", "B")
G1.add_directed("B", "C")

G2 = mg.LabelledMixedGraph(nodes={"A", "B", "C"})
G2.add_directed("A", "B")
G2.add_directed("A", "C")

# or use one of our example graphs
# test_graphs = G_testing.generate_graphs()
# G3 = test_graphs['simple_collider']
# G4 = test_graphs['chain']
# G5 = test_graphs['empty']

# Compute SHD (Structural Hamming Distance) between DAGs
shd = metrics.SHD_DAGs(G1, G2, normalized=True)
print("SHD (normalized):", shd)

# Compute separation distance (SD) using parent separation
sd = metrics.SD_DAGs(G1, G2, type='parent', normalized=True)
print("SD (parent, normalized):", sd)

# Compute an sc-metric between DAGs (default uses all orders)
sc = metrics.metric_DAGs(G1, G2, type='sc', normalized=True)
print("sc-metric:", sc)