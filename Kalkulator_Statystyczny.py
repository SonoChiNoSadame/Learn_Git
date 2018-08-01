print("Hello, my fantastic guest!!!!")
wejscie = int(input("How many numbers do you have?"))

numbers = []


def dane(l):
    stringi = ("first", "second", "third", "forth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", 'next')
    y = 0
    a = 0
    while y < l:
        x = float(input("Please enter " + stringi[a] + " number(from 1 to 100):"))
        if x > 100:
            print("Too big number!!! Select different number")
        elif x < 1:
            print("Number is too small!!! Select different number")
        else:
            numbers.append(x)
            y = y + 1
            if a < 10:
                a = a + 1


def std(sth):
    tabelka = []
    suma = sum(sth)
    divisor = len(sth)
    mean = suma / divisor
    for x in sth:
        tabelka.append((x - mean) ** 2)
    x_x = sum(tabelka)
    standard = (x_x / 5) ** (1 / 2)
    return standard


dane(wejscie)
suma = sum(numbers)
divisor = len(numbers)
mean = suma / divisor
std = std(numbers)
rsd = std / mean
cv = rsd * 100
print("Sum is equal to:", suma)
print("Mean is equal to:", mean)
print("Standard deviation is equal to:", std)
print("Relative standard deviation is equal to:", rsd)
print("Coefficient of variation is equal to:", cv, "%")
