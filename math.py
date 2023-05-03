 import random

 try:
     while True:
        num1=random.randint(1, 100)
        num2 = random.randint(1, 100)
        result = num1 + num2

        print(str(num1)+ "+" + str(num2))


        answer = input(">")

        if answer == str(result): print("Correct!")
        else: print("Wrong! the correct answer was " + str(result)) 

 except ValueError:
    print("Number Only.")   