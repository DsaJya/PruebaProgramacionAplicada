#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde'] #Se declara la lista junto con sus elementos
#input()
print(my_lista) #Muestra la lista
print(type(my_lista)) #Muestra el tipo de dato, en este caso una lista
print(my_lista[2]) #Muestra el elemento número 2 (Sabiendo que se cuenta desde 0: 0,1,2...))

print("my_lista size: ", len(my_lista)) #Len sirve para determinar el número de objetos que hay en la lista en vez de usar el "for"
print(my_lista[0:2])#Muestra elementos de un rango de numeros de la lista, en este caso, del elemento 0 al elemento 2
print(my_lista[:2])#Muestra los elementos de un rango de numeros a partir del elemento 0 

my_lista.append('Blanco')    #Agrega elemento al final de la lista, en este caso un string 
print(my_lista) #Muestra la lista Actual 

my_lista.insert(3, 'Negro') #Agrega un elemento a la lista, pero denota la posición a añadir
print(my_lista)#Muestra la lista Actual 


my_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
print(my_lista)#Muestra la lista Actual 

print(my_lista.index('Azul')) #Se encarga de buscar el primer elemento de la lista, en este caso, "Azul" y muestra su posición

#my_lista.remove('Magenta')
my_lista.remove('Marron') #Elimina un elemento de la lista 
print(my_lista) #Muestra la lista Actual 

my_lista.insert(8, 'Marron') #Agrega un elemento a la lista, pero denota la posición a añadir
print(my_lista)#Muestra la lista Actual 
print(my_lista.pop()) #Se elimina el ultimo elemento de la lista y se muestra (Se puede especificar la posición)
size = len(my_lista) #Declara la variable que será el tamaño de la lista
print("size = ", size) #Muestra el tamaño de la lista
#print(my_lista.pop(size))

my_lista_3 = my_lista*3 #Declara una nueva lista que será tres veces la primera lista
print("my_lista_3: ", my_lista_3) #Muestra la lista triple 

print("Sort:") 
print()
my_listaSort = my_lista.sort() #Declara una nueva lista la cual ordenará los elementos en orden ascendente (numeros) o segun el tamaño de palabras
print(my_listaSort) #Muestra la lista ordenada

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1] #Declara una lista solo con numeros
print("Ordering my_NumList: ")#
my_NumList.sort()#Ordena los numeros en la lista 
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList)



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista) #declara una Tupla 
print()
print()
print("my_tuple: ", my_tupla) #Muestra la tupla actual

print(my_tupla[0])#Muestra elemento en la posicion 0 de la Tupla
print(my_tupla[2])#Muestra elemento en la posicion 2 de la Tupla


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)