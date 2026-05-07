import numpy as np

class PointCloud:
    def __init__(self, N: int, seed: int = 42):
        self.N = N
        self.seed = seed
        rng = np.random.default_rng(seed)
        self.points = rng.uniform(-1, 1, (N, 2))
        self.inside_mask = (
            self.points[:, 0]**2 +
            self.points[:, 1]**2
        ) <= 1

    def fraction(self) -> float:
        return self.inside_mask.mean()

# использование
cloud = PointCloud(N=10_000)
print(cloud.fraction())  # 0.7854