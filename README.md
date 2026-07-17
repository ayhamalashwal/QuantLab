# QuantLab

A Python quantitative finance library for option pricing, risk analysis, and volatility modeling.

## Features

- Black-Scholes option pricing
- Monte Carlo simulation pricing
- Delta, Gamma, Vega calculations
- Implied volatility solver

## Installation

```bash
git clone https://github.com/ayhamalashwal/QuantLab.git
cd QuantLab
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Example

```python
from quantlab import (
    EuropeanOption,
    BlackScholes,
    MonteCarlo,
    delta,
    gamma,
    vega,
    implied_volatility,
)

option = EuropeanOption(
    spot=100,
    strike=100,
    maturity=1,
    rate=0.05,
    volatility=0.2,
)

bs = BlackScholes()
mc = MonteCarlo()

price = bs.price(option)

print("Black-Scholes price:", price)
print("Monte Carlo price:", mc.price(option))
print("Delta:", delta(option))
print("Gamma:", gamma(option))
print("Vega:", vega(option))
print("Implied volatility:", implied_volatility(price, option))
```

## Project Structure

```
src/
└── quantlab/
    ├── options/
    ├── pricing/
    ├── greeks/
    └── volatility/
```

## Documentation

Detailed explanations of the models and mathematics:

- [Option Pricing](docs/pricing.md)
- [Option Greeks](docs/greeks.md)
- [Volatility Tools](docs/volatility.md)
- [QuantLab Architecture](docs/models.md)

## License

MIT License
# 
