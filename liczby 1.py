#liczby pierwsze - zadanie domowe


def gen(x):
    pierwsze=[]
    z = 2
    while len(pierwsze)<x-1:
        jest=False
        for a in pierwsze:
            if z%a ==0:
                jest=True
            break
        if not jest:
            pierwsze.append(z)
        z+=1
    pierwsze.insert(0,1)
    return pierwsze
print(gen(25))
