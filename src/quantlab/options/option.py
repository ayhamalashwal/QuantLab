from dataclasses import dataclass


@dataclass
class EuropeanOption:
    spot: float
    strike: float
    maturity: float
    rate: float
    volatility: float
    option_type: str = "call"

    def is_call(self):
        return self.option_type.lower() == "call"

    def is_put(self):
        return self.option_type.lower() == "put"
