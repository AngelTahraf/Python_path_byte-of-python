# functions
import random
num = 5
def turn_akira():
    yuhp = 100
    atk = yuhp - random.randint(5,16)
    print("Remain HP:",atk)
    yuhp = atk
def turn_yu():
    akirahp = 100
    atk1 = akirahp - random.randint(4,17)
    print("Remain HP:",atk1)
    akirahp = atk1   
     
while True:
    start = int(input("Write a number to start:"))
    turn_akira()
    turn_yu()
    ("---------------------")
    if turn_yu<=0:
        print("Yu wins")
        break
    elif turn_akira<=0:
        print("Akira Wins")
        break
    else:
        print("another round")
        continue
print("--END--")
