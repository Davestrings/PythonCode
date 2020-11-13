for i in range(2,11):
    number_str = ''

    for j in range(1, i):
        number_str = number_str + str(j)
    number = int(number_str)
    ans = number * 9 + i
    print(number, 'x', 9, '+', i, '=', ans)
    ##print(f'{number:>10} x + {i} = {ans}')


##for i in range(11, 1, -1):
##    number_str = ''

##    for j in range(1, i):
##        number_str = number_str + str(j)
##    number = int(number_str)
##    ans = number * 9 + i
   ## print(number, 'x', 9, '+', i, '=', ans)
##    print(f'{number:>10} x + {i} = {ans}')
