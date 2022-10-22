def visualizacao_previsao_auto_arima(serie,serie3,residuos_auto,resultado_auto, periodo ):
     import matplotlib.pyplot as plt
     import pandas as pd
     import pickle

     plt.plot(serie3, color ='blue', label='Série real')
     plt.plot(serie3-residuos_auto(),color ='green', label='Residuo_AutoARIMA')
     plt.legend(loc ='best')
     plt.title('Comparativo Série e Residuo_AutoARIMA')
     plt.xlabel('Anos')
     plt.savefig('serie_e_residuo.png', dpi =300, format ='png')
     plt.show()
     previsao_auto =resultado_auto.predict(n_periods= periodo)
     
     previsao_auto_escala = pd.DataFrame((previsao_auto)**3, columns= ['Previsao_AUTO_ARIMA'])
     pd.concat([serie,previsao_auto_escala], names=['Series real', 'Previsao_AUTO_ARIMA']).plot()
     plt.legend(loc ='best')
     plt.title('Cenário preditivo')
     plt.xlabel('Anos')
     plt.ylabel('Indice Pluviometrico mm')
     plt.savefig('cenario_preditivo.png', dpi =300, format ='png')
     plt.show()
     
     # Open a file and use dump()
     with open('previsao_auto_arima.pkl', 'wb') as arquivo:
         # A new file will be created
          pickle.dump(previsao_auto_escala,arquivo)
     return(previsao_auto_escala)


