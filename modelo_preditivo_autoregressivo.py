def modelo_preditivo_autoregressivo(serie3,serie):
      import matplotlib.pyplot as plt
      from statsmodels.tsa.arima.model import ARIMA
      from matplotlib.pylab import rcParams
      import pickle
      import pandas as pd
      rcParams['figure.figsize'] =[15,6]

      modelo_ar = ARIMA(serie3, order=(9,0,0))
      resultado_ar = modelo_ar.fit()
      print(resultado_ar.summary())
      residuos_modelo_ar =resultado_ar.resid
      plt.plot(serie3, label ="Série Real", color ='blue') 
      plt.plot(serie3-residuos_modelo_ar, color= 'green', label ='Residuos-AutoRegressivo')
      plt.legend(loc ='best')
      plt.show()
      #Previsão modelo AR
      resultado_ar.fittedvalues
      previsao_modelo_ar =resultado_ar.predict(start =431, end =443)
      plt.plot(serie3, color = 'blue', label ='Serie real' )
      plt.plot(previsao_modelo_ar, color ='orange', marker ="^", label = 'Previsao autoregressivo')
      plt.plot(serie3-residuos_modelo_ar, color= 'green', label ='Residuos-AutoRegressivo')
      plt.xlabel('Anos')
      plt.title('Serie transformada e previsao AutoRegressivo')
      plt.legend(loc ='best')
      plt.savefig('comparativo_serie_residuo_previsao_autoregressivo.png', format ='png', dpi=300)
      plt.show()
 
      
      previsao_modelo_ar_escala =pd.DataFrame(previsao_modelo_ar**3, columns=['AutoRegressivo'] )
      plt.plot(serie, color = 'blue', label ='Serie real' )
      plt.plot(previsao_modelo_ar_escala, color ='orange', marker ="^", label ='Previsao-AutoRegressivo')
      plt.xlabel('Anos')
      plt.ylabel('Indíce pluviimétrico em mm')
      plt.title('Serie e previsao modelo AutoRegressivo')
      plt.legend(loc ='best')
      plt.savefig('previsao_autoregressivo.png', format ='png', dpi=300)
      plt.show()
     
      # Open a file and use dump()
      with open('previsao_modelo_ar_escala.pkl', 'wb') as arquivo:
    #      A new file will be created
            pickle.dump(previsao_modelo_ar_escala,arquivo)
     
      return(0)

