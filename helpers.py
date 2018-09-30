import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.stats import pearsonr
import seaborn as sns

def printAll(df):
    fig = plt.figure(figsize=(15, 15))
    ax3 = fig.add_subplot(331)
    ax3.set_xlabel('Amostra')
    ax3.set_ylabel('valor')
    ax3.set_title('XLMBTC')
    plt.plot(df['XLMBTC'])

    ax4 = fig.add_subplot(332)
    ax4.set_xlabel('Amostra')
    ax4.set_ylabel('valor')
    ax4.set_title('IOTABTC')
    plt.plot(df['IOTABTC'])

    ax5 = fig.add_subplot(333)
    ax5.set_xlabel('Amostra')
    ax5.set_ylabel('valor')
    ax5.set_title('ADABTC')
    plt.plot(df['ADABTC'])

    ax6 = fig.add_subplot(334)
    ax6.set_xlabel('Amostra')
    ax6.set_ylabel('valor')
    ax6.set_title('BNBBTC')
    plt.plot(df['BNBBTC'])

    ax7 = fig.add_subplot(335)
    ax7.set_xlabel('Amostra')
    ax7.set_ylabel('valor')
    ax7.set_title('EOSBTC')
    plt.plot(df['EOSBTC'])


    ax8 = fig.add_subplot(336)
    ax8.set_xlabel('Amostra')
    ax8.set_ylabel('valor')
    ax8.set_title('XRPBTC')
    plt.plot(df['XRPBTC'])


    ax9 = fig.add_subplot(337)
    ax9.set_xlabel('Amostra')
    ax9.set_ylabel('valor')
    ax9.set_title('ETHBTC')
    plt.plot(df['ETHBTC'])


    ax10 = fig.add_subplot(338)
    ax10.set_xlabel('Amostra')
    ax10.set_ylabel('valor')
    ax10.set_title('NEOBTC')
    plt.plot(df['NEOBTC'])

    ax11 = fig.add_subplot(339)
    ax11.set_xlabel('Amostra')
    ax11.set_ylabel('valor')
    ax11.set_title('LTCBTC')
    plt.plot(df['LTCBTC'])

    plt.show()


    
def linregress(df):
    x = np.arange(0, 500)
    col = df.columns[1:len( df.columns)-1]

    for column in col:
        value = linregress(x, df[column])
        print('MOEDA: ' + str(column))
        print(str(value) + '\n')
        
        
def normalize(timeseries):
    normalized = (timeseries-timeseries.min())/(timeseries.max()-timeseries.min())
    return normalized 


def normalizeDF(df):
    col = df.columns
    col = col[1:len( df.columns)]
    for c in col:
        df[col] = normalize(df[col])


def printScatter(df):
    pd.plotting.scatter_matrix(df, alpha = 0.3, figsize = (14,8), diagonal = 'kde');
    

def corrAll(df):
    plt.figure(figsize=(12,8))
    kwargs = {'fontsize':12,'color':'black'}
    sns.heatmap(df.corr(),annot=True,robust=True)
    plt.title('Correlation Analysis',**kwargs)
    plt.tick_params(length=3,labelsize=12,color='black')
    plt.yticks(rotation=0)
    plt.show()
    
def print2(dt1, dt2):
    fig = plt.figure(figsize=(30, 30))
    ax6 = fig.add_subplot(334)
    ax6.set_xlabel('Amostra')
    ax6.set_ylabel('valor')
    ax6.set_title(dt1)
    plt.plot(df[dt1])

    ax7 = fig.add_subplot(335)
    ax7.set_xlabel('Amostra')
    ax7.set_ylabel('valor')
    plt.show()
    
def compare(dt1, dt2):
    plt.plot(df[dt1], label=dt1)
    plt.plot(df[dt2], label=dt2)
    plt.xlabel('Amostra')
    plt.ylabel('Valor')
    plt.title("Compare")
    plt.legend()
    plt.show()
    
def pearsonr(dt1, dt2):
    return pearsonr(dt2, dt2)
    