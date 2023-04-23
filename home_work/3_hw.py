def maxchislo():
    list = [-1, 1]
    max_number = max(list)
    print ('наибольшее число', max_number)
maxchislo()


def otlichie():
    a = 50
    b = 100
    if a and b == 135:
        print('yes')
    else:
        print('No')
otlichie()

def season(m):
    if m == 12 or m < 3:
        return 'Зима'
    if m > 2 and m < 6:
        return 'Весна'
    if m > 5 and m < 9:
        return 'Лето'
    if m > 8 and m < 12:
        return 'Осень'
m = int(input('Введите номер месяца: '))
print(season(m))


def proizvol():
    a = 4
    b = 5
    c = 6
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    if a < 10 and b < 10 and c < 10:
        print('No')
proizvol()












