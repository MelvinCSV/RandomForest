from Tree import Tree
from Pile import Pile
from random_fun import get_random_tuple
import pandas as pd
import numpy as np


class ScoreFunction:

    def __call__(self, data: np.ndarray, *args, **kwargs) -> float:
        return 0


class RandomTree(Tree):

    def __init__(self, is_leaf: bool, data: tuple, df: pd.DataFrame):
        Tree.__init__(self, is_leaf, data)
        self.__df = df

    def find_leaf(self, df: pd.Series) -> Tree:
        if self.is_leaf():
            return self

        data = self.get_data()
        childrens = self.get_children()
        test = df[data['column']] <= data['value']

        if test:
            child = childrens[0]

        else:
            child = childrens[1]

        return child.find_leaf(df)

    def eval(self, df, score_fun: ScoreFunction):
        assert (isinstance(df, pd.Series) or isinstance(df, pd.DataFrame))
        if isinstance(df, pd.Series):
            return self.__eval_series(df, score_fun)

        if isinstance(df, pd.DataFrame):
            return self.__eval_dataframe(df, score_fun)

    def __eval_series(self, df: pd.Series, score_fun: ScoreFunction) -> float:
        leaf = self.find_leaf(df)
        value = leaf.get_value()
        score = score_fun(df.values, value)

        return score

    def __eval_dataframe(self, df: pd.DataFrame, score_fun: ScoreFunction) -> pd.Series:
        res = pd.Series()
        for ind in df.index:
            score = self.__eval_series(df.loc[ind], score_fun)
            res.loc[ind] = score

        return res

class RandomForest:

    def __init__(self, n_trees: int, min_leaf: int, n_col: int, score_fun: ScoreFunction):
        self.__n_trees = n_trees
        self.__min_leaf = min_leaf
        self.__n_col = n_col
        self.__score_fun = score_fun
        self.__trees = []
        self.__df = None

    def fit(self, df: pd.DataFrame, score_fun: ScoreFunction):
        self.__df = df

    def build_bootstrap_data(self) -> pd.DataFrame:
        n = len(self.__df)
        idx = []

        for i in range(n):
            idx.append(self.__df.index[np.random.randint(0, n)])

        res = self.__df.reindex(idx)

        return res

    def build_tree(self):
        df = self.build_bootstrap_data()
        p = df.shape[1]

        def aux(data: pd.DataFrame, tree: RandomTree):
            cols = df.columns[get_random_tuple(self.__n_col, p)]


# def build_random_tree()
