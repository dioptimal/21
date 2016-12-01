from random import random, randint

#k=sorted([6, 7, 8, 9, 10, 2, 3, 4, 11] * 4, key=lambda k: random())

def take_card(kol, ruka=0, ruka2=0):
    choice = input('Будете брать карту? y/n\n')
    if choice == 'y':
        karta = kol.pop()
        ruka += karta
        if ruka2<15:
            ruka2 += kol.pop()
        print('Вам попалась карта достоинством %d' % karta)
        if ruka > 21:
            print('Вы проиграли, набрав %d .' % ruka)
        elif ruka == 21:
            print('Поздравляю, вы набрали 21!')
        elif ruka2 > 21:
            print('Дилер проиграл, набрав %d очка.' % ruka2)
        elif ruka2 == 21:
            print('Дилер выиграл, набрав 21.')
        else:
            print('У вас %d очков.' % ruka)
            take_card(kol, ruka, ruka2)
    elif choice == 'n':
        while ruka2<15:
            ruka2 += kol.pop()
        print('У вас %d очков и вы закончили игру.' % ruka)
        if ruka > ruka2:
            print('У дилера %d очков.\nВы выиграли!' % ruka2)
        else:
            print('У дилера %d очков.\nВы проиграли!' % ruka2)
    else:
        print('Ответом должно быть либо "y",  либо "n"')
        take_card(ruka, kol)

def play(kol, again=''):
    choice = input('Сыграем%s? y/n\n' % again)
    if choice == 'y':
        take_card(kol)
    elif choice == 'n':
        return
    else:
        print('Ответом должно быть либо "y",  либо "n"')
        return play(kol)

    return play(kol, ' снова')
k = sorted([6, 7, 8, 9, 10, 2, 3, 4, 11] * 4, key=lambda k: random())
play(k)

print('До новых встреч!')
