import numpy as np  # Numerical methods

# Represents a network (graph) with random walkers
class Network:
    def __init__(self, N: int, adj_matrix: np.ndarray , alpha: float):
        """Initializes a network.

        Args:
            N (int): Number of vertices 
            adj_matrix (np.ndarray): Adjacency matrix
            alpha (float): Nonlinear parameter
        """
        # Stores the graph's characteristics
        self.N = N 
        self.alpha = alpha
        self.adj_matrix = adj_matrix
        # Initializes the transition matrix
        self.trans_matrix = np.zeros((N, N))
        # Initializes the vector of probabilities 
        self.p_vector = np.array([1.0 / N for _ in range(N)])
        
    def update_trans_matrix(self) -> np.ndarray:
        """Updates the transition matrix.

        Returns:
            np.ndarray: Updated transition matrix.
        """
        # Calculates e^(p_i * alpha) for each p_i in the vector of probabilities
        exp_p = np.exp(self.alpha * self.p_vector)
        # Calculates the numerator of each element in the transition_matrix 
        # (the product between the connection in the adjacency matrix and the respective node in exp_p)
        numerator = self.adj_matrix * exp_p[:, None]
        # Calculates the denominator of each element in the transition matrix
        # (sum of every line)
        denominator = np.sum(numerator, axis=0, keepdims=True)
        
        # Calculates the new transition_matrix
        self.trans_matrix = numerator / denominator
        
        # Returns the updated matrix
        return self.trans_matrix
        
    def update_p_vector(self) -> np.ndarray:
        """Updates the vector of probabilities

        Returns:
            np.ndarray: Updated vector of probabilities
        """
        # Multiply both matrices for time evolution
        self.p_vector = np.dot(self.trans_matrix, self.p_vector)
        # Returns the updated p vector
        return self.p_vector
        
    def evolve_system(self, time: int=100) -> None:
        """Iterates the system for the specified amount of time

        Args:
            time (int, optional): Quantity of steps desired. Defaults to 100.
        """
        p_vectors = []
        
        for _ in range(time):
            self.update_trans_matrix()
            p_vectors.append(self.update_p_vector())
            
        p_vectors = np.array(p_vectors[-1])
        #np.savetxt(f"pvec_evolution_alpha={self.alpha}_N={self.N}.dat", p_vectors, fmt="%.4f")