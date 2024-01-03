
#We can also do 0 for snake, 1 for water and 2 for gun and not do -1 in both input and comp
from random import choice

matrix=[["Draw","You won","You lose"],["You lose","Draw","You Won"],["You won","You lose","Draw"]]

def play_game():
    comp=choice([1,2,3])
    print(f"computer choosed  {comp}")
    comp=comp-1
    answer=matrix[a][comp]
    print(answer)

while True:
    print(" 1 is for snake, 2 is for water, 3 is for gun and 4 is to exit the game: ")
    try:
        a=int(input("Enter your choice  "))-1
        if a==3:
           print("Thank you for playing")
           break
        play_game()
    except Exception as e:
        print("Enter number between 1-4 only")










