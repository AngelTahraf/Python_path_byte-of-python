akira = set(("lilim","alice","arsene","jack frost"))
yu = set(("izanagi","jack frost", "High pixie","Foul"))

print(akira)
print(yu)
print("♦♦♦♦♦♦♦♦♦♦♦")
print(akira | yu )
print("♣♣♣♣♣♣♣♣♣♣♣")
print(akira & yu )
print("♠♠♠♠♠♠♠♠♠♠♠")
print(akira - yu )

akira.add("izanagi")
akira.remove("arsene")
yu.add("arsene")
yu.remove("izanagi")

print(akira)
print(yu)