import json

# Carregando o Json
with open("dados.json", encoding='utf=8') as f:
    dados = json.load(f)
 
# Criação da lista com os valores de faturamento diário
faturamento_diario = [dia['valor'] for dia in dados]

    
# Calcular o menor e o maior valor de faturamento diário
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

# Calcular a média mensal de faturamento, desconsiderando os dias sem faturamento
dias_com_faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Calculo do número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

# Mostrando os resultados
print(f"Menor valor de faturamento diário: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento diário: R$ {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
