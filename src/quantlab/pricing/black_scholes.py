import math
from scipy.stats import norm

from ..options import EuropeanOption


class BlackScholes:
    """
    Black-Scholes pricing model for European options.
    """

    def price(self, option: EuropeanOption):
        S = option.spot
        K = option.strike
        T = option.maturity
        r = option.rate
        sigma = option.volatility

        d1 = (
            math.log(S / K)
            + (r + 0.5 * sigma ** 2) * T
        ) / (sigma * math.sqrt(T))

        d2 = d1 - sigma * math.sqrt(T)

        if option.is_call():
            return (
                S * norm.cdf(d1)
                - K * math.exp(-r * T) * norm.cdf(d2)
            )

        return (
            K * math.exp(-r * T) * norm.cdf(-d2)
            - S * norm.cdf(-d1)
        )
