# Análisis ejercicio 10

### Recibe un texto y un desplazamiento, y devuelve el texto cifrado usando el cifrado César


#### Para hacer un código cifrado:
1. Crear una función que reciba un texto y el desplazamiento que se quiere tener en cada letra
2. Luego se debe definir las variables 
3. Se debe recibir el texto y el desplazamiento que se quiere hacer para cada letra 
4. Se utiliza la función ord ("letra en tabla ASCII") para devuelva el numero al que corresponde en esa tabla
5. Una vez lee el numero equivalente hace operación para convertir letra ASCII en letra equivalente
6. Se debe crear una condición en la que se defina el rango en el que están letras
7. Se hace la operación de #letra_devuelve=#letra_devuelve + desplazamiento (esto solo en caso de que la suma de dentro del rango)
8. Si la suma da dentro del rango, se hace la operación anterior si no el desplazamiento se da hasta el rango maximo y vuelve y comienza
9. Se debe crear una lista que vaya almacenando los caracteres resultantes 
10. Se debe usar .lower() para que convierta las entradas de texto a minúscula y pueda comparar más facilmente con el rango que se específico de la tabla ASCII 
 
