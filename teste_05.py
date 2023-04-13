# Entrada de dados
entrada = input("Digite uma palavra ou frase: ")

str_invertida = ""

for i in range(len(entrada)-1, -1, -1):
    str_invertida += entrada[i]

print("A string invertida é:", str_invertida)