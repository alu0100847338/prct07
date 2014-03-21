#!/src/bin/python

import modulo
t_upla=(1e1,1e2,1e3,1e4,1e5,1e6,1e7)
lista = []
def mostrar(lista):
  for l in range(0, m):
    dif = modulo.PI-l
   print ' PI35DT: %.35f lista: %f PI35DT-lista: %f ' % (modulo.PI,l,dif)
for i in t_upla:
  y = modulo.aproximacion(i)
  lista = lista + [y]

mostrar(lista)

#El numero maximo de elementos de la t_upla es 7.
#Al introducir el elemento 100000000  se producen errores de memoria.
#Los elementos de la t_upla no se pueden definir en notación cientifica.
#La expresion .pyc es el acronimo de "Copiled Python script file".