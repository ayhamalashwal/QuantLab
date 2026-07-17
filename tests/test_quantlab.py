from quantlab import (
    EuropeanOption,
    BlackScholes,
    MonteCarlo,
    delta,
    gamma,
    vega,
    implied_volatility,
)


def test_black_scholes_call():
    option = EuropeanOption(
        100, 100, 1, 0.05, 0.2
    )

    price = BlackScholes().price(option)

    assert round(price, 2) == 10.45


def test_greeks():
    option = EuropeanOption(
        100, 100, 1, 0.05, 0.2
    )

    assert round(delta(option), 4) == 0.6368
    assert round(gamma(option), 4) == 0.0188
    assert round(vega(option), 2) == 37.52


def test_implied_volatility():
    option = EuropeanOption(
        100, 100, 1, 0.05, 0.2
    )

    price = BlackScholes().price(option)

    iv = implied_volatility(price, option)

    assert round(iv, 2) == 0.20


def test_monte_carlo():
    option = EuropeanOption(
        100, 100, 1, 0.05, 0.2
    )

    price = MonteCarlo().price(
        option,
        simulations=200000
    )

    assert 10 < price < 11
