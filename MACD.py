# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
from datetime import datetime, date, timedelta
from yahooquery import Ticker


# %%

#stocks = ["UPS","GME","AAPL","BB","OCGN"]
 
 


# %%
def df_(stocks2,Symbol,Volume_Price):
    #d200 = datetime.today() - timedelta(days=100)
    #yq_data200 = stocks2.history(start=d200, interval='1d')
    yq_data200 = stocks2
    #yq_data200.reset_index(inplace=True)

    
    if Volume_Price=="Volume":
        df = yq_data200[['symbol','date','volume']]
        df1 = df[df.symbol==Symbol]

    if Volume_Price=="Price":
        df = yq_data200[['symbol','date','close']]
        df1 = df[df.symbol==Symbol]

    return df1


# %%
#df_(stocks2,"GME","Volume")


# %%
def rolling_avgs(stocks2,Symbol, days,Volume_Price,MA=False, EMA=False, MACD_V=False,MACD_P=False):
    """
    Add selected moving averages to the DataFrame
    """
    global df
    df=df_(stocks2,Symbol,Volume_Price)
    if MA==True:
    # simple moving average
        #df["MA"] = df["adjclose"].rolling(window=days).mean()
        df["MA"] = df["volume"].rolling(window=days).mean()
        df["v/VMA"] =  df["volume"] / df["MA"]   
        df = df['v/VM'].iloc[-1]     

    if EMA==True:
    # exponential moving average
        df["EMA"] = df["adjclose"].ewm(span=days).mean()

    if MACD_V==True:
        # exponential moving average
        df["EMA_3"] = df["volume"].ewm(span=5).mean()
        df["EMA_10"] = df["volume"].ewm(span=10).mean()
        df["MACD"] = df["EMA_3"]/df["EMA_10"] 

          #for last value #hide this for dataframe
        #df = df['MACD'].iloc[-1]

        
        #for a dict
        df={df['symbol'].iloc[-1] : df['MACD'].iloc[-1]}



    if MACD_P==True:
        # exponential moving average
        df["EMA_3"] = df["close"].ewm(span=5).mean()
        df["EMA_10"] = df["close"].ewm(span=10).mean() 
        df["MACD"] = df["EMA_3"]/df["EMA_10"] 

        #for last value #hide this for dataframe
        #df = df['MACD'].iloc[-1]

        
        #for a dict
        df={df['symbol'].iloc[-1] : df['MACD'].iloc[-1]}

      
    return df


# %%
#rolling_avgs(stocks2,"OCGN",30,"Volume",MACD_V=True)


# %%
def rollavg(stocks,yq_data90x,days,Volume_Price,MACD_V=False,MACD_P=False):
    stocks2=yq_data90x
    MACD_df2= []
    i=0
    for i in stocks:
        try:
            if MACD_V==True:
                MACD_df = rolling_avgs(stocks2,i,days,Volume_Price,MACD_V=True)
            if MACD_P==True :
                MACD_df = rolling_avgs(stocks2,i,days,Volume_Price,MACD_P=True) 
            MACD_df2.append(MACD_df)
        except:
            continue
        MACD_df2
        dr = {k: v for dct in MACD_df2 for k, v in dct.items()}

    return dr


# %%
#rollavg(stocks,30,"Price",MACD_P=True)


# %%
#rollavg(stocks,30,"Volume",MACD_V=True)


