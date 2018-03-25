# Cerem doua numere de la usher si il printam pe cel mai mare
num1 =input('Choose a number! ')
num2 =input('Choose another number! ')

num1 =int(num1)
num2 =int(num2)

if num1 < num2:
    print('cel mai mare numar este :' , num2)
else:
    print('cel mai mare numar este :' , num1)


print ('...sau mai smecher:')
print(max(num1,num2))