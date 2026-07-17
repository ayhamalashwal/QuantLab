from scipy.optimize import brentq

from ..pricing import BlackScholes
from ..options import EuropeanOption


def implied_volatility(
    market_price,
    option: EuropeanOption
):
    """
    Calculate implied volatility using Brent's method.
    """

    def objective(sigma):
        temp_option = EuropeanOption(
            option.spot,
            option.strike,
            option.maturity,
            option.rate,
            sigma,
            option.option_type,
        )

        price = BlackScholes().price(temp_option)

        return price - market_price

    return brentq(
        objective,
        0.0001,
        5.0
    )
