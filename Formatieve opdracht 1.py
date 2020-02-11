#Opdracht 1
hoog = int(input("hoe hoog? "))
for a in range(1, hoog + 1):
    print("*" * a)
for b in reversed(range(1, hoog + 1)):
    print("*" * b)
i = 1
while i <= hoog:
    print("*" * i)
    i += 1
# Opdracht2
def Tekstcheck():
    Zin1 = input("geef de eerste zin aan ")
    Zin2 = input("geef de tweede zin aan ")
    return
# #Opdracht 3
# LijstOpdracht3A = (1,2,3,4,5,5,5,4,1,3)
# def tel():
#     tel = input("wat wilt u tellen ")
#     TelHoeveelheid = LijstOpdracht3A.count(tel)
#     return print(TelHoeveelheid)
# tel()

# Opdracht 4
#https://stackoverflow.com/questions/931092/reverse-a-string-in-python gebruikt voor de reverse.
def Palindroom():
    gewoon = input("van welk woord wilt u weten of het een Palindroom is ")
    gedraaid = (gewoon[::-1])
    if gedraaid == gewoon:
        print("het is een Palindroom")
    else:
        print("Het is geen Palindroom")
    return
Palindroom()

# Opdracht 5
def Sorteer():
    gewoon = (5,4,3,2,1)
    sorteer = gewoon.sort()
    return print(sorteer)
Sorteer()
# opdracht 6
def Gemmiddelde():
    cijfer = (5,4,3,2,1)
    x = sum(cijfer)
    aantal = len(cijfer)
    gemmiddelde = (x/aantal)
    return print (gemmiddelde)
Gemmiddelde()
# Opdracht 7
