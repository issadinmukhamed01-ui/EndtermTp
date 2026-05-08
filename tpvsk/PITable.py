import pandas as pd
from MonteCarloPi import MonteCarloPI
class PITable:
    NS = [100, 1_000, 10_000, 100_000]

    def __init__(self, seed: int = 42):
        self.seed = seed
        self._rows = [
            {"N": n,
             "pi_hat": MonteCarloPI(n, seed).estimate()}
            for n in self.NS
        ]

    def to_df(self) -> pd.DataFrame:
        return pd.DataFrame(self._rows)

table = PITable()
print(table.to_df().to_string(index=False))

