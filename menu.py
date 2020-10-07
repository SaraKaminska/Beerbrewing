import pickle
from brew_class import Brew
from input_functions import ingr_func, hops_func, int_input, comment_func


def show_menu():
    print("ÖLBRYGGNING")
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
        return_to_menu()


def choice_1():
    f = open("recipe.txt", encoding="utf-8")
    text = f.read()
    print(text)
    return_to_menu()


def choice_2():
    # Asks the user for some values, and then saves them in a new object
    print("Vänligen besvara frågorna nedan:")
    date = input("Vilket datum bryggdes ölen? Ange i formatet ÅÅÅÅ/MM/DD")

    ingredients = ingr_func("malt")
    ingredients += hops_func(60)
    ingredients += hops_func(30)
    ingredients += hops_func(5)
    ingredients += ingr_func("jäst")

    sugar = int_input("Hur många gram socker användes vid sockerprimning?")
    fermentation_time = int_input("Hur många dagar jäste ölen i jäskärlet?")
    beer_quantity = int_input("Hur många liter öl fick du ut av din bryggning?")
    OG = int_input("Vilket OG fick du fram vid mätning?")
    FG = int_input("Vilket FG fick du fram vid mätning?")
    grade = int_input("Betygsätt denna brygning på en skala från 1 till 10.")
    description = input("Beskriv kort ölets smak och karaktär.")
    comment = comment_func()

    date = Brew(date, ingredients, fermentation_time, beer_quantity, OG, FG, sugar, description, grade, comment)

    with open("saved_brews.txt", "ab") as saved_brews:
        pickle.dump(date, saved_brews)
    print("Din brygd har blivit sparad!")

    return_to_menu()


def choice_3():
    # Views all the saved brews
    brews = []
    with open("saved_brews.txt", "rb") as saved_brews:
        try:
            brew = pickle.load(saved_brews)
            brews.append(brew)
        except EOFError:
            print("Det finns inga sprade bryggningar.")
            return_to_menu()

    for brew in brews:
        print("")
        brew.brew_print()
        print("-"*80)
        print("")

    return_to_menu()


def return_to_menu():
    print("-"*80)
    print("")
    show_menu()
    menu_choice()


def main():
    #malts = malt_func()
    #for malt in malts:
    #    malt.print_ingredient()

    show_menu()
    menu_choice()


if __name__ == "__main__":
    main()
