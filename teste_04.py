# Criação de um dicionario de dados do faturamento por estado
fat_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calculo do faturamento total e dos percentuais por estado
fat_total = sum(fat_por_estado.values())
percent_por_estado = {
    estado: (valor / fat_total) * 100 for estado, valor in fat_por_estado.items()
    }
# Mostrando o resultado
for estado, percent in percent_por_estado.items():
    print("{}: {:.2f}%".format(estado, percent))
