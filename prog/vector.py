import numpy as np


class VectorManager:
    SUCCESS = 0
    EMPTY_ERROR = 1
    VECTOR_ERROR = 2

    def __init__(self, root):
        self.root = root
        self.vectors = list()

    def add(self, vector):
        vector_np = np.array(vector)
        self.vectors.append(vector_np)

    def sum(self):
        result = {
            "value": None,
            "info": self.SUCCESS
        }
        if len(self.vectors) == 0:
            result['info'] = self.EMPTY_ERROR
        try:
            result['value'] = sum(np.asarray(self.vectors, dtype=float))
        except Exception:
            result['info'] = self.VECTOR_ERROR

        return result

    def clear(self):
        self.vectors.clear()