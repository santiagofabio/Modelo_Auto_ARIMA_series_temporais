def  modelo_moving_avarage(serie3,serie): 
      import matplotlib.pyplot as plt
      from statsmodels.tsa.arima.model import ARIMA
      from matplotlib.pylab import rcParams
      import pandas as pd
      import pickle
      rcParams['figure.figsize'] =[15,6]

      modelo_ma = ARIMA(serie3, order=(0,0,8))
      resultado_ma = modelo_ma.fit()
      print(resultado_ma.summary())
      residuos_modelo_ma =resultado_ma.resid
      plt.plot(serie3, label ="Série Real", color ='blue') 
      plt.plot(serie3-residuos_modelo_ma, color= 'green', label ='Residuos-moving_avarage')
      plt.title('Serie e resíduo moving_avarage')
      plt.legend(loc ='best')
      plt.show()
      #Previsão modelo moving_avarage
      resultado_ma.fittedvalues
      previsao_modelo_ma =resultado_ma.predict(start =431, end =443)
      plt.plot(serie3, color = 'blue', label ='Serie real' )
      plt.plot(previsao_modelo_ma, color ='orange', marker ="^", label = 'Previsao moving_avarage')
      plt.plot(serie3-residuos_modelo_ma, color= 'green', label ='Residuos-moving_avarage')
      plt.xlabel('Anos')
      plt.title('Comparativo serie e previsao modelo moving_avarage')
      plt.legend(loc ='best')
      plt.savefig('comparativo_serie_residuo_moving_avarage_previsao_.png', format ='png', dpi=300)
      plt.show()
       
      previsao_modelo_ma_escala = previsao_modelo_ma**3
      
      
      lista =[]
      for numero  in previsao_modelo_ma_escala :
             lista.append(numero)   
      
      prev_escala = pd.DataFrame( lista, columns=['Previsão_Moving_Average'])
   
      
      plt.plot(serie, color = 'blue', label ='Serie real' )
      plt.plot(previsao_modelo_ma_escala, color ='orange', marker ="^", label ='Previsao Modelo-moving_avarage')
      plt.xlabel('Anos')
      plt.ylabel('Indíce pluviometrico em mm')
      plt.title('Comparativo serie e previsao modelo ')
      plt.legend(loc ='best')
      plt.savefig('previsao_moving_avarage.png', format ='png', dpi=300)
      plt.show()
      
      # Open a file and use dump()
      with open('previsao_modelo_moving_average.pkl', 'wb') as arquivo:
    #      A new file will be created
            pickle.dump(prev_escala,arquivo)
            
      return(0)

