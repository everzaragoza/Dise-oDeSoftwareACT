from hourly_employee import HourlyEmployee
from salaried_employee_with_commission import SalariedEmployeeWithCommission

def main():
    juan = HourlyEmployee(name="Juan", id=12346, pay_rate=50, hours_worked=100)
    print(f"{juan.name} earned ${juan.compute_pay()}")

    pedro = SalariedEmployeeWithCommission(
        name="Pedro", id=47832, monthly_salary=5000, contracts_landed=10
    )
    print(f"{pedro.name} earned ${pedro.compute_pay()}")

if __name__ == "__main__":
    main()