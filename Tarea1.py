import xlrd
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score
import  numpy as np
import matplotlib.pyplot as plt

data=pd.read_excel('BI_Alumnos07.xlsx')
print(data.shape)
dataX=data[['Altura']]
x=np.array(dataX)
y=data['Peso'].values
regL=linear_model.LinearRegression()
regL.fit(x,y)
y_pred=regL.predict(x)
print('Coeficiente de R: ',regL.coef_)
print("Error cuadrado medio: %2.f" % mean_squared_error(y,y_pred))
print("Puntaje de Varianza: %2.f" % r2_score(y,y_pred))
x=data['Altura']
arreglo=np.array(x)
print("-----------------------")
print("| Altura","|Predicción|")
for i in arreglo:
    predPeso=regL.predict([[i]])
    print("|  ",i," | ",int(predPeso),"     |")
