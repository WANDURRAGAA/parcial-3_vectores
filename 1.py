# realizar un ejercicio que lea 10 numeros enteros de dos cifras, almacene dichos numeros en un vector y muestre el vector resultante multiplicado por 2

enteros = []

for _ in range(10):
    numero = int(input("Ingresa un entero de dos digitos: "))
    if numero < 10 or numero > 99:
        print("El numero no es de 2 digitos")
        continue
    enteros.append(numero)

resultado = [num * 2 for num in enteros]

print("multiplicado por 2:", resultado)