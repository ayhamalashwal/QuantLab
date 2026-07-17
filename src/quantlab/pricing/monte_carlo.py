import numpy as np

from ..options import EuropeanOption


class MonteCarlo:
    """
    Monte Carlo simulator for European option pricing.
    """

    def price(self, option: EuropeanOption, simulations=100000):
        S = option.spot
        K = option.strike
        T = option.maturity
        r = option.rate
        sigma = option.volatility

        Z = np.random.standard_normal(simulations)

        ST = S * np.exp(
            (r - 0.5 * sigma ** 2) * T
            + sigma * np.sqrt(T) * Z
        )

        if option.is_call():
            payoff = np.maximum(ST - K, 0)
        else:
            payoff = np.maximum(K - ST, 0)

        return np.exp(-r * T) * np.mean(payoff)
