from PointCloud import PointCloud

class MonteCarloPI(PointCloud):
    def estimate(self) -> float:
        return 4 * self.fraction()

# два прогона
for s in (42, 43):
    m = MonteCarloPI(N=100_000, seed=s)
    print(f"seed={s}  π̂={m.estimate():.5f}")