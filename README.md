
#Modelo da séries temporais -Auto_Arima
 **Objetivo*** Automatically discover the optimal order for an ARIMA model.  The auto-ARIMA process seeks to identify the most optimal parameters for an ARIMA model, settling on a single fitted ARIMA model. This process is based on the commonly-used R function, **forecast::auto.arima**

 ## Modelo Uitlizado

 - **pmdarima.arima.auto_arima**

 
 



### Série temporal estudada
1. Série temporal
![serie_temporal_estudada](serie_temporal_estudada.png)

2. Transformação raíz cubica sobre a série
2.1 Série transformada
![serie_raiz_cubica](serie_raiz_cubica.png )

3. Aplicação Modelo AUTO ARIMA
3.1 Estudo dos resíduos
![residuos_modelo_ar](residuo_autoarima.png)

3.2 Quantile-Quantile Plot-Rediduo -Modelo AR
![Quantile-Quantile Plot-Rediduo Série raíz cúbica](normal_qq_residuo_autoarima.png) 

3.3 Autocorrelation Function-Resíduos -Modelo AR.
![nomral_qq_plt_serie_raiz_cubica](diagrama_acf_residuo_autoarima.png)

3.4. Partial Autocorrelation Function -Resíduos- -Modelo AR.
![Parcial autocorreção residuos](diagrama_pacf_residuo_autoarima.png)

4 Resultados

4.1 Série e resíduos
![seire_e_residuos](serie_e_residuo.png)


4.1 Previsão.
![previsao_final](cenario_preditivo.png)