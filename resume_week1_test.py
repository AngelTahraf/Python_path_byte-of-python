#(\t) - (\n) - f and Format
# While - for and fuctions


pw = "btk1"  #Password
tries = 0
def user_data (namee,email):
    print("{0}\t{1}".format(namee,email))


while True:
    guess = str(input("Write your password: "))
    tries = tries+1
    if tries >3:
        print("You are Out\nGuesses")
        break
    elif guess == pw:
        print("Login Succesful")
        user_data("Anthony","ant-ony@mail.com")
        break
    else:
        print("Wrong password")
