import numpy as np 

class Network:
    def __init__(self, N: int, adj_matrix: np.array, alpha: float):
        self.N = N  # quantity of nodes 
        self.adj_matrix = adj_matrix    # adjacency matrix
        self.trans_matrix = np.zeros((N, N)) # transition matrix
        self.p_vector = np.array([1.0 / N for _ in range(N)]) # p vector of probabilities
        self.alpha = alpha
        
    def update_trans_matrix(self) -> np.array:
        exp_p = np.exp(self.alpha * self.p_vector)
        numerator = self.adj_matrix * exp_p[:, None]
        denominator = np.sum(numerator, axis=0, keepdims=True)
        
        self.trans_matrix = numerator / denominator
        return self.trans_matrix
        
    def update_p_vector(self) -> np.array:
        self.p_vector = np.dot(self.trans_matrix, self.p_vector)
        return self.p_vector
        
    def evolve_system(self, time: int=100) -> None:
        p_vectors = []
        
        for _ in range(time):
            self.update_trans_matrix()
            p_vectors.append(self.update_p_vector())
            
        p_vectors = np.array(p_vectors)
        np.savetxt(f"pvec_evolution_alpha={self.alpha}_N={self.N}.dat", p_vectors)