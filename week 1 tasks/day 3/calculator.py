try:
  run = True

  while run:
    num1 = float(input("Enter first number:"))
    operator = input("Enter the operator:")
    num2 = float(input("Enter second number:"))
    result=None

    if operator=="+":
      result=num1+num2
    elif operator=="-":
      result=num1-num2
    elif operator=="*":
      result=num1*num2
    elif operator=="/":
      result=num1/num2
    elif operator=="^" or operator=="**":
      result=num1**num2
    elif operator=="%":
      result=num1%num2
    else:
      print("Please, enter a valid operator which can be + or - or * or / or ^  ** or %")

    if result is not None:
      print(f"Answer:  {result}")
    
    print("Do you want to do another calculation?, type \"no\" to exit")

    userInput=input()
    
    if userInput=='no':
      run=False
    

except ZeroDivisionError:
    print("Please, don't try to divide by zero, how is it even possible? think about it buddy, how can you make something into nothing, not possible according to the laws of physics and divine law")
except:
    print("something went wrong, buddy. don't worry you'll got this, keep working on it")
