


def add(n1, n2):
  return n1+n2
  
def substract(n1, n2):
  return n1-n2
  
def mul(n1, n2):
  return n1*n2
  
def div(n1, n2):
  return n1/n2

operations = {"+" : add, "-": substract, "*" : mul, "/" : div }

def calculator():
  num1 = float(input("enter number 1 : \n"))
  for symbol in operations:
    print(symbol)
  
  carry_on = True
  
  
  while carry_on:
    selected_operation = input("Select operator :")
  
    num2 = float(input("enter next number: \n"))
    perform = operations[selected_operation]
    answer =perform( num1,  num2)
  
    print(answer)
  
    if input("enter y to continue and n to exit :") == 'y':
      num1 = answer
    else:
      carry_on = False
      calculator()




calculator()
  

  


