import httpx
import yfinance as yf
import numpy as np
from settings import config

def main():

    tickers = ["AAPL", "TSLA"]
    data = yf.download(
        tickers=tickers,
        start="2020-01-01",
        end="2021-01-01"
    )

    data = data['Adj Close']

    returns = np.log(data/data.shift(1))

    returns.cov()

    pass




if __name__ == '__main__':
    main()