# 📊 Análise de Dados de Vendas Simples

Este é o meu primeiro projeto de Ciência de Dados no GitHub! 

O objetivo deste script em Python é demonstrar conceitos básicos de manipulação de dados e visualização usando as bibliotecas mais famosas da área.

## 🛠️ Tecnologias Utilizadas
* **Python**
* **Pandas** (para criação e manipulação do DataFrame)
* **Matplotlib** (para a geração do gráfico)

## 🚀 O que o código faz?
1. Gera um conjunto de dados fictícios de vendas e custos mensais.
2. Calcula automaticamente o lucro de cada mês.
3. Exibe um resumo no terminal.
4. Gera um gráfico de linhas comparando Vendas e Custos e o salva como imagem (`grafico_vendas.png`).

---
*Desenvolvido por Juliano Hugo Barbosa*



import pandas as pd
import matplotlib.pyplot as plt

# 1. Criação de um conjunto de dados fictício de vendas
dados = {
    'Mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'],
    'Vendas': [1500, 2200, 1800, 2500, 3000, 2800],
    'Custos': [800, 1100, 900, 1200, 1500, 1400]
}

df = pd.DataFrame(dados)

# 2. Criando uma nova coluna de Lucro
df['Lucro'] = df['Vendas'] - df['Custos']

print("Resumo dos Dados de Vendas do Primeiro Semestre:")
print(df)
print("\nLucro Total no Semestre: R$", df['Lucro'].sum())

# 3. Gerando um gráfico de Vendas vs Custos
plt.figure(figsize=(10, 5))
plt.plot(df['Mês'], df['Vendas'], label='Vendas', marker='o', color='blue')
plt.plot(df['Mês'], df['Custos'], label='Custos', marker='x', color='red')

plt.title('Análise de Vendas e Custos - 1º Semestre')
plt.xlabel('Meses')
plt.ylabel('Valor (R$)')
plt.legend()
plt.grid(True)

# Salva o gráfico como imagem
plt.savefig('grafico_vendas.png')
print("Gráfico gerado com sucesso e salvo como 'grafico_vendas.png'.")
