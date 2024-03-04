import random
from dataclasses import dataclass

__all__ = ["CleaningResults", "PondCleaner"]


@dataclass
class CleaningResults:
    garbage: float


class PondCleaner:
    def clean(self) -> CleaningResults:
        garbage = random.uniform(0, 3)
        return CleaningResults(garbage)
