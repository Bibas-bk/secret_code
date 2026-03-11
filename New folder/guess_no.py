import time
print("AI mind reader")
time.sleep(2)#it
print("Guess a number bewtween 1 and 100")
input("press enter when you ready!")

low=1
high=100
while low<=high:
    guess=(low+high)//2
    answer=input(f"Choose y for if number is greater than {guess} Otherwise n: y/n\n") 
    if answer.lower()=='y':
        low=guess+1
    else:
        high=guess-1
print("Your num is:",low)            