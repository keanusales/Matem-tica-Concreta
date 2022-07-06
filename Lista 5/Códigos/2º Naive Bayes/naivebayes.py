import os, funçõesbayes as ftn
os.system("cls||clear")
vector1 = []
tabela = ftn.openarch("dataset02.csv")
limit = int(len(tabela)*0.7) + 1
for i in range(limit, len(tabela)):
  vector1.append(tabela[i][-1])
acertos, erros, vector2 = ftn.corebayes(tabela)
print(f"Acertos - {acertos} | Erros - {erros}")
equa1, equa0, diff1, diff0 = 0, 0, 0, 0
for i in range(len(vector1)):
  if vector1[i] == 1:
    if vector1[i] == vector2[i]: equa1 += 1
    else: diff1 += 1
  else:
    if vector1[i] == vector2[i]: equa0 += 1
    else: diff0 += 1
equa1, equa0 = str(equa1).center(7), str(equa0).center(7)
diff1, diff0 = str(diff1).center(7), str(diff0).center(7)
print(f"""
Real/Predição | 1 - Pred. | 0 - Pred.
   1 - Real   |  {equa1}  |  {diff1}
   0 - Real   |  {diff0}  |  {equa0}
""")