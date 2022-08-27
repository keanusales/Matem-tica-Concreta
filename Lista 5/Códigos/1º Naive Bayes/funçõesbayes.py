def openarch(arquivo):
  import csv
  with open(arquivo, encoding = "utf-8") as file:
    tabela = list(csv.reader(file, delimiter = ","))
    del tabela[0]
    return tabela

def countclasses(tabela):
  classes = {}
  for linha in tabela:
    if linha[-1] in classes: classes[linha[-1]] += 1
    else: classes[linha[-1]] = 1
  del classes[""]
  return classes

def countypes(tabela, classes):
  class1, class2, totais = [], [], []
  p = len(tabela[0]) - 1
  keys = list(classes.keys())
  for i in range(p):
    class1.append({}); class2.append({}); totais.append({})
  class1.append(keys[0]); class2.append(keys[1])
  for linha in tabela:
    if linha[-1] in classes:
      for i in range(p):
        if linha[i] in totais[i]: totais[i][linha[i]] += 1
        else: totais[i][linha[i]] = 1
      if linha[-1] == keys[0]:
        for i in range(p):
          if linha[i] in class1[i]: class1[i][linha[i]] += 1
          else: class1[i][linha[i]] = 1
      else:
        for i in range(p):
          if linha[i] in class2[i]: class2[i][linha[i]] += 1
          else: class2[i][linha[i]] = 1
  for i in range(len(totais)): totais[i] = len(totais[i])
  return class1, class2, totais

def corebayes(tabela):
  from math import log10
  p = len(tabela[0]) - 1
  for linha in tabela:
    classes = countclasses(tabela)
    if linha[p] not in classes:
      total, soma1, soma2 = 0, 0, 0
      class1, class2, totais = countypes(tabela, classes)
      for i in classes: total += classes[i]
      soma1 = log10(classes[class1[-1]]/total)
      soma2 = log10(classes[class2[-1]]/total)
      for i in range(p):
        if linha[i] in class1[i]:
          parte1 = class1[i][linha[i]] + 1
          parte2 = classes[class1[-1]] + totais[i]
          soma1 += log10(parte1/parte2)
        else:
          parte2 = classes[class1[-1]] + totais[i]
          soma1 += log10(1/parte2)
        if linha[i] in class2[i]:
          parte1 = class2[i][linha[i]] + 1
          parte2 = classes[class2[-1]] + totais[i]
          soma2 += log10(parte1/parte2)
        else:
          parte2 = classes[class2[-1]] + totais[i]
          soma2 += log10(1/parte2)
      soma1, soma2 = 10**soma1, 10**soma2
      i, total = tabela.index(linha) + 1, soma1 + soma2
      soma1, soma2 = soma1/total, soma2/total
      print(f"Probabilidade de ser {class1[-1]}: {soma1}")
      print(f"Probabilidade de ser {class2[-1]}: {soma2}")
      linha[p] = class1[-1] if soma1 > soma2 else class2[-1]
      print(f"O resultado da {i}ª linha é: \"{linha[p]}\".\n")