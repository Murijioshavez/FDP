#definimos nuestra lista
list = [9,18,9,25,4,1,9,27]
resultado = []
#Encontramos maximo y minimo de la funcion
maximo = max(list)
minimo = min(list)
#Y los metemos en nuestra lista de resultado
resultado.append(minimo)
resultado.append(maximo)
#ahora quitamos el maximo y minimo de la lista, ya que al recorrer no vamos a necesitar
#mas al maximo y minimo porque nos pueden estorbar
list.remove(minimo)
list.remove(maximo)
#<------------------------------------------------------------------------------------>


#definimos la funcion
def ordenar(list):
    
    
#<---------------------------------------------------------------------------------------------------------->
    #recorro los indices de la lista para ver luego donde los vamos a insertar.
    #para ello vamos a recibir 3 parametros como se ve aca abajo, el numero para compararlo
    #con otros valores, la lista resultado y el indice que por default esta en 0.
    def iterar(numero, list, indice = 0):
        #si el elemento en el indice es el mismo que el numero final entonces devolvemos ese indice
        #el cual es el final xd
        if list[indice] == list[-1]:
            return indice
        #si el elemento en el indice es mayor que el numero entonces devolvemos el indice,
        #ya que el numero es menor entonces insertamos el numero detras del indice en esa instancia.
        elif numero < list[indice]:
            return indice
        #si nada de esto se cumple pues pasamos a la siguiente iteracion
        else:
            return iterar(numero, resultado, indice + 1)


#<-------------------------------------------------------------------------------------------------------->
    #cuento cuantas veces aparece cada numero en la lista y lo inserto ese numero de veces.
    #hice la funcion porque si multiplico el numero de inserciones realmente estaria multiplicando
    #enteros, ej: 9 aparece 3 veces, entonces si multiplico 9 por 3, me da 27 sin esta funcion
    def agregar_repetidos(numero, apariciones):
        if apariciones == 0 or apariciones == None:
            return
        else:
            #guardamos el indice donde vamos a insertar el numero en la lista.
            indice = iterar(numero, resultado)
            #append no me deja controlar el indice de donde poner las cosas, entonces
            #mejor uso insert
            resultado.insert(indice, numero)
            agregar_repetidos(numero, apariciones - 1)
#<---------------------------------------------------------------------------------------------------------->

               
    #este condicional es para evitar que el programa se quede en un bucle infinito
    if not list:
        return
    else:
        apariciones = list.count(list[0])
        #si el numero ya esta en la lista pues no hace nada
        if list[0] in resultado:
            pass
        #si el numero no ta en la lista pues lo vamos a meter
        elif list[0] not in resultado:
            #llamamos a la funcion que ya explique.
            agregar_repetidos(list[0], apariciones)
            #llamamos a la recursion
        ordenar(list[1:])
        
#<---------------------------------------------------------------------------------------------------------->

#llamamos a la funcion para que haga lo que deba hacer        
ordenar(list)
