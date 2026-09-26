from dataclasses import dataclass
from commission import Commission

@dataclass
class ContractCommission(Commission):
    commission_per_contract: float = 100
    contracts_landed: float = 0

    def get_payment(self) -> float:
        return self.commission_per_contract * self.contracts_landed