#¡Bienvenido al reto de programación!
#Nombre del Reto: Sumasw
#En este desafío, deberás implementar una función en el lenguaje de tu preferencia, que reciba dos números enteros, los sume 
#y devuelva un mensaje indicando el resultado.

#Descripción del Reto
#Tu tarea es implementar una función sumarNumeros(a, b) que:

#Verifique que ambos parámetros a y b sean números enteros.
#Si alguno de los parámetros no es un número entero, la función debe retornar el mensaje: "Ambos parámetros deben ser números enteros.".
#Si ambos parámetros son válidos, debe sumar los dos números y retornar un string con el siguiente formato: 
#"El resultado de la suma es: Resultado SW", donde Resultado es la suma de a y b y "SW" son las iniciales.

def sumarNumero(a,b):
    if type(a) == int and type (b) == int: #Verificacion de numeros enteros
        suma=a+b #la suma
        return f"El resultado de la suma es: {suma} SW" #Return del string
    else: #Si alguno no es un entero
        return "Ambos parámetros deben ser números enteros."

print("***Casos Válidos***")  #Comprobacion con valores de git
print(sumarNumero(5,3)) 
print(sumarNumero(-10,4))
print(sumarNumero(0,0))
print(sumarNumero(123,877))

print("\n***Casos Inválidos***")
print(sumarNumero(5.5,2))
print(sumarNumero("10",5))
print(sumarNumero(8,None))
print(sumarNumero(True,3))
print(sumarNumero([],{}))