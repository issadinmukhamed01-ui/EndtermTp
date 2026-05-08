import math
from fastapi import FastAPI

from tpvsk.MonteCarloPi import MonteCarloPI


class PIService:
    def __init__(self, seed: int = 42):
        self.seed = seed

    def handle(self, n: int) -> dict:
        pi_hat = MonteCarloPI(n, self.seed).estimate()
        return {
            "n":      n,
            "pi_hat": round(pi_hat, 6),
            "error":  round(abs(pi_hat - math.pi), 6),
        }

app = FastAPI()
_svc = PIService(seed=42)

@app.get("/pi")
def estimate(n: int = 10_000):
    return _svc.handle(n)