
import datetime as dt
from math import sqrt
from pandas_datareader import data as pdr
from notifypy import Notify

cantDias = 250

def mediaMovil( accion , cantDias , df):
    precioSpot = df.Close
    return precioSpot.rolling(cantDias).mean()[accion]

def notificar(accion , mensaje):
    notificacion = Notify()
    notificacion.title = accion
    notificacion.message = mensaje
    notificacion.send()

def ChequearAcciones( start  , end ):
    arc_acciones = open("ListadoDeAcciones.txt")
    listaDeAcciones = arc_acciones.read().split()

    df = pdr.get_data_yahoo(listaDeAcciones , start , end)

    #spy = pdr.DataReader('SPY','yahoo', start, end)
    cuerpo = ""
    
    for accion in listaDeAcciones:
        
        i = 0

        if(ValidacionDeRetorno(accion , df )):
            cuerpo += "- Kurt y Asimetria OK - \n"
            i += 1
        if(RSI(accion , df)):
            cuerpo += "- RSI entre 40 y 70 - \n"
            i += 1
        if (margenInferior(accion , df) > 0):
            cuerpo += "- margen inferio POSITIVO - \n"
            i += 1 
        if (testDeHipotesis(accion , df) > 1.28):
            cuerpo += "- Rechaza h0 - \n"
            i += 1
        if (mediaMovil( accion ,50 , df).iloc[-1] > mediaMovil(accion , 200 , df).iloc[-1]):
            cuerpo += "- MA50 > MA200 - \n"
            i += 1
        if (df.Close[accion].iloc[-1] > mediaMovil(accion , 50 , df).iloc[-1]):
            cuerpo += "- Spot > MA50  - \n"
            i += 1 


        if i > 3 :
            notificar(accion , cuerpo)
            print(accion)

        cuerpo = ""    
            

def RatioSharp(accion , spy , df):
    variacion = df.Close[accion].pct_change()
    Retorno = variacion.mean()
    Desvio = variacion.std(ddof=1)
    rSharp = Retorno / Desvio
    
    
    variacionSpy = spy['Close'].pct_change()
    RetornoSpy = variacionSpy.mean()
    Desvio = variacionSpy.std(ddof=1)
    rSharpSpy = RetornoSpy / Desvio

    return rSharp > rSharpSpy

def ValidacionDeRetorno(accion , df):
    return (df.Close[accion].pct_change().skew(skipna = 1) < 0) & (df.Close[accion].pct_change().kurtosis(skipna = 1) > 0) 
            
def desvio(accion , df): 
    return df.Close[accion].pct_change().std(ddof=1)

def margenInferior(accion , df):
    return df.Close[accion].pct_change().mean() - 1.68 * desvio(accion , df) / sqrt(cantDias)

def testDeHipotesis(accion , df):
    return df.Close[accion].pct_change().mean() / (desvio(accion , df) / sqrt(cantDias))

def RSI(accion , df):
    
    delta = df.Close[accion].diff()
    up = delta.clip(lower=0)
    down = -1*delta.clip(upper=0)
    ema_up = up.ewm(com=13, adjust=False).mean()
    ema_down = down.ewm(com=13, adjust=False).mean()
    rs = ema_up/ema_down
    rsi = (100 - (100 / (1 + rs))).iloc[-1]

    return (rsi >= 40) & (rsi <= 70)

end = dt.datetime.now()
start = end - dt.timedelta(days = cantDias)

ChequearAcciones( start , end )
