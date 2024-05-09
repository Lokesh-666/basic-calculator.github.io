# define the functions needed: add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# white loop to continue the program until the user wants to exit
def add(a, b):
    answer = a+b
    print(str(a) + '+' + str(b) + '=' + str(answer) + "\n")

def sub(a, b):
    answer = a-b
    print(str(a) + '-' + str(b) + '=' + str(answer) + "\n")            

def mul(a,b):
    answer = a*b
    print(str(a) + '*' + str(b) + '=' + str(answer) + "\n")

def div(a, b):
    answer = a/b
    print(str(a) + '/' + str(b) + '=' + str(answer) + "\n")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")


    choice = str(input("give your choice: "))
    if choice.upper() == 'A':
        print ("addition of the two numbers. Give those two numbers now:-")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        add(a,b)

    elif choice.upper() =='B':
        print("Subtraction of two numbers. Give those two numbers now:- ")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        sub(a,b)    


    elif choice.upper() =='C':
        print("Multiplication of two numbers. Give those two numbers now:- ")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        mul(a,b)    

    elif choice.upper() =='D':
        print("Division of two numbers. Give those two numbers now:- ")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        div(a,b)    
    elif choice.upper() == 'E':
        print("programe Ended!")
        quit