def metricas_previsoes(valores_reais,prev_auto_arima,prev_autoregressivo,prev_arma,prev_moving_average,prev_arima):
     import pandas as pd
     from sklearn.metrics import mean_absolute_error,mean_squared_error
     
     #------------METRICAS----------------------------------
     prev_auto_arima_validacao =prev_auto_arima.iloc[0:4]  
     prev_autoregressivo_validacao =prev_autoregressivo.iloc[0:4]
     prev_arima_validacao =prev_arima.iloc[0:4]
     prev_arma_validacao =prev_arma.iloc[0:4]
     prev_moving_validacao =prev_moving_average.iloc[0:4]
     desempenho =pd.concat([valores_reais,prev_auto_arima_validacao,prev_autoregressivo_validacao,prev_arima_validacao,prev_arma_validacao,prev_moving_validacao], axis =1)
     print(desempenho.columns)
   
     
     print('-----------------MEAN ABSOLUT ERROR-----------------------')
     mae_auto_arima =mean_absolute_error(desempenho['Valores reais'],desempenho['Previsao_AUTO_ARIMA']    )
     print('Meam absolut error AUTO_ARIMA:  {:.4f}'.format(mae_auto_arima) )
     
     mae_arima =mean_absolute_error(desempenho['Valores reais'],desempenho['Previsão_Arima']    )
     print('Meam absolut error ARIMA:  {:.4f}'.format(mae_arima ))
     
     mae_moving_average =mean_absolute_error(desempenho['Valores reais'],desempenho['Previsão_Moving_Average']    )
     print('Meam absolut error Moving Average:  {:.4f}'.format(mae_moving_average ))
     
     mae_arma =mean_absolute_error(desempenho['Valores reais'],desempenho['Previsão_Arma']    )
     print('Meam absolut error ARMA:  {:.4f}'.format(mae_arma ))
     
     mae_autoregressivo =mean_absolute_error(desempenho['Valores reais'],desempenho['Previsão_Auto regressivo']    )
     print('Meam absolut error AUTOREGRESSIVO:  {:.4f}'.format(mae_autoregressivo))
     
     print('--------------------------------------------------')
     
     
     print('-----------------MEAN SQUARED ERROR-----------------------')
     mae_auto_arima =mean_squared_error(desempenho['Valores reais'],desempenho['Previsao_AUTO_ARIMA']    )
     print('Meam squared error AUTO_ARIMA:  {:.4f}'.format(mae_auto_arima) )
     
     mae_arima =mean_squared_error(desempenho['Valores reais'],desempenho['Previsão_Arima']    )
     print('Meam squared error ARIMA:  {:.4f}'.format(mae_arima ))
     
     mae_moving_average =mean_squared_error(desempenho['Valores reais'],desempenho['Previsão_Moving_Average']    )
     print('Meam squared error Moving Average:  {:.4f}'.format(mae_moving_average ))
     
     mae_arma =mean_squared_error(desempenho['Valores reais'],desempenho['Previsão_Arma']    )
     print('Meam squared error ARMA:  {:.4f}'.format(mae_arma ))
     
     mae_autoregressivo =mean_squared_error(desempenho['Valores reais'],desempenho['Previsão_Auto regressivo']    )
     print('Meam squared error AUTOREGRESSIVO:  {:.4f}'.format(mae_autoregressivo))
     
     print('--------------------------------------------------')
     
     
     print('-----------------MEAN SQRT ERROR-----------------------')
     mae_auto_arima =mean_squared_error(desempenho['Valores reais'],desempenho['Previsao_AUTO_ARIMA'], squared = False  )
     print('Meam SQRT error AUTO_ARIMA:  {:.4f}'.format(mae_auto_arima) )
     
     mae_arima =mean_squared_error(desempenho['Valores reais'],desempenho['Previsão_Arima'] , squared = False   )
     print('Meam SQRT error ARIMA:  {:.4f}'.format(mae_arima ))
     
     mae_moving_average =mean_squared_error(desempenho['Valores reais'],desempenho['Previsão_Moving_Average'], squared = False    )
     print('Meam SQRT error Moving Average:  {:.4f}'.format(mae_moving_average ))
     
     mae_arma =mean_squared_error(desempenho['Valores reais'],desempenho['Previsão_Arma'], squared = False  )
     print('Meam SQRT error ARMA:  {:.4f}'.format(mae_arma ))
     
     mae_autoregressivo =mean_squared_error(desempenho['Valores reais'],desempenho['Previsão_Auto regressivo'], squared = False    )
     print('Meam SQRT error AUTOREGRESSIVO:  {:.4f}'.format(mae_autoregressivo))
     
     print('--------------------------------------------------')
     
     
     
     
     
     
     
    
