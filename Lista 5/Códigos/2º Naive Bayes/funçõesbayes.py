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

def classaverage(tabela, classes):
  p = len(tabela[0]) - 1
  limit = int(len(tabela)*0.7)
  keys = list(classes.keys())
  class1, class2 = [], []
  for i in range(p):
    class1.append(0); class2.append(0)
  for linha in tabela:
    if linha[p] == keys[0]:
      for i in range(p): class1[i] += linha[i]
    else:
      for i in range(p): class2[i] += linha[i]
    if tabela.index(linha) == limit: break
  for i in range(p):
    class1[i] = class1[i]/classes[keys[0]]
    class2[i] = class2[i]/classes[keys[1]]
  return class1, class2

def classvariance(tabela, classes):
  p = len(tabela[0]) - 1
  limit = int(len(tabela)*0.7)
  keys = list(classes.keys())
  class1, class2 = classaverage(tabela, classes)
  varin1, varin2 = [], []
  for i in range(p):
    varin1.append(0); varin2.append(0)
  for linha in tabela:
    if linha[p] == keys[0]:
      for i in range(p):
        varin1[i] += (linha[i] - class1[i])**2
    else:
      for i in range(p):
        varin2[i] += (linha[i] - class2[i])**2
    if tabela.index(linha) == limit: break
  for i in range(p):
    varin1[i] = varin1[i]/classes[keys[0]]
    varin2[i] = varin2[i]/classes[keys[1]]
  return varin1, varin2

def classdeviation(tabela, classes):
  defdev1, defdev2 = [], []
  varin1, varin2 = classvariance(tabela, classes)
  for i in range(len(tabela[0]) - 1):
    defdev1.append(varin1[i]**0.5)
    defdev2.append(varin2[i]**0.5)
  return defdev1, defdev2

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
      class1, class2 = classaverage(tabela, classes)
      varin1, varin2 = classvariance(tabela, classes)
      defdev1, defdev2 = classdeviation(tabela, classes)
      for i in classes: total += classes[i]
      soma1 = log10(classes[keys[0]]/total)
      soma2 = log10(classes[keys[1]]/total)
      if linha[p] == keys[0]:
        for i in range(p):
          parte1 = -(((linha[i]-class1[i])**2)/(2*varin1[i]))
          parte2 = defdev1[i]*((2*pi)**0.5)
          soma1 += log10((e**parte1)/parte2)
      else:
        for i in range(p):
          parte1 = -(((linha[i]-class2[i])**2)/(2*varin2[i]))
          parte2 = defdev2[i]*((2*pi)**0.5)
          soma2 += log10((e**parte1)/parte2)
      if soma1 > soma2: saida.append(keys[0])
      else: saida.append(keys[1])
      if saida[-1] == linha[p]: acertos += 1
      else: erros += 1
  return acertos, erros, saida