#!/src/bin/python
PI = 3.14155926535897931159979634685441852
import sys
def aproximacion(n):
  n = int n
  if (n!=0):
    suma = 0
    for i in range(1,n+1):
      xi = (i - (1/2)) / float(n)
      f_xi = 4 / (1 + xi**2)
      b = i / float(n)
      a = b - (1 / float(n))
      suma = suma + f_xi
    pi = suma/n
    return pi
    
if __name__ == "__main__":
  
 if(len(sys.argv)==3):
   n = int(sys.argv[1])
   m = int(sys.argv[2])
   
   
 else:
   print'La forma de uso es: "modulo.py, n, m", por lo que se utilizaran los valores por defecto'
   n = 10
   m = 10
 
 lista = []

 for j in range(1,m+1):
   pi = aproximacion(j*m)
   lista = lista + [pi]
 print lista
 
 for z in range(0, m):
   npi = lista[z]
   dif =  PI - npi
 print ' PI35DT: %.35f lista: %f PI35DT-lista: %f ' % (PI,npi,dif)

