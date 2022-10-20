from ctypes.wintypes import PINT
from django.forms import modelform_factory
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams
from pmdarima.arima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from testa_hipotese_shapiro_wilk import testa_hipotese_shapiro_wilk
from avaliacao_residuo import avaliacao_residuo
from visualizacao_previsao_auto_arima import visualizacao_previsao_auto_arima
from scipy import stats
from modelo_moving_avarage import  modelo_moving_avarage
from modelo_arma import  modelo_arma
from modelo_preditivo_autoregressivo import modelo_preditivo_autoregressivo
from modelo_preditivo_arima import modelo_preditivo_arima
import pickle
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] =[15,6]

alpha =0.05
file ='chuva_tratado.csv'
chuva =pd.read_csv('chuva_tratado.csv', sep= ',')
print(f'{chuva.head()}')

chuva2 =chuva.drop(columns='Ano')
chuva3 =chuva2.values
chuva4 =list(chuva3.flatten()) 

#criação dos indices
indice = pd.date_range('1985', periods=len(chuva4), freq='M')

#criação da serie
serie = pd.Series(chuva4, index=indice )
serie.plot(label ='Série real')
plt.title("Serie Pluviometrica ")
plt.xlabel('Anos')
plt.legend(loc ='best')
plt.savefig('serie_temporal_estudada.png', dpi =300, format ='png')
plt.show()


serie3 =(serie)**(1/3)
print(serie3)
serie3.plot(label ='Série Raiz Cúbica')
plt.title("Transformação raiz cúbica")
plt.xlabel('Anos')
plt.legend(loc ='best')
plt.savefig('serie_raiz_cubica.png', dpi =300, format ='png')
plt.show()

"""
#Modelo Auto ARIMA
modelo_auto = auto_arima(serie3, trace=True, stepwise=False, seasonal=True, max_p=10,max_q=10, max_P=4, max_Q=4,
                         start_p=0,start_q=0,start_P=0,start_Q=0,m=12)
print(modelo_auto.aic())

resultado_auto =modelo_auto.fit(serie3)

# Open a file and use dump()
with open('resultado_auto.pkl', 'wb') as arquivo:
    # A new file will be created
    pickle.dump(resultado_auto,arquivo)

print(resultado_auto.summary())
residuos_auto = resultado_auto.resid

#Estudo dos residuos
avaliacao_residuo(residuos_auto,alpha)

periodo =12
visualizacao_previsao_auto_arima(serie,serie3,residuos_auto, resultado_auto, periodo)

#--------Modelo Auto Regressivo
modelo_preditivo_autoregressivo(serie3,serie)


#-----Modelo  moving_avarage
modelo_moving_avarage(serie3, serie)

#---------Modelo ARMA---------
modelo_arma(serie3,serie)

#--------Modelo ARIMA
modelo_preditivo_arima(serie3,serie)
"""







# -------------------------Leitura das previsões

with open("previsao_auto_arima.pkl", "rb") as arquivo:
    prev_auto_arima =pickle.load(arquivo)
    
with open("previsao_modelo_ar_escala.pkl", "rb") as arquivo:
    prev_autoregressivo =pickle.load(arquivo)

with open("previsao_modelo_arima_escala.pkl", "rb") as arquivo:
    prev_arima =pickle.load(arquivo)
    
with open("previsao_modelo_arma_escala.pkl", "rb") as arquivo:
    prev_arma =pickle.load(arquivo)

with open("previsao_modelo_moving_average.pkl", "rb") as arquivo:
    prev_moving_average =pickle.load(arquivo)

#----------------------------------------------------




#Lista com os valores reais
lista =[373.3,174.1,137.8,55.7]

valores_reais =pd.DataFrame(lista, columns =['Valores reais'])
print(valores_reais)

# Autoarima 
prev_auto_arima_validacao = prev_auto_arima.iloc[0:4]
pd.DataFrame.reset_index(prev_auto_arima_validacao, drop =True, inplace =True)
print(prev_auto_arima_validacao)




#Autoregressivo
prev_autoregressivo_validacao =prev_autoregressivo.iloc[1:5]
pd.DataFrame.reset_index(prev_autoregressivo_validacao, drop =True, inplace =True)
print(prev_autoregressivo_validacao)

#Arima
prev_arima_validacao =  prev_arima.iloc[1:5]
pd.DataFrame.reset_index(prev_arima_validacao, drop =True, inplace =True)
print(prev_arima_validacao)

#Arma 
prev_arma_validacao = prev_arma.iloc[1:5]
pd.DataFrame.reset_index(prev_arma_validacao, drop =True, inplace =True)
print(prev_arma_validacao)

#Moving Average
prev_moving_average = prev_moving_average.iloc[1:5]
pd.DataFrame.reset_index(prev_moving_average, drop =True, inplace =True)
print(prev_moving_average)

desempenho =pd.concat([valores_reais,prev_auto_arima_validacao,prev_moving_average, prev_arma_validacao,prev_arima_validacao], axis =1)
 
#desempenho.columns =['Valores_reais','Previsao_AUTO','Previsao_MA','Previsao_ARMA','Previsao_ARIMA'] 

print(desempenho.columns)

#from sklearn.metrics import mean_absolute_error,mean_squared_error
