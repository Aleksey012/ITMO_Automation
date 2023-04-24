def maxchislo(x, y):
    # list = [-1, 1]
    max_number = max(x, y)
    print ('наибольшее число', max_number)
maxchislo(-1, 1)


def otlichie(a, b):
    # a = 50
    # b = 100
    if max(a, b) - min(a, b) == 135:
        print('yes')
    else:
        print('No')
otlichie(50, 100)

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


def proizvol(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    # if a < 10 and b < 10 and c < 10:
    else:
        print('No')
proizvol(11, 12, 13)












