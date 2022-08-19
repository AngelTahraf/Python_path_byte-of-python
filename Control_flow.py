#while
#for 
#if

#2 first exercise -guess the rate of your 5 star accesory with number 

while True:
    weak_point = 6
    guess = int(input("Write a number from 1 to 10"))
    if guess == weak_point:
        print("You did it")
        break
    elif guess > weak_point:
        print("Your number is higher")
        continue
    else:
        print("Your number is less")
        continue
print("END")

