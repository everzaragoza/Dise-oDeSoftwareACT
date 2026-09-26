from dataclasses import dataclass
from contract import Contract

@dataclass
class HourlyContract(Contract):
    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        return (self.pay_rate * self.hours_worked) + self.employer_cost