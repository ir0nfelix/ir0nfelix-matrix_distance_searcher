import numpy as np


class RachkovskySearcher:
    def __init__(self, initial_matrix):
        self.origin_d_matrix = initial_matrix

    def _generate_r_matrix(self, input_matrix: np.ndarray) -> np.ndarray:
        r_matrix_obj = np.vectorize(lambda d: 1 if d else 0)
        r_matrix = r_matrix_obj(input_matrix)
        np.fill_diagonal(r_matrix, 1)

        return r_matrix

    def _generate_d_matrix(self, input_matrix: np.ndarray) -> np.ndarray:
        r_matrix = self._generate_r_matrix(input_matrix)
        index_pairs = [
            (i, j) for i in range(0, input_matrix.shape[0]) for j in range(0, input_matrix.shape[1]) if i < j
        ]

        new_matrix = np.empty_like(input_matrix)
        for pair in index_pairs:
            i, j = pair
            sum_list = [
                r_matrix[j, row] * input_matrix[i, row] + r_matrix[i, row] * input_matrix[j, row]
                for row in range(0, input_matrix.shape[1])
            ]
            new_matrix[i, j] = new_matrix[j, i] = 0 if set(sum_list) == set([0]) else min(sum_list)
            np.fill_diagonal(new_matrix, 0)

        return new_matrix
