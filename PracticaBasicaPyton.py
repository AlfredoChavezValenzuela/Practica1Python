'''#1.	Escribir “hola mundo” en python
print("Hola")

#2.	Operaciones Matemáticas
a = 3
b = 7.2
print( a+b ) 

#3.	Bucles
for i in range(10):
	print( "Numero: ",  i )

#4.	Funciones
def miFuncion() :
	print( "Esta es la llamada ") 
miFuncion()

#Librerias
#1.	Para importar numpy debemos usar la siguiente línea:
import numpy as np

#2.	Para iniciar un arreglo
a = np.array([1,3,5,7]) #inicializando un vector
a = type(a)

#3.	Operaciones de numpy:
np.ones( 4 ) # crea un vector horizontal de tamaño 4 con todos los elementos en 1
np.ones((3,4)) # crea una matriz de tamaño 3x4. Fíjese que recibe una tupla
np.arange( 10 ) # crea un vector horizontal con elementos del 0 al 9
np.arange( 1,10 ) # crea un vector horizontal con elementos del 1 al 10
np.arange( 1,10,2 ) # crea un vector horizontal con elementos impares del 1 al 10
np.random.rand(3,4) # crea una matriz(3x4) con valores aleatorios entre 0 y 1.

#4.	Atributos de los objetos numpy:
x = np.ones( 4 ) 
x.ndim # retornará 1 porque el vector x posee 1 dimensión

#shape retornará una tupla indicando el tamaño del vector o matriz
#size retornará el total de elementos en la matriz o vector
#dtype retornará el tipo de dato del objeto
#Además, la función reshape podrá redefinir el tamaño del vector o matriz, por ejemplo:

x = np.ones(100)
x.reshape(2,5)

#5.	Indexación (recordar que los índices comienzan en 0).
x[4:10] #mostrará los elementos del 4 al 10 de x.
x[4:] #mostrará los elementos del 4 hasta el final
x[4,:] #mostrará solo la fila 4
x[:4] #mostrará las filas hasta la 4
x[:,4] #mostrará la columna de 4

6#.	Operaciones matemáticas.
x+5 #adicionará la constante 5 a todos los elementos de x
x + np.array([1,2,3]) #adicionará el vector [1,2,3] si x tiene 3 columnas
x * y #realizará una multiplicación uno a uno
np.dot(x,y) #realizará una multiplicación cruzada



#1.	Importar la libreria
import pandas as pd

#2.	
personas = {
 "peso": pd.Series([68, 83, 112], index = ["maria", "mario", "memo"]),
 "cumpleanhos": pd.Series([1994, 1995, 2002], index = ["mario", "maria", "memo"], name = "anho"),
 "hijos": pd.Series([0, 3], index = ["memo", "mario"]),
 "actividades": pd.Series(["Biking", "Dancing"], index = ["maria", "mario"]),
}

#3.	
persona = pd.DataFrame(personas)
persona # muestra
persona[persona["cumpleanhos"] < 2000]

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10,10,0.1)
y = x**2

plt.plot(x,y)
plt.show()

#Problema 1: 1.	Calcular fibonacci de ( n ) elevando la matriz [[1 1],[1,0]] a la potencia n-1

import numpy as np
n=8
x = np.array([ [1,1],
               [1,0] ])
y = np.linalg.matrix_power(x, (n-1))
print(y[0][0])'''

import pandas as pd
datos=pd.read_excel('D:/Gestion de sistemas de la informacion/MODULO3/Diseño web back end/cara.xlsx',header=None)
#print(datos)

import matplotlib.pyplot as plt
import numpy as np

x = np.array(datos)

plt.figure(figsize=(50,50))
plt.imshow(x)
plt.show()