import xlrd
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import  mean_squared_error, r2_score
import numpy as np
data=pd.read_excel('Data_Ev2.xlsx')
lista=pd.DataFrame()
alt=data['YearlyIncome']
ed=data['TotalChildren']
lista['YearlyIncome']=alt
lista['TotalChildren']=ed
XY=np.array(lista)
Z=data['NumberCarsOwned'].values
regLM=linear_model.LinearRegression()
regLM.fit(XY,Z)
z_pred=regLM.predict(XY)
print('Coeficientes de R',regLM.coef_)
print('error cuadrado medio: %.2f '% mean_squared_error(Z,z_pred))
print('puntaje de varianza: %.2f' % r2_score(Z,z_pred))

predCarro= regLM.predict([[50000,5]])
print('prediccion de Numero de Carro: ', int(predCarro))