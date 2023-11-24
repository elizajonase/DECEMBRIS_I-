skaitlis = int(input("Ievadiet skaitli: "))


if skaitlis % 3 == 0 and skaitlis % 7 == 0:
    print(f"{skaitlis} dalās gan ar 3, gan ar 7.")
else:
    print(f"{skaitlis} nedalās gan ar 3, gan ar 7.")