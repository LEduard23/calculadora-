def addmultiplenumbers(numbers):
      return sum(numbers)


def multiplymultiplenumbers(numbers):   
    result = 1
    for n in numbers:
        result *= n
    return result


def isiteven(num):
    if isinstance(num, int):
        return num % 2 == 0
    return False


def isitaninteger(num):
      return isinstance(num, int)


def main():
    print("Hello learners! Bienvenidos a la calculadora mejorada ")
    
    while True:
        print("\nOpciones:")
        print("1. Sumar varios números")
        print("2. Multiplicar varios números")
        print("3. Verificar si un número es par")
        print("4. Verificar si un número es entero")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == "1":
            numeros = input("Ingresa números separados por espacio: ")
            lista = [float(x) for x in numeros.split()]
            print("Resultado de la suma:", addmultiplenumbers(lista))
        
        elif opcion == "2":
            numeros = input("Ingresa números separados por espacio: ")
            lista = [float(x) for x in numeros.split()]
            print("Resultado de la multiplicación:", multiplymultiplenumbers(lista))
        
        elif opcion == "3":
            num = float(input("Ingresa un número: "))
            print("¿Es par?", isiteven(int(num)) if num.is_integer() else False)
        
        elif opcion == "4":
            num = input("Ingresa un número: ")
            try:
                val = float(num)
                print("¿Es entero?", isitaninteger(val) and val.is_integer())
            except ValueError:
                print("Entrada inválida")
        
        elif opcion == "5":
            print("Gracias por usar la calculadora. ¡Adiós!")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
