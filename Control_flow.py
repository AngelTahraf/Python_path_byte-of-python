#while
#for 
#if

#1 first eexercise -guess the rate of your 5 star accesory with number 

guess = 45
running = True

while running:
    tries = int(input("Write a number: "))
    if tries == guess:
        print("Congratulations!")
        running = False
    elif tries > 45:
        print("You need to put a less number")
    else:
        print("A higher number")
else:
    print("END LOOP")

print("END")