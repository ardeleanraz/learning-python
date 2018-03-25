# 4 se imparte la 2 , deci nu e prim
# 5 nu se imparte la nimic deci ii prim
# 6 se imparte la 2 si la 3 deci nu ii prim
# 7 ... prim
# 8 nu ii prim
# 9 nu ii prim

num =input('Choose a number')
num =int(num)
ii_prim =True
for checker in range(2 , num//2+ 1):
    if num % checker ==0:

        ii_prim = False

if ii_prim:
    print('prim')
else:
    print('nu ii prim')
