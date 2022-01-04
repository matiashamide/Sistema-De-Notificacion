
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

#msft = pd.read_csv('C:/Users/Matias/AppData/Local/Programs/Python/Python39/Lib/site-packages/matplotlib/mpl-data/sample_data/msft.csv')
msft = yf.Ticker("MSFT")

print(msft.info)
#plt.show()

'''
msft['MA5'] = msft['Close'].rolling(5).mean()
msft['MA50'] = msft['Close'].rolling(50).mean()
msft['MA200'] = msft['Close'].rolling(200).mean()
'''
msft['MA5'].plot()
#plt.show()

precio = msft.iloc[0 , 4]
print(precio)
print(msft['MA5'][4])



def notificarAFabio():
    if precio > msft['MA5'][4]:
        print(5)    
notificarAFabio()
