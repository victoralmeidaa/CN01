import math

def f(x):
  return math.log(math.pow(x,2)+1)-math.exp(x)

def flinha(x):
  return 2*x/(math.pow(x,2)+1)-math.exp(x)

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

newton(2,0.0001)