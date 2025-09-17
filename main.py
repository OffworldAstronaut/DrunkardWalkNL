import numpy as np 

class Network:
    def __init__(self, N: int, adj_matrix: np.array):
        self.N = N  # quantity of nodes 
        self.adj_matrix = adj_matrix    # adjacency matrix
        self.trans_matrix = np.zeros((N, N)) # transition matrix
        self.p_vector = np.array(N) # p vector of probabilities
        
    def update_trans_matrix(self) -> np.array:
        ...
        
    def update_p_vector(self) -> np.array:
        ...
        
    def evolve_system(self) -> None:
        ...