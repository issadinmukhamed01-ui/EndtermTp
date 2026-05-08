import math
import matplotlib.pyplot as plt
from PITable import PITable
from PIAnalyzer import PIAnalyzer

class PIPlotter:
    def __init__(self, analyzer: PIAnalyzer):
        self.df = analyzer.summary()

    def save_png(self, path: str = "pi_estimate.png"):
        df = self.df.copy()
        df["error"] = df["error"].astype(float)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(df["N"], df["pi_hat"],
                marker="o", linewidth=1.5, label="π̂")
        ax.axhline(math.pi, color="red",
                   linestyle="--", linewidth=1, label="π")
        ax.set_xscale("log")
        ax.set_xlabel("N"); ax.set_ylabel("π̂")
        ax.set_title("Монте-Карло оценка π")
        ax.legend(); plt.tight_layout()
        plt.savefig(path, dpi=150)
        return path

PIPlotter(PIAnalyzer(PITable())).save_png()