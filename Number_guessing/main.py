import random

print("-------------------------------")
print("Welcome to the  guessing game!!")
print("-------------------------------")

#generate a random number between 0-9 single digit
#ui = user input


def play():
    choice = input("Would you like to start this game? Yes/No" + " ").lower()
    attempts = 0
    # print("there is no record of you gameplay")
    score = { }
    random_number = int(random.randint(0,9))
    print(random_number)
    name = input("Enter your name" + " ")
    print("Generated a single random digit number, try to find that in minimum attempts")
    ui = int(input("Please make the guess!!!"+ " "))
    while choice == "yes":
        score = {name : attempts}
        if ui == random_number:
            print("YOU NAILED IT!!!! Congratulations")
            attempts += 1
            score[name] = attempts
            print("1: Play Again")
            print("2: EXIT ")
            data = int(input())
            if data == 1:
                play()
            elif data == 2:
                exit()
            else:
                print("You choose the wrong number")
            #if he wants to play again??? then??
        elif random_number < ui :
            print("HINT: entered number is Bigger!! Try some small value")
            attempts += 1
        elif ui < random_number:
            print("HINT: entered number is Smaller!! Try some big value")
            attempts += 1
    if choice == "no":
        print("cool, have a good day!!")
    else:
        print("Wrong Value")
    return

play()