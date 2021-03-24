import numpy as np


class RachkovskySearcher:
    def __call__(self, initial_matrix_path: str):
        return self.get_distance_matrix(initial_matrix_path)

    def get_distance_matrix(self, initial_matrix_path: str) -> np.ndarray:
        origin_d_matrix = np.load(initial_matrix_path)
        return self._get_matrix_compare(origin_d_matrix)

    def _get_matrix_compare(self, current_d_matrix: np.ndarray):
        next_d_matrix = self._generate_d_matrix(current_d_matrix)
        while not np.array_equal(next_d_matrix, current_d_matrix):
            return self._get_matrix_compare(next_d_matrix)
        else:
            return current_d_matrix

    @staticmethod
    def _generate_r_matrix(input_matrix: np.ndarray) -> np.ndarray:
        r_matrix_obj = np.vectorize(lambda d: 1 if d else 0)
        r_matrix = r_matrix_obj(input_matrix)
        np.fill_diagonal(r_matrix, 1)

        return r_matrix

    def _generate_d_matrix(self, input_matrix: np.ndarray) -> np.ndarray:
        r_matrix = self._generate_r_matrix(input_matrix)
        index_pairs = [
            (i, j) for i in range(0, input_matrix.shape[0])
            for j in range(0, input_matrix.shape[1]) if i < j
        ]

        d_matrix = np.empty_like(input_matrix)
        for pair in index_pairs:
            i, j = pair
            sum_list = [
                r_matrix[j, k] * input_matrix[i, k] + r_matrix[i, k] * input_matrix[j, k]
                for k in range(0, input_matrix.shape[1])
            ]

            d_matrix[i, j] = d_matrix[j, i] = 0 if {*sum_list} == {0} else min({*sum_list}-{0})
            np.fill_diagonal(d_matrix, 0)

        return d_matrix
