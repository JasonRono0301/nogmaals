#De eerste opdracht.
teller = 30
while teller > 0:
    print(teller)
    teller = teller - 1

#De tweede opdracht.
uren = 0
while uren < 12:
    if uren < 6:
        print(str(uren) + ' am')
    else:
        print(str(uren) + ' pm')
    uren += 1  

#De derde opdracht.
getal = 20
while getal <= 50:
    print(getal)
    getal += 1

deDag = input('Type een dag in:')
while deDag > '':
    if deDag == 'maandag':
        print('hello')
        break
    else:
        print('Ongeldige invoer')
        break
