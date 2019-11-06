
arreglo = [12,4,2,1]

def multiplicacion(lista):
    
    pivote = 1
    for i in range(len(lista)): 

        resultado = pivote*lista[i]
        pivote = resultado

    print("Resultado: " + str(resultado))

multiplicacion(arreglo)
