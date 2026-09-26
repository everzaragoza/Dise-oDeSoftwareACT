from employee import Employee
from hourly_contract import HourlyContract
from salaried_contract import SalariedContract
from contract_commission import ContractCommission

def main():

    
    juan_contract = HourlyContract(pay_rate=50, hours_worked=100)
    juan = Employee(name="Juan", id=12346, contract=juan_contract)
    print(f"{juan.name} earned ${juan.compute_pay()}")


   
    pedro_contract = SalariedContract(monthly_salary=5000)
    pedro_commission = ContractCommission(contracts_landed=10)
    pedro = Employee(name="Pedro", id=47832, contract=pedro_contract, commission=pedro_commission)
    print(f"{pedro.name} earned ${pedro.compute_pay()}")

if __name__ == "__main__":
    main()