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
    # Asks the user for some values, and then saves them in a new object
    print("Vänligen besvara frågorna nedan:")
    date = input("Vilket datum bryggdes ölen? Ange i formatet ÅÅ/MM/DD")

    malt = malt_func()

    hops_60 = hops_func(60)
    hops_30 = hops_func(30)
    hops_5 = hops_func(5)

    yeast = input("Vilken jäst använde du?")
    yeast_quantity = int_input(f"Hur många gram {yeast} använde du?")

    fermentation_time = int_input("Hur många dagar jäste ölen i jäskärlet?")
    beer_quantity = int_input("Hur många liter öl fick du ut av din bryggning?")
    OG = int_input("Vilket OG fick du fram vid mätning?")
    FG = int_input("Vilket FG fick du fram vid mätning?")
    sugar = int_input("Hur många gram socker användes vid sockerprimning?")
    description = input("Beskriv kort ölets smak och karaktär.")
    grade = int_input("Betygsätt denna brygning på en skala från 1 till 10.")
    comment = comment_func()

    print(date, malt, hops_60, hops_30, hops_5, yeast, yeast_quantity, fermentation_time, beer_quantity, OG, FG,
          sugar, description, grade, comment)


def choice_3():
    # Will view a list of all the saved objects
    pass


def hops_func(minutes):
    hop_number = int_input(f"Hur många sorter humle använde du vid {minutes} minuter?")
    hops = []
    for n in range(hop_number):
        kind = input("Vilken sorts humle använde du?")
        quantity = int_input(f"Hur många gram {kind} använde du?")
        hops.append(f"{kind} ({quantity} g)")
    return hops


def malt_func():
    malt_number = int_input("Hur många sorter malt har du använt?")
    malt = []
    for n in range(malt_number):
        kind = input("Vilken sorts malt använde du?")
        quantity = input(f"Hur många kilo {kind} malt använde du?")
        malt.append(f"{kind} ({quantity} kg)")
    return malt


def int_input(user_input):
    while True:
        data = input(user_input)
        if data.isdigit():
            return int(data)
        else:
            print("Ditt svar måste vara numeriskt.")


def comment_func():
    add_comment = input("Vill du lägga till en kommentar angående den här bryggningen, exempelvis förbättrningsförslag?"
                        " Ange J/N ")
    if add_comment.lower() == "j":
        comment = input("Ange din kommentar här: ")
        return comment
    else:
        comment = "Du har inte sparat någon kommentar."
        return comment



def main():
    show_menu()
    menu_choice()


if __name__ == "__main__":
    main()
