from dataclasses import dataclass
from employee import Employee

@dataclass
class HourlyEmployee(Employee):
    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000
    

    def compute_pay(self) -> float:
        return (self.pay_rate * self.hours_worked) + self.employer_cost