from quantlab import EuropeanOption, BlackScholes


def test_call_price():
    option = EuropeanOption(
        spot=100,
        strike=100,
        maturity=1,
        rate=0.05,
        volatility=0.2,
    )

    price = BlackScholes().price(option)

    assert abs(price - 10.45) < 0.01
