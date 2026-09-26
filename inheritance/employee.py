from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    id: int

    def compute_pay(self) -> float:
        return 0.0