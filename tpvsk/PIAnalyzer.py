import math
from PITable import PITable
class PIAnalyzer:
    def __init__(self, table: PITable):
        self.df = table.to_df().copy()

    def summary(self) -> pd.DataFrame:
        df = self.df.copy()
        df["error"] = (df["pi_hat"] - math.pi).abs()
        df["error"] = df["error"].map("{:.6f}".format)
        return df

ana = PIAnalyzer(PITable())
print(ana.summary().to_string(index=False))