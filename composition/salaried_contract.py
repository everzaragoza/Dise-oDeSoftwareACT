from dataclasses import dataclass
from contract import Contract

@dataclass
class SalariedContract(Contract):
    monthly_salary: float = 0
    percentage: float = 1

    def compute_pay(self) -> float:
        return self.monthly_salary * self.percentage