from dataclasses import dataclass
from typing import Optional


@dataclass
class BillRecord:
    """Domain model for storing electricity bill records."""
    units: float
    predicted_amount: float
    actual_amount: Optional[float] = None
    anomaly_flag: int = 0

    def to_tuple(self):
        return (self.units, self.predicted_amount, self.actual_amount, self.anomaly_flag)
