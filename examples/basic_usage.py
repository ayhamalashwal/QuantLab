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

print(
    "Implied volatility:",
    implied_volatility(price, option)
)
