a = int(input("Введите a: "))
b = int(input("Введите b: "))

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(f"НОД = {a + b}")
