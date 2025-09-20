def addmultiplenumbers(numeros):
 result = 0
 for num in numeros:
   result = result + num 
 return result
 
def multiplymultiplenumbers(numeros):
   result = 1
   for num in numeros:
      result *= num 
   return result
    
   
def isiteven(num):
    if isinstance(num, int):
        return num % 2 == 0
    return False  



def isitaninteger(num):
 return isinstance(num, int)  
 
#def main():
#  num = []
 # while True:
 #  num1 = input("ingresa un numero o ingresa la letra q para detener: ")
   #if num1 == "q":
    # break
  
 #  print("El resultado de la operacion es: ", )
   

#print("Hello learners!")
#if __name__=="__main__":
 # main()