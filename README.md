## **Modelo da séries temporais**
##  *Auto_Arima*

 **Objetivo*** Automatically discover the optimal order for an ARIMA model.  The auto-ARIMA process seeks to identify the most optimal parameters for an ARIMA model, settling on a single fitted ARIMA model. This process is based on the commonly-used R function, **forecast::auto.arima**

 ## Modelo Uitlizado

 - **pmdarima.arima.auto_arima**

 
 



## Estudo série pluviométrica 

1. Série temporal estudada
![serie_temporal_estudada](serie_temporal_estudada.png)

3. Transformação raíz cubica sobre a série
 
    3.1  Série transformada
![serie_raiz_cubica](serie_raiz_cubica.png )

4. Aplicação Modelo AUTO ARIMA
     
      3.1 Estudo dos resíduos
     ![residuos_modelo_ar](residuo_autoarima.png) 
     
      3.2 Quantile-Quantile Plot-Rediduo -Modelo AR
     ![Quantile-Quantile Plot-Rediduo Série raíz cúbica](normal_qq_residuo_autoarima.png) 

      3.3 Autocorrelation Function-Resíduos -Modelo AR.
       ![nomral_qq_plt_serie_raiz_cubica](diagrama_acf_residuo_autoarima.png)

      3.4. Partial Autocorrelation Function -Resíduos- -Modelo AR.
       ![Parcial autocorreção residuos](diagrama_pacf_residuo_autoarima.png)

4. Resultados

     4.1 Série e resíduos
     ![seire_e_residuos](serie_e_residuo.png)

      4.2 Previsão.
      ![previsao_final](cenario_preditivo.png)

## **Análise compartiva de modelos.**
Está sessão tem como objetivorelizar uma análise comparativa dos modelos Autoregressivos, Moving Average,ARMA, ARIMA e Auto_ARIMA,  através das métricas erros.

* Previsão Modelo Autoregressivo
  
  ![previsao_final_autoregressivo](previsao_autoregressivo.png)

* Previsão Modelo Moving Average
 
  ![previsao_final_moving_average](previsao_moving_avarage.png)
* Previsão Modelo ARMA
 
  ![previsao_final_arma](previsao_arma.png)

* Previsão Modelo ARIMA
   
    ![previsao_final_arima](previsao_arima.png)

### Validação/Métricas

### _Mean abslout error_
Modelo | Mean abslout error
-----------|---------------
Auto arima |   53.2494
Arima  |98.1856
Moving Average|  109.5696
Arma | 68.0473
Auto regressivo| 72.0368


### _Mean squared error_
Método |Mean squared error
-----------|--------------
Auto arima|  3327.0952
Arima | 14587.1759
Moving average|  18852.7186
Arma|  7244.2779
Auto regressivo|  8271.8396


### _Mean sqrt error_

Método|Mean sqrt error
-------|-----------------
Auto arima|  57.6810
Arima| 120.7774
Moving average|137.3052
Arma| 85.1133
Auto regressivo| 90.9497


