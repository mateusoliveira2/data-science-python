#coding: utf-8
# Visualizacao de dados em Python

import matplotlib.pyplot as plt 

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 5]

title = "Scatterplot: grafico de dispercao"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(title)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label = "Meus pontos", marker = "H", s = 50,   color = "red")
plt.plot(x, y, linestyle = "--", color = "black")
plt.legend()
plt.show()