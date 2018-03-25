#Se cer numere de la usher ,pana cand se introduce numarul 0.
# Dupa introducerea numarului 0 , se va printa cel mai mare numar introdus de usher.
numere =[]
while True:
    num1 =input('Dati un numar sau 0 pentru oprire ')

    num1=int(num1)
    numere.append(num1)
    print(numere)






    if num1 == 0:
        break

print(max(numere))
