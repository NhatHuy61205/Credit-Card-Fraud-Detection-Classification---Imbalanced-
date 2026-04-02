from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
import numpy as np

class TransactionInput(BaseModel):
    Time: float = Field(..., description="Seconds elapsed")
    Amount: float = Field(..., )
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    time_diff: float
    is_rapid_transaction: int


    @computed_field
    @property
    def log_amount(self) -> float:
        return np.log1p(self.Amount)

    @computed_field
    @property
    def Hour_from_start_mod24(self) -> int:
        return int((self.Time // 3600) % 24)

    @computed_field
    @property
    def is_night_proxy(self) -> int:
        return int(self.Hour_from_start_mod24 in [22,23,0,1,2,3,4,5])

    @computed_field
    @property
    def is_business_hours_proxy(self) -> int:
        return int(9 <= self.Hour_from_start_mod24 <= 17)
    
    @computed_field
    @property
    def hour_sin(self) -> float:
        return np.sin(2 * np.pi * self.Hour_from_start_mod24 / 24)

    @computed_field
    @property
    def hour_cos(self) -> float:
        return np.cos(2 * np.pi * self.Hour_from_start_mod24 / 24)
    
    @computed_field
    @property
    def is_high_amount(self) -> int:
        threshold = 5000
        return int(self.Amount > threshold)