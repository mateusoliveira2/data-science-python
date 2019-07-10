#coding: utf-8
# Crescimento da população brasileira (1980 - 2016)
# DataSus

import matplotlib.pyplot as plt 
dados = open("populacao-brasileira.csv").readlines()
anos = []
pop = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        anos.append(int(linha[0]))
        pop.append(int(linha[1]))

plt.plot(anos, pop, linestyle = "--")
plt.bar(anos, pop, color = "#e4e4e4")

# Legendas
plt.title("Crescimento da populacao brasileira (1980 - 2016)")
plt.xlabel("ano")
plt.ylabel("populacao x 100.000.000 ")

plt.show()