# Calculadora de consumo elétrico inteligente
# Autor: lauratarantini

# Entrada
nome_aparelho = input("Qual é o nome do aparelho que será calculado? ")
potencia_aparelho = float(input("Qual a potência do aparelho em watts (W)? "))
tempo_uso = float(input("Qual é o tempo médio de uso diário em horas? "))

# Processamento
consumo_mensal = (potencia_aparelho * tempo_uso * 30) / 1000

# Saída
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh por mês")