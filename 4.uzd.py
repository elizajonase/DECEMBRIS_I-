ievaditais_skaitlis = int(input("Ievadiet skaitli: "))

if ievaditais_skaitlis < 0:
    print("Faktoriāls nav definēts negatīviem skaitļiem.")
else:
    faktorials = 1

    for i in range(1, ievaditais_skaitlis + 1):
        faktorials *= i

    print(f"{ievaditais_skaitlis} faktoriāls ir: {faktorials}")