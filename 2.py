# crear un vector de 10 enteros. A continuación, pedir un entero y una posición del vector y sustituir el entero situado en esa posición del vector por el nuevo entero introducido. Visualizar el vector resultante

def main():
    a = []
    for i in range(10):
        b = int(input(f"dime un numero {i + 1}: "))
        a.append(b)
    print("vector: ")
    print(a)
    c = int(input("dime un numero: "))
    d = int(input("dime una posicion: "))
    a[d] = c
    print("vector corregido:")
    print(a)
    
main()