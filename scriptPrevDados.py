import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Carrega os dados do arquivo excel
df = pd.read_excel('Dados.xlsx')

# Cria o modelo ARIMA
model = ARIMA(df['Vendas'], order=(1,1,1))
model_fit = model.fit()

# Faz a previsão
previsao = model_fit.forecast(steps=5)

# Exibe o resultado
print("Previsão de vendas para os próximos 5 dias:")
print(previsao)