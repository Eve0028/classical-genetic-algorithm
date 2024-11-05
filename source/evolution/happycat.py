import numpy as np


class ShiftedRotatedHappyCat:
    def __init__(self, n_dimensions, F_star=1300, a=5, b=100):
        self.n_dimensions = n_dimensions
        self.F_star = F_star
        self.a = a
        self.b = b
        self.o = np.random.uniform(-32, 32, n_dimensions)
        theta = np.pi / 4  # 45-degree rotation (can be adjusted)
        self.M = self.create_rotation_matrix(n_dimensions, theta)

    def create_rotation_matrix(self, n, theta):
        # Creates a rotation matrix with theta angle in n-dimensions
        if n == 2:
            return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        else:
            M = np.eye(n)
            cos_theta = np.cos(theta)
            sin_theta = np.sin(theta)
            for i in range(n - 1):
                for j in range(i + 1, n):
                    M[i, i] = cos_theta
                    M[i, j] = -sin_theta
                    M[j, i] = sin_theta
                    M[j, j] = cos_theta
            return M

    def happy_cat_function(self, x):
        alpha = 1 / 8
        norm_x = np.linalg.norm(x)
        return ((norm_x ** 2 - len(x)) ** 2) ** alpha + (0.5 * (norm_x ** 2 + np.sum(x))) / len(x) + 0.5

    def __call__(self, x):
        # Apply shift
        shifted_x = np.array(x) - self.o
        # Apply rotation
        rotated_x = np.dot(self.M, shifted_x)
        # Scale the result
        scaled_x = (self.a * rotated_x) / self.b
        # Evaluate the HappyCat function
        return self.happy_cat_function(scaled_x) + self.F_star
