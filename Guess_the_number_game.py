import random
x=int(input("Press 0 for playing in default range. \nPress 1 for playing in custom range. "))
if(x==1):
    b=int(input("Enter the start of the range="))
    c=int(input("Enter the end of the range="))
elif(x==0):
    b=1
    c=20
    print("Default range is between 1 to 20.")
else:
    b=1
    c=20
    print("Since you have not selected 0 or 1, So you are playing in default range. \nDefault range is between 1 to 20.")
n=random.randint(b,c)
a=c*5
d=a
while(c):
    if(a != d):
        print(f"To quit type {b-1}")
    u=int(input(f"Enter the number between {b} to {c}="))
    if(u==b-1 and a!=d):
        print("Exited")
        break
    if(u==n):
        print("Great! You Won")
        print(f"Your Score is {a} out of {d}")
        break
    elif(u>c or u<b-1):
        print(f"Please give the number in the range of {b} to {c}")
    elif(u<n):
        print("Oops wrong answer, you guessed too small, try again.")
        a=a-1
        continue
    elif(u>n):
        print("Oops wrong answer, you guessed too large, try again.")
        a=a-1
        continue
print("Game Over!")
