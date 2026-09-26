from dataclasses import dataclass
from typing import Optional
from contract import Contract
from commission import Commission

@dataclass
class Employee:
    name: str
    id: int
    contract: Contract
    commission: Optional[Commission] = None

    def compute_pay(self) -> float:
        payout = self.contract.compute_pay()
        if self.commission:
            payout += self.commission.get_payment()
        return payout