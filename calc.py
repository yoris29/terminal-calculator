import time

def add(a, b):
   return int(a) + int(b)
def mult(a, b):
   return int(a) * int(b)
def sub(a, b):
   return int(a) - int(b)
def div(a, b):
   return int(a) / int(b)

while True:
   print("A. Addition")
   print("B. Subtraction")
   print("C. Multiplication")
   print("D. Division")
   print("E. Exit")

   operation = input("What is your desired operation: ")
   if(operation.isupper()):
      operation = operation.lower()

   if operation == "e":
      break

   first_num = input("Please enter your first number: ")
   second_num = input("Please enter your second number: ")   

   if operation == "a":
      print("Your number is: ", add(first_num, second_num))
   elif operation == "b":
      print("Your number is: ", sub(first_num, second_num))
   elif operation == "c":
      print("Your number is: ", mult(first_num, second_num))
   elif operation == "d":
      print("Your number is: ", div(first_num, second_num))
   else:
      print("Please enter a valid operation choice (a, b, c, d, e).")
      break

   time.sleep(2)