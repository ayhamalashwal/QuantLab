import math
from scipy.stats import norm

from ..options import EuropeanOption


def delta(option: EuropeanOption):
    S = option.spot
    K = option.strike
    T = option.maturity
    r = option.rate
    sigma = option.volatility

    d1 = (
        math.log(S / K)
        + (r + 0.5 * sigma ** 2) * T
    ) / (sigma * math.sqrt(T))

    if option.is_call():
        return norm.cdf(d1)

    return norm.cdf(d1) - 1


def gamma(option: EuropeanOption):
    S = option.spot
    K = option.strike
    T = option.maturity
    r = option.rate
    sigma = option.volatility

    d1 = (
        math.log(S / K)
        + (r + 0.5 * sigma ** 2) * T
    ) / (sigma * math.sqrt(T))

    return norm.pdf(d1) / (
        S * sigma * math.sqrt(T)
    )


def vega(option: EuropeanOption):
    S = option.spot
    K = option.strike
    T = option.maturity
    r = option.rate
    sigma = option.volatility

    d1 = (
        math.log(S / K)
        + (r + 0.5 * sigma ** 2) * T
    ) / (sigma * math.sqrt(T))

    return (
        S * norm.pdf(d1)
        * math.sqrt(T)
    )
