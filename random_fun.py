import numpy as np
import pandas as pd


def get_random_tuple(k: int, n: int):
    """
    :param k:
    :param n:
    :return: k-tuple of random different numbers between 0 and n-1
    """

    res = []
    i = 0
    while i < k:
        random_int = np.random.randint(0, n)
        if random_int not in res:
            res.append(random_int)
            i += 1

    return res


def get_bootstrap_data(data: pd.DataFrame) -> pd.DataFrame:
    n = len(data)
    idx = []

    for i in range(n):
        idx.append(data.index[np.random.randint(0, n)])

    res = data.reindex(idx)

    return res


if __name__ == '__main__':
    k_ = 3
    n_ = 10
    for j in range(10):
        print(get_random_tuple(k_, n_))
