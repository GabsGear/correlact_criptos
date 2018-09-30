from binance.client import Client
import pandas as pd
import numpy as np

pairs = ['BTCXLM', 'BTCIOTA', 'BTCADA', 'BTCBNB', 'BTCEOS', 'BTCXRP',
         'BTCETH', 'BTCLTC', 'BTCETC', 'BTCTRX', 'BTCNEO', 'BTCLTC']
client = Client('', '')


def createDataset():
    df = pd.DataFrame(columns=['BTCXLM', 'BTCIOTA', 'BTCADA', 'BTCBNB', 'BTCEOS', 'BTCXRP',
                               'BTCETH', 'BTCLTC', 'BTCETC', 'BTCTRX', 'BTCNEO', 'BTCLTC'])

    for pair in pairs:
        close = []
        candles = client.get_klines(
            symbol=pair, interval=Client.KLINE_INTERVAL_1MINUTE)
        for candle in candles:
            close.append(candle[4])
        df[pair] = np.array(close).astype(np.float)

    return df

