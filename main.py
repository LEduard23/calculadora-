def addmultiplenumbers(numeros): # Esta herramienta de suma facilita el cálculo de la suma de una lista de números.
 result = 0
 for num in numeros:
   result = result + num 
 return result
 
def multiplymultiplenumbers(numeros): # multiplicando los dos primeros números, luego tomando ese resultado y multiplicándolo por el tercer número, y continuando este proceso hasta que hayas multiplicado todos los números juntos
   result = 1
   for num in numeros:
      result *= num 
   return result
    
   
def isiteven(num): #se refiere a una función o problema en programación que determina si un número dado es par o impar
    if isinstance(num, int):
        return num % 2 == 0
    return False  



def isitaninteger(num): #cualquier número entero positivo o negativo, incluido el cero, que no tenga partes decimales ni fraccionarias
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
