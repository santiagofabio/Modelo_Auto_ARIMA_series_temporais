def  modelo_arma(serie3,serie): 
      import matplotlib.pyplot as plt
      from statsmodels.tsa.arima.model import ARIMA
      from matplotlib.pylab import rcParams
      rcParams['figure.figsize'] =[15,6]
      import pickle
      import pandas as pd
      

      modelo_arma = ARIMA(serie3, order=(10,0,2))
      resultado_arma = modelo_arma.fit()
      print(resultado_arma.summary())
      residuos_modelo_arma =resultado_arma.resid
      plt.plot(serie3,color ='blue', label ='Serie cúbica') 
      plt.plot(serie3-residuos_modelo_arma, color= 'green', label ='Residuos-arma')
      plt.xlabel('Anos')
      plt.legend(loc ='best')
      plt.show()
      #Previsão modelo moving_avarage
      resultado_arma.fittedvalues
      previsao_modelo_arma =resultado_arma.predict(start =431, end =443)
      
      plt.plot(serie3, color = 'blue', label ='Serie real' )
      plt.plot(previsao_modelo_arma, color ='orange', marker ="^", label = 'Previsão')
      plt.plot(serie3-residuos_modelo_arma, color= 'green', label ='Residuos- arma')
      plt.xlabel('Anos')
      plt.title('Serie transfomada  e previsao modelo arma')
      plt.legend(loc ='best')
      plt.savefig('comparativo_serie_residuo__arma_previsao_.png', format ='png', dpi=300)
      plt.show()
 
      
      
      previsao_modelo_arma_escala = previsao_modelo_arma**3
      lista =[]
      for numero  in previsao_modelo_arma_escala:
             lista.append(numero)   
      
      prev_escala = pd.DataFrame(   lista, columns=['Previsão_Arma'])
      
     
      
      
      
      
      plt.plot(serie, color = 'blue', label ='Serie real' )
      plt.plot(previsao_modelo_arma_escala, color ='orange', marker ="^", label ='Previsao Modelo ARMA')
      plt.xlabel('Anos')
      plt.title('Serie real e previsao modelo -ARMA ')
      plt.legend(loc ='best')
      plt.savefig('previsao_arma.png', format ='png', dpi=300)
      plt.show()
      
      with open('previsao_modelo_arma_escala.pkl', 'wb') as arquivo:
    #      A new file will be created
           pickle.dump(prev_escala,arquivo)
      
      return(0)

