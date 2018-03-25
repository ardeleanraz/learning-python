# palindroame: 1 sau 2 sau 11 sau 88 sau 959 sau 12321 sau 252 sau 14541
# care nu sunt palindroame : 1332

l1 = []
l2 = []
num = input('Choose a number')
num = int(num)
num_backup = num
while num > 0:
    ultima_cifra = num % 10
    num = num // 10
    l1.append(ultima_cifra)


#copiam lista l1
l2 = list(l1)
l2.reverse()
print (l2)
print (l1)

if l1 == l2 :
    print('palindrom')
else:
    print('nu e palindrom')


if str(num)== str(''.join(reversed(str(num)))):
    print ('ii palindrom')
else:
    print('nu ii')