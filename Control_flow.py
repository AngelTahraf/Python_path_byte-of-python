#while
#for 
#if

#2 first exercise -guess the rate of your 5 star accesory with number 
weak_point = 6
weak_point_2 = 9
tries = 0
def info_data ():
    print("1-Head\n2-RightArm\n3-LeftArm\n4-Chest\n5-Eyes")
    print("6-Body\n7-RightLeg\n8-LeftLeg\n9-Back\n10-Foot")
while True:
    info_data()
    guess = int(input("Write a number from 1 to 10: "))
    tries = tries + 1
    if guess == weak_point:
        print("You did it")
        break
    elif tries == 3:
        print("You're out of guesses")
        break
    elif guess != weak_point:
        print("E-------RR-------OR")
        print("Write another number")
        print("E-------RR-------OR")
        continue
print("END")

