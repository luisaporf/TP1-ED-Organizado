import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

plt.switch_backend('Agg')

dados = pd.read_csv('resultados.csv')

num_algoritmos = 13
num_pontos = 260

parametros = ["tamanho", "tempo", "comparacoes", "movimentacoes", "chamadas"]
parametros_colunas = [6, 8, 10, 12, 14]

for param, coluna_idx in zip(parametros, parametros_colunas):

    for i in range(num_algoritmos):
        inicio = i * num_pontos
        fim = (i + 1) * num_pontos
        
        # Extrair os dados da coluna correspondente ao parâmetro atual
        coluna = dados.iloc[inicio:fim, coluna_idx].values.astype(float)

        # Plotar o gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(np.arange(1, num_pontos + 1), coluna)
        plt.xlabel('Índice')
        plt.ylabel(param)
        plt.title(f'Algoritmo {i+1}')
        plt.grid(True)
        
        if param == "tamanho":
            save_dir = os.path.join('imagens', 'tamanho')
        elif param == "tempo":
            save_dir = os.path.join('imagens', 'tempo')
        elif param == "comparacoes":
            save_dir = os.path.join('imagens', 'comparacoes')
        elif param == "movimentacoes":
            save_dir = os.path.join('imagens', 'movimentacoes')
        elif param == "chamadas":
            save_dir = os.path.join('imagens', 'chamadas')
        
        plt.savefig(os.path.join(save_dir, f'algoritmo_{i+1}.png'))          
        plt.close()