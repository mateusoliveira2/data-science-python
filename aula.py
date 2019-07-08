#Visualizacao de dados em Python

import matplotlib.pyplot as plt 

x1 = [1, 3, 5, 7, 9]
x2 = [2, 4, 6, 8, 10]
y1 = [2, 3, 7, 1, 5]
y2 = [5, 7, 4, 3, 6]

title = "Meu primeiro grafico com Python"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(title)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x1, y1, label = "Grupo 1")
plt.bar(x2, y2, label = "Grupo 1")
plt.legend()
plt.show()