import random
num = 5
yuhp = 100
akirahp = 100
   
while True:
    start = int(input("Write the number of the turn: "))
    print("")
    akira_atk= random.randint(5,16)
    yu_atk= random.randint(4,17)
    hp_remain_yu = yuhp - akira_atk
    hp_remain_akira = akirahp - yu_atk
    if akira_atk >10 and yu_atk>10:
        print("Crtical Hit from akira",akira_atk)
        print("***************************")
        print("Crtical Hit from Yu",yu_atk)
        print("***************************")
    elif akira_atk >10:
        print("Crtical Hit from akira",akira_atk)
        print("***************************")
    elif yu_atk>10:
        print("Crtical Hit from Yu",yu_atk)
        print("***************************")
    def turn_akira():
        print(f"|Yu Remain HP:{hp_remain_yu}|")
    def turn_yu():
        print(f"|Akira Remain HP:{hp_remain_akira}|")
    turn_akira()
    turn_yu()
    yuhp = hp_remain_yu
    akirahp = hp_remain_akira
    ("---------------------")
    if akirahp<=0:
        print("Yu wins")
        break
    elif yuhp<=0:
        print("Akira Wins")
        break
    else:
        print("|another round|")
        continue
print("--END--")
