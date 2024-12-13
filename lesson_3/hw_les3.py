number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

match number1 and number2:
    case ("+"):
        print(number1+number2)
    case ("-"):
        print(number1-number2)
    case ("/"):
        print(number1/number2)
    case ("*"):
        print(number1*number2)
    case _: # аналог else
        print("Invalid input please try again")