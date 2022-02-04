import datetime as dt
from math import sqrt
from pandas_datareader import data as pdr
from notifypy import Notify
import numpy as np
from scipy.optimize import minimize
import time

cantAcc = 0

listDeAccionesElectas = []
end = dt.datetime.now()
start = end - dt.timedelta(days = 365)
df = None
matriz = []
covar = []

def MatrizDeCovarianzas(df):

    Retornos = df.Close.pct_change()
    matrizCov = Retornos.cov()

    return matrizCov.to_numpy()

def objectiveRatioSharp(W):
    global covar
    transp = np.transpose(W) 

    desvio = sqrt(float(np.asarray(np.matmul((np.matmul(W , covar)) , transp))))
    Retorno = df.Close.pct_change().mean().to_numpy()

    retornoPonderado = np.matmul(Retorno , W)
    ratioSharp  = retornoPonderado / desvio
    return -ratioSharp

def objectiveMinimizarvarianza(W):
    global covar
    transp = np.transpose(W)
    y = float(np.asarray(np.matmul((np.matmul(W , covar)) , transp)))
    return y

def constraint1(W : list):
    return np.sum(W) - 1

con1 = {'type' : 'eq' , 'fun' : constraint1}
const = [con1]

def initialGuess():
    guesses = []
    value = 1 / cantAcc

    for i in range (0 , cantAcc):
        guesses.append(value)
    return guesses

def bnds():
    bnds = []
    value = (0.0 , 1.0)

    for i in range (0,cantAcc):
        bnds.append(value)

    return bnds

def optimizar(acciones , option : int):
    listDeAccionesElectas.append(acciones)
    global cantAcc
    cantAcc = len(acciones)
    global df
    try:
        df = pdr.get_data_yahoo(acciones , start , end)
    except:
        print("ingrese tickers correctos")
        time.sleep(1)
    global covar
    covar = MatrizDeCovarianzas(df)

    sol = None

    if option == 1:
        sol = optimizarRatioSharp()

    elif option == 2:
        sol =  optimizarVarianza()
    try:
        print(sol , "\n\n\n" )
        print("-----------------------------------")
        print("Valor Minimo: ")
        print(sol.fun , "\n")
        print("Pesos: ")
        print(listDeAccionesElectas)
        print(sol.x , "\n")
        listDeAccionesElectas.clear()
    except:
        print("Ingrese una opcion de optimizacion correcta ")
    



def optimizarRatioSharp():
    sol = minimize(objectiveRatioSharp        , initialGuess(), bounds = bnds(), constraints= const, options={ 'ftol': 1e-20,})
    return sol

def optimizarVarianza():
    sol = minimize(objectiveMinimizarvarianza , initialGuess(), bounds = bnds(), constraints= const, options={ 'ftol': 1e-20,})
    return sol

