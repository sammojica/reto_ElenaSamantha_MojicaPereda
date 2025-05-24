# Descripción del código

## General
Este código fue diseñado en python, a través de cada print se va llamando a la función, la cual forzosamente debe recibir 2 parámetros para poder ejecutarse.
En cualquier caso (válido/inválido) la terminal debe mostrar el mensaje del return.

### Lógica
- def sumarNumero(a,b): Aquí se define la función, la cual entre paréntesis lleva los parámetros que le fueron dados desde el print.
- if ... else: Procede a usarse para validar 2 casos, el primero donde se cumple nuestra condición y el segundo en caso contrario. Con el if type(valor) == int, comprobamos que la clase de nuestra variable corresponda al entero que necesitamos.
- return: Valor que retorna la función, se pide que retorne un string y al estar trabajando con enteros se debe utilizar "f" antes de las comillas, el cual lo formatea a una cadena, con ello colocamos la variable de nuestro resultado entre llaves {}.
