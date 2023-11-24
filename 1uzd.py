ievaditais_skaitlis = int(input("Ievadiet skaitli: "))

summa = 0

for i in range(1, ievaditais_skaitlis + 1):
    summa += i

print(f"Summa no 1 līdz {ievaditais_skaitlis} ir: {summa}")