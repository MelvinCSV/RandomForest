import numpy as np


def ridge_reg(x: np.ndarray, y: np.ndarray, lmd: float = 0) -> np.ndarray:
    assert x.shape[1] == y.shape[0]

    return np.linalg.inv(x.T.dot(x) - lmd * np.identity(len(x))).dot(x.T.dot(y))
