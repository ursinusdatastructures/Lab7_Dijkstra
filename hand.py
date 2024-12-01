import matplotlib.pyplot as plt
import numpy as np
from trimesh import load_off, get_edges
from graph import Graph

## Setup Graph
i1 = 1134 # Vertex on tip of thumb
i2 = 4644 # Vertex on tip of index finger
X, _, tris = load_off("hand.off")
edges = get_edges(X, tris)
g = Graph()
for i in range(X.shape[0]):
    g.add_vertex(i)
for i, j in zip(*edges):
    d = X[i, :] - X[j, :]
    d = np.sqrt(np.sum(d**2))
    g.add_edge(i, j, d)

## Run Dijstra's algorithm
dists = g.explore(i1)
dists = np.array([dists[i] for i in range(len(dists))])
path = g.backtrace(i2)

fig = plt.figure(figsize=(16, 8))
## Plot Euclidean results
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
dists_euc = np.sqrt(np.sum((X - X[i1, :][None, :])**2, axis=1))
ax1.scatter(X[:, 0], X[:, 1], X[:, 2], c=dists_euc, cmap='magma_r')
ax1.plot(X[[i1, i2], 0], X[[i1, i2], 1], X[[i1, i2], 2], c='C0', zorder=100)
ax1.view_init(elev=33, azim=-6)
ax1.set_axis_off()
ax1.set_aspect("equal")
ax1.set_title("As The Bird Flies")


## Plot Dijkstra's results
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.scatter(X[:, 0], X[:, 1], X[:, 2], c=dists, cmap='magma_r')
ax2.plot(X[path, 0], X[path, 1], X[path, 2], c='C0', zorder=100)
ax2.view_init(elev=33, azim=-6)
ax2.set_axis_off()
ax2.set_aspect("equal")
ax2.set_title("As The Ant Crawls")
plt.show()