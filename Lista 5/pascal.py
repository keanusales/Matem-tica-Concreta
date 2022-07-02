import os
from math import comb
os.system("cls||clear")
width = os.get_terminal_size().columns
r = int(input("Digite o valor de r: "))
saida = []; os.system("cls||clear")
for i in range(r+1):
  for j in range(i+1):
    saida.append(str(comb(i, j)))
  print(" ".join(saida).center(width))
  saida.clear()