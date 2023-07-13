import random 
score=0
r=random.randint(1,11)

while True:
    f=int(input("Guess the number: "))
    if f!=r:
        if (f>r):
            score-=1
            print("Try smaller number: ")
            print("Score is: ",score)
        else:
            score-=1
            print("Try greater number: ")
            print("Score is: ",score)
    else:
        score+=1
        print("You got it right!!!")
        print("Score is: ",score)