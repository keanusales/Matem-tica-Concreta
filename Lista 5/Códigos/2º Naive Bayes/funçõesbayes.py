def openarch(arquivo):
  import csv
  with open(arquivo, encoding = "utf-8") as file:
    tabela = list(csv.reader(file, delimiter = ","))
    del tabela[0]
    for linha in tabela:
      for i in range(len(linha)):
        linha[i] = float(linha[i])
    return tabela

def countclasses(tabela):
  classes, limit = {}, int(len(tabela)*0.7)
  for linha in tabela:
    if linha[-1] in classes: classes[linha[-1]] += 1
    else: classes[linha[-1]] = 1
    if tabela.index(linha) == limit: break
  return classes

def standaverage(tabela, classes):
  p = len(tabela[0]) - 1
  limit = int(len(tabela)*0.7)
  keys = list(classes.keys())
  class1, class2 = 0, 0
  for linha in tabela:
    if linha[p] == keys[0]:
      for i in range(p): class1 += linha[i]
    else:
      for i in range(p): class2 += linha[i]
    if tabela.index(linha) == limit: break
  class1 = class1/classes[keys[0]]
  class2 = class2/classes[keys[1]]
  return class1, class2

def classvariance(tabela, classes):
  p = len(tabela[0]) - 1
  limit = int(len(tabela)*0.7)
  keys = list(classes.keys())
  class1, class2 = standaverage(tabela, classes)
  var1, var2 = 0, 0
  for linha in tabela:
    if linha[p] == keys[0]:
      for i in range(p):
        var1 += (linha[i] - class1)**2
    else:
      for i in range(p):
        var2 += (linha[i] - class2)**2
    if tabela.index(linha) == limit: break
  var1 = var1/classes[keys[0]]
  var2 = var2/classes[keys[1]]
  return var1, var2

def corebayes(tabela):
  from math import log10, pi, e
  acertos, erros, saida = 0, 0, []
  p = len(tabela[0]) - 1
  limit = int(len(tabela)*0.7)
  for linha in tabela:
    classes = countclasses(tabela)
    keys = list(classes.keys())
    if tabela.index(linha) > limit:
      total, soma1, soma2 = 0, 0, 0
      class1, class2 = standaverage(tabela, classes)
      var1, var2 = classvariance(tabela, classes)
      defdev1, defdev2 = var1**0.5, var2**0.5
      for i in classes: total += classes[i]
      soma1 = log10(classes[keys[0]]/total)
      soma2 = log10(classes[keys[1]]/total)
      if linha[p] == keys[0]:
        for i in range(p):
          parte1 = -(((linha[i]-class1)**2)/(2*var1))
          parte2 = defdev1*((2*pi)**0.5)
          soma1 += log10((e**parte1)/parte2)
      else:
        for i in range(p):
          parte1 = -(((linha[i]-class2)**2)/(2*var2))
          parte2 = defdev2*((2*pi)**0.5)
          soma2 += log10((e**parte1)/parte2)
      i = tabela.index(linha) + 1
      if soma1 > soma2: saida.append(keys[0])
      else: saida.append(keys[1])
      if saida[-1] == linha[p]: acertos += 1
      else: erros += 1
  return acertos, erros, saida