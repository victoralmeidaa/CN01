import math

def f(x):
  return 4*math.exp(x)-math.cos(x)-1.1

def flinha(x):
  return 4*math.exp(x) + math.sin(x)

def newton(x0,erro,interacao = 0):
  interacao +=1
  x1 = x0-f(x0)/flinha(x0)
  if abs(f(x1)) < abs(erro):
    print(x1)
    print(f(x1))
    print(interacao)
    return
  print(f(x1))
  newton(x1,erro,interacao)

newton(-1,0.0001)