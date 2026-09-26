from dataclasses import dataclass
from employee import Employee

@dataclass
class SalariedEmployee(Employee):
    monthly_salary: float = 0
    percentage: float = 1

    def compute_pay(self) -> float:
        return self.monthly_salary * self.percentage