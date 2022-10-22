def modelo_preditivo_arima(serie3,serie):
      import matplotlib.pyplot as plt
      from statsmodels.tsa.arima.model import ARIMA
      from matplotlib.pylab import rcParams
      rcParams['figure.figsize'] =[15,6]
      import pandas as pd
      import pickle

      modelo_arima = ARIMA(serie3, order=(10,1,2))
      resultado_arima = modelo_arima.fit()
      print(resultado_arima.summary())
      residuos_modelo_arima =resultado_arima.resid
      plt.plot(serie3, label ="Série Real", color ='blue') 
      plt.plot(serie3-residuos_modelo_arima, color= 'green', label ='Residuos-ARIMA')
      plt.legend(loc ='best')
      plt.show()
      #Previsão modelo AR
      resultado_arima.fittedvalues
      previsao_modelo_arima =resultado_arima.predict(start =431, end =443)
      plt.plot(serie3, color = 'blue', label ='Serie real' )
      plt.plot(previsao_modelo_arima, color ='orange', marker ="^", label = 'Previsao ARIMA')
      plt.plot(serie3-residuos_modelo_arima, color= 'green', label ='Residuos-ARIMA')
      plt.xlabel('Anos')
      plt.title('Serie transformada e previsao ARIMA')
      plt.legend(loc ='best')
      plt.savefig('comparativo_serie_residuo_previsao_arima.png', format ='png', dpi=300)
      plt.show()
 
      previsao_modelo_arima_escala =pd.DataFrame(previsao_modelo_arima**3, columns=['Previsao_ARIMA'])
      plt.plot(serie, color = 'blue', label ='Serie real' )
      plt.plot(previsao_modelo_arima_escala, color ='orange', marker ="^", label ='Previsao-arima')
      plt.xlabel('Anos')
      plt.ylabel('Indíce pluviimétrico em mm')
      plt.title('Serie e previsao modelo ARIMA')
      plt.legend(loc ='best')
      plt.savefig('previsao_arima.png', format ='png', dpi=300)
      plt.show()
     
      # Open a file and use dump()
      with open('previsao_modelo_arima_escala.pkl', 'wb') as arquivo:
    #      A new file will be created
            pickle.dump(previsao_modelo_arima_escala,arquivo)
     
      return(0)