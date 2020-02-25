ye = 9
while ye == 9: 
    print("Select operation.")
    print("1. Aritmetic")
    print("2. Geometric")
    choice = input("your choice: ")
    if choice == '1':
        print(input("Press Enter to start ..."))
        a1 = float(input('a:'))
        an = float(input('n:'))
        dif = float(input('dif:'))
        aa = a1+(an-1)*dif
        print('answer:', aa)
        aq1 = int(input('between number:'))
        aq2 = int(input('and number:'))
        lista = []
        for x in range(aq1, (aq2+1)):
            asd = (a1+((x-1)*dif))
            lista.append(asd)
        print(sum(lista))       
        print(input("Press Enter to end ..."))
    elif choice == '2':
        print(input("Press Enter to start ..."))
        a1 = float(input('a:'))
        an = float(input('n:'))
        q = float(input('q:'))
        ga = a1*q**(an-1)
        print('answer:', ga)
        aq1 = int(input('between number:'))
        aq2 = int(input('and number:'))
        lista = []
        for x in range(aq1, (aq2+1)):
            gs = a1*q**(x-1)
            lista.append(gs)
        print(sum(lista))
        print(input("Press Enter to end ..."))
    else:
        for i in range(50):
            print('  ')

#this is pretty spaghetti...