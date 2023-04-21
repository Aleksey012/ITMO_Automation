num_float = 3.4

# Также попробуйте варианты
# num_float = 0
# num_float = -4.5


if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('ноль')
else:
    print('число отрицательное')


permit_print = True
num = 3
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

num_2 = 120
if num_2 > 120 or num_2 < -100:
    print('-')
else:
    print('+')