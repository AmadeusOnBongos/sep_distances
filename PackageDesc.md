This repository provides an implementation of separation distances and s/c-metrics
for causal graphs as introduced in the paper ['Separation-based distance metrics for causal graphs'](https://proceedings.mlr.press/v258/wahl25b.html).

You can install it as a package using `pip install sep-distances`. The test suite is not part of the [package on pypi](https://pypi.org/project/sep-distances/), but it is still available on the [official github repo](https://github.com/JonasChoice/sep_distances).

Below is a short description of the important source files and how to use them.

## Usage

- [`from sep_distances.mixed_graph import ...`](https://github.com/JonasChoice/sep_distances/blob/main/codebase/mixed_graph.py)
    - Contains the `LabelledMixedGraph` class: a compact representation for directed, undirected,
        bidirected and semidirected edges. Useful helpers include conversion to/from NetworkX,
        adding/removing edges, methods to compute skeletons and CPDAGs, finding v-structures,
        computing Markov blankets, BayesBall, minimal d-separators and several converters
        (`get_canonical_directed_graph`, `get_acyclification`, etc.). This is the main graph data
        structure used by the metrics.

- [`from sep_distances.metrics import ...`](https://github.com/JonasChoice/sep_distances/blob/main/codebase/metrics.py)
    - Implements the distance/metric functions comparing two graphs. Major groups of functions:
        - SHD (Structural Hamming Distance) for DAGs/CPDAGs/MAGs: `SHD_DAGs`, `SHD_CPDAGs`, `SHD_MAGs`.
        - AID (Adjustment Identification Distances) wrappers using `gadjid` (e.g. `parent_AID_DAGs`).
        - Separation distances (SD) for DAGs, CPDAGs, and mixed graphs: `SD_DAGs`, `SD_CPDAGs`, `SD_mixed_graphs`.
        - s/c-metrics and variants (s-metric, c-metric, sc-metric) for DAGs, CPDAGs, mixed graphs and
            graphs with cycles (`metric_DAGs`, `metric_CPDAGs`, `metric_mixed_graphs`, `metric_directed_cyclic_graphs`).
        - Utilities: `generate_triples` (create separation statements) and several helper wrappers.


## Quick example

Basic usage pattern (import, construct graphs, compute a metric):

```python
from sep_distances import mixed_graph as mg
from sep_distances import metrics as metrics

# create two simple DAGs
G1 = mg.LabelledMixedGraph(nodes={"A", "B", "C"})
G1.add_directed("A", "B")
G1.add_directed("B", "C")

G2 = mg.LabelledMixedGraph(nodes={"A", "B", "C"})
G2.add_directed("A", "B")
G2.add_directed("A", "C")

# Compute SHD (Structural Hamming Distance) between DAGs
shd = metrics.SHD_DAGs(G1, G2, normalized=True)
print("SHD (normalized):", shd)

# Compute separation distance (SD) using parent separation
sd = metrics.SD_DAGs(G1, G2, type='parent', normalized=True)
print("SD (parent, normalized):", sd)

# Compute an sc-metric between DAGs (default uses all orders)
sc = metrics.metric_DAGs(G1, G2, type='sc', normalized=True)
print("sc-metric:", sc)
```

Notes:
- Many metric functions expect the same node set in both graphs. They typically check `graph1.nodes == graph2.nodes`.
- For CPDAGs some functions compute or require a representative DAG of the MEC (see `get_representative_of_MEC`).
- AID functions rely on the external `gadjid` package; install it to use those functions.

## Installation / requirements

- Python 3.10+ is required (see [`setup.py`](https://github.com/JonasChoice/sep_distances/blob/main/setup.py)).
- The project depends on packages listed in [`requirements.txt`](https://github.com/JonasChoice/sep_distances/blob/main/requirements.txt) / [`setup.py`](https://github.com/JonasChoice/sep_distances/blob/main/setup.py). Notable dependencies:
    - `networkx`, `numpy`, `scipy`, `gadjid` (optional but required for AID functions).

## License

This project is released under the GNU General Public License v3 (GPLv3). See [`LICENSE.txt`](https://github.com/JonasChoice/sep_distances/blob/main/LICENSE.txt) for the full text.

## Contact & attribution

Original research and initial code: Jonas Wahl & Jakob Runge.

Package implementation and maintenance: Muhammad Haris Owais Ahmed.

If you have questions, bug reports, or performance suggestions, please open an issue or contact the maintainers listed in [`setup.py`](https://github.com/JonasChoice/sep_distances/blob/main/setup.py).