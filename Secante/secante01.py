import math

def f(x):
  return 4*math.exp(x)-math.cos(x)-1.1

def flinha(x):
  return 4*math.exp(x) + math.sin(x)

def secante(a,b,erro,interacao = 0):
  interacao +=1
  c = -( b*f(a) - a*f(b) ) / ( f(b) - f(a) )
  if abs(f(c)) < abs(erro) :
    print(c)
    print(f(c))
    print(interacao)
    return
  print(f(c))
  secante(b,c,erro,interacao)

secante(0,1,0.0001)