def summ(a, b):

    if b == 0:
        return a

    return summ(a + 1, b - 1)

Sum = summ(int(input('a:')), int(input('b:')))
print(f'Сумма -  {Sum}')


