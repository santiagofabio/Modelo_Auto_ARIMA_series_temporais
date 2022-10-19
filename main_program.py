from ctypes.wintypes import PINT
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams
from pmdarima.arima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from testa_hipotese_shapiro_wilk import testa_hipotese_shapiro_wilk

from scipy import stats

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
serie.plot()
plt.title("Serie Pluviometrica ")
plt.xlabel('Anos')
plt.savefig('serie_temporal_estudada.png', dpi =300, format ='png')
plt.show()


serie3 =(serie)**(1/3)
print(serie3)
serie3.plot(label ='Série Raiz Cúbica')
plt.title("Transformação raiz cúbica")
plt.xlabel('Anos')
plt.savefig('serie_raiz_cubica.png', dpi =300, format ='png')
plt.show()


modelo_auto = auto_arima(serie3, trace=True, stepwise=False, seasonal=True, max_p=10,max_q=10, max_P=4, max_Q=4,
                         start_p=0,start_q=0,start_P=0,start_Q=0,m=12)
print(modelo_auto.aic())

resultado_auto =modelo_auto.fit(serie3)

print(resultado_auto.summary())

residuos_auto = resultado_auto.resid

plt.plot(residuos_auto()) 
plt.savefig('residuo_autoarima.png', dpi =300, format ='png')
plt.show()

stats.probplot( residuos_auto(), dist ='norm' , plot =plt)
plt.title("Normal QQ plot -Residuo_AutoARIMA")
plt.savefig('normal_qq_residuo_autoarima.png', dpi =300, format ='png')
plt.show()

#Teste de Shapiro-Wilk 
statistic,value_p =stats.shapiro(residuos_auto())
print('Métricas  Shapiro-Wilk:\n')
print('Estatistica do teste: {:.6f} '.format(statistic))
print('p-valor: {:.6f} '.format(value_p))
testa_hipotese_shapiro_wilk(value_p, alpha)

import seaborn as sns
sns.displot(residuos_auto())
plt.show()

plot_acf(residuos_auto(), lags= 30)
plt.title("Diagrama Autocorrelação Residuo_AutoARIMA")
plt.xlabel('Nº Lags')
plt.ylabel('Autocorrelação')
plt.savefig('diagrama_acf_residuo_autoarima.png', dpi =300, format ='png')
plt.show()

plot_pacf(residuos_auto(), lags= 30)
plt.title("Diagrama Autocorrelação Parcial Residuo_AutoARIMA")
plt.xlabel('Nº Lags')
plt.ylabel('Autocorrelação parcial ')
plt.savefig('diagrama_pacf_residuo_autoarima.png', dpi =300, format ='png')
plt.show()


plt.plot(serie3, color ='blue', label='Série real')
plt.plot(serie3-residuos_auto(),color ='green', label='Residuo_AutoARIMA')
plt.legend(loc ='best')
plt.title('Comparativo Série e Residuo_AutoARIMA')
plt.xlabel('Anos')
plt.savefig('serie_e_residuo.png', dpi =300, format ='png')
plt.show()

previsao_auto =resultado_auto.predict(n_periods=12)

previsao_auto_escala = (previsao_auto)**3
pd.concat([serie,previsao_auto_escala], names=['Series real', 'Previsão']).plot()
plt.legend(loc ='best')
plt.title('Cenário preditivo')
plt.xlabel('Anos')
plt.ylabel('Indice Pluviometrico mm')
plt.savefig('cenario_preditivo.png', dpi =300, format ='png')
plt.show()


