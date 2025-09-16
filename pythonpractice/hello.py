import random
a=random.randrange(1,50)
n=int(input("Print a number between 1 to 50: " ))
if n==a:
    print("You win")    
else:
    n2=int(input("Try again: "))
    if n2==a:
        print("You win")
    else:
        n3=int(input("Last chance: "))
        if n3==a:
            print("You win")
        else:
            print("You lose, the number was ",a)