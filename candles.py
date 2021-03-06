from binance.client import Client
import pandas as pd
import numpy as np

pairs = ['BTCUSDT', 'XLMBTC','IOTABTC','ADABTC' ,'BNBBTC' ,'EOSBTC' ,  'XRPBTC' ,'ETHBTC', 'LTCBTC', 'ETCBTC','NEOBTC']
client = Client('', '')


def createDataset():
    df = pd.DataFrame(columns=[ 'BTCUSDT', 'XLMBTC','IOTABTC','ADABTC' ,'BNBBTC' ,'EOSBTC' , 'XRPBTC' ,'ETHBTC', 'LTCBTC', 'ETCBTC','NEOBTC'])

    for pair in pairs:
        close = []
        candles = client.get_klines(
            symbol=pair, interval=Client.KLINE_INTERVAL_1MINUTE)
        for candle in candles:
            close.append(candle[4])
        df[pair] = np.array(close).astype(np.float)

    return df

<<<<<<< HEAD
=======
df = createDataset()
df.to_csv('dataset_1min')
>>>>>>> 6548af0d9f5e4a0a4847f8bbf9cc49b157fe634c
