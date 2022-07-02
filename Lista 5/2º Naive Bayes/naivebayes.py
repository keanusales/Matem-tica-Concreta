import os, funçõesbayes as ftn
os.system("cls||clear")
tabela = ftn.openarch("dataset01.csv")
ftn.corebayes(tabela)
print("O resultado final da tabela:")
for linha in tabela:
  i = tabela.index(linha) + 1
  print(f"{i} - {linha}")