for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")



base = 2
exponent = 5

def fun(base,exponent):
    if base==2:
        z=base**exponent
        print(f'2 raises to the power of 5:{z}')
    else:
         print("none")

fun(2,5)

