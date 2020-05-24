import xlrd
import pandas as pd
from sklearn import linear_model
#importamos la funcion que nos permitira tener la regresion lineal
from sklearn.metrics import mean_squared_error,r2_score
#para obtener el coeficiente de r , obtener margenes de error
import  numpy as np
import matplotlib.pyplot as plt

data=pd.read_excel('BI_Alumnos07.xlsx')
print(data.shape)#puedo reconocer el numero de filas y de dimensiones estadisticas del grupo
print(data.describe())
#omite la columna nombre para utilizar
data.drop(['Nombres'],1).hist()
#hist es el metodo que eliminara el campo
plt.show()
dataX=data[['Altura']]
x=np.array(dataX)
y=data['Peso'].values
regL=linear_model.LinearRegression()
regL.fit(x,y)
y_pred=regL.predict(x)
print('Coeficiente de R: ',regL.coef_)
print("Error cuadrado medio: %2.f" % mean_squared_error(y,y_pred))
print("Puntaje de Varianza: %2.f" % r2_score(y,y_pred))
predPeso=regL.predict([[180]])
print("Prediccion de Peso:",int(predPeso))

