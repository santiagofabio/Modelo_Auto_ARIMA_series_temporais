def avaliacao_residuo(residuos_auto,alpha):
      from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
      from testa_hipotese_shapiro_wilk import testa_hipotese_shapiro_wilk
      import numpy as np
      import pandas as pd
      import matplotlib.pyplot as plt
      from scipy import stats

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
      return(0)