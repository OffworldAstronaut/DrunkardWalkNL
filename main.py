from network import Network
import numpy as np
import matplotlib.pyplot as plt

N = 8

adj_matrix = np.array([
    [0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0]
])

alphas = np.linspace(-6, 6, 75)
final_p_vectors = []

for alpha in alphas:
    network = Network(N=N, adj_matrix=adj_matrix, alpha=alpha)
    network.evolve_system(time=5000)
    final_p_vectors.append(network.p_vector.copy())

final_p_vectors = np.array(final_p_vectors)

for node in range(N):
    plt.scatter(alphas, final_p_vectors[:, node], marker='o', label=f'Node {node}', s=10)

plt.xlabel('Alfa')
plt.ylabel('Prob. final (nó)')
plt.ylim(0, 0.5)
plt.title('Caso 1: matriz de transição primitiva')
plt.grid(True)
plt.tight_layout()
plt.savefig("graph.png")