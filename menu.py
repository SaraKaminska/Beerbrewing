def show_menu():
    print("Ölbryggning")
    print("Välj ett av menyalternativen:")
    print("1 Grundrecept för öl")
    print("2 Lägg till ny brygd")
    print("3 Visa sparade bryggningar")


def menu_choice():
    choice = input("Menyval: ")
    if choice.isdigit():
        if int(choice) == 1:
            choice_1()
        elif int(choice) == 2:
            choice_2()
        elif int(choice) == 3:
            choice_3()
    else:
        print("Du har gjort ett ogiltigt val. Försök igen.")
        show_menu()


def choice_1():
    f = open("recept.txt", encoding="utf-8")
    text = f.read()
    print(text)


def choice_2():
    # Will ask the user for some values, and then save them in a new object brygd
    pass


def choice_3():
    # Will view a list of all the saved objects
    pass


def main():
    show_menu()
    menu_choice()


if __name__ == "__main__":
    main()
