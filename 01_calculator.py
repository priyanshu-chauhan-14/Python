while(True):
    print("=====================================================")
    choice = int(input("Enter your choice : \n1. ADD \n2.SUBTRACT \n3.MULTIPLY \n4.FLOOR DIVISION \n5.DIVISION \n6.REMAINDER \n7.EXIT > "))
    print("=====================================================")

    if(choice==1):
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print(f"Sum: {num1} + {num2}: {num1+num2}")
        print("=====================================================")

    elif(choice==2):
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print(f"Difference: {num1} - {num2}: {num1-num2}")
        print("=====================================================")

    elif(choice==3):
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print(f"Product: {num1} x {num2}: {num1-num2}")
        print("=====================================================")

    elif(choice==4):
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print(f"Floor Division {num1} // {num2}: {num1//num2}")
        print("=====================================================")

    elif(choice==5):
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print(f"Division {num1} / {num2}: {num1/num2}")
        print("=====================================================")

    elif(choice==6):
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print(f"Remainder {num1} % {num2}: {num1%num2}")
        print("=====================================================")

    elif(choice==7):
        print("Exiting..")
        break
            

    
    
