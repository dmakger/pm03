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
        # try:
        sum_value = sum(np.asarray(self.vectors, dtype=float))
        result['value'] = " ".join(self.to_string(sum_value))
        # except Exception:
        #     result['info'] = self.VECTOR_ERROR

        return result

    def to_string(self, vector):
        result = list()
        for value in vector.tolist():
            value_int = int(value)
            if value == value_int:
                result.append(str(value_int))
            else:
                result.append(str(value))
        return result

    def clear(self):
        self.vectors.clear()
