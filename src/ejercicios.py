# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    suma_total = 0
    for fila in matriz:
        for elemento in fila:
            suma_total += elemento
    return suma_total

matriz = [[1, 2], [3, 4]]
resultado = sumar_elementos_matriz(matriz)
print(resultado)

# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
    valor_maximo = float('-inf')  
    for fila in matriz:
        for elemento in fila:
            if elemento > valor_maximo:
                valor_maximo = elemento
    return valor_maximo

matriz = [[1, 2], [3, 4]]
resultado = maximo_matriz(matriz)
print(resultado) 
    

# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
  if n <= 1:
    return False
  
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False

  return True

print(es_primo(7))  
print(es_primo(4))  
    

# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
    """
    Recibe una lista de listas y devuelve la matriz transpuesta.
    Incluir el código aquí para transponer la matriz.
    """
    pass

# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
  pares = []
  for numero in lista:
    if numero % 2 == 0:
      pares.append(numero)
  return pares

numeros = [1, 2, 3, 4, 5, 6]
pares = filtrar_pares(numeros)
print(pares)  
    

# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
  palabras = texto.split()
  return len(palabras)

texto = "Hola Mundo"
cantidad_palabras = contar_palabras(texto)
print(cantidad_palabras)  

# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
  tabla = []
  for i in range(1, 11):
    resultado = n * i
    tabla.append(resultado)
  return tabla

numero = 2
resultado = tabla_multiplicar(numero)
print(resultado)  

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
  contador = 0
  for numero in lista:
    if numero < 0:
      contador += 1
  return contador

numeros = [-1, 0, 1, 2, -3]
negativos = contar_negativos(numeros)
print(negativos)  

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
  for i in range(len(lista) - 1):
    if lista[i] > lista[i+1]:
      return False
  return True

lista1 = [1, 2, 3, 4]
lista2 = [1, 3, 2, 4]

print(lista_ordenada(lista1))  
print(lista_ordenada(lista2))  


# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    """
    Recibe un texto y un desplazamiento, y devuelve el texto cifrado usando el cifrado César.
    Incluir el código aquí para cifrar el texto con el cifrado César.
    """
    pass


#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    pass


if __name__ == "__main__":
    main()