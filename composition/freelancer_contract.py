from dataclasses import dataclass
from contract import Contract

@dataclass
class FreelancerContract(Contract):
    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked