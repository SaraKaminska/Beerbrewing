import os
import pickle
import tkinter as tk
from brew_class import Brew
from input_functions import *


def show_menu():
    print("Välj ett av menyalternativen:")
    print("1 Grundrecept för öl")
    print("2 Lägg till ny brygd")
    print("3 Visa sparade bryggningar")
    print("4 Ta bort en bryggning")


def menu_choice():
    choice = input("Menyval: ")
    if choice.isdigit():
        if int(choice) == 1:
            choice_1()
        elif int(choice) == 2:
            choice_2()
        elif int(choice) == 3:
            choice_3()
        elif int(choice) == 4:
            choice_4()
    else:
        print("Du har gjort ett ogiltigt val. Försök igen.")
        return_to_menu()


def choice_1():
    def return_menu(event):
        window.destroy()
        print("-" * 80)
        print("")
        show_menu()
        menu_choice()

    window = tk.Tk()
    header = tk.Label(window, text="Grundrecept för öl \n", font=("Arial", 20, "bold"), padx=15)
    header.grid(sticky=tk.W)

    recipe = open("recipe.txt", encoding="utf-8")
    for line in recipe:
        if line.startswith(("1", "2", "3", "4", "5", "6", "7")):
            header = tk.Label(window, text=line, font=("Arial", 10, "bold"), justify="left", wraplength=800, padx=15)
            header.grid(sticky=tk.W)
        else:
            plain = tk.Label(window, text=line, font=("Arial", 10), justify="left", wraplength=800, padx=15)
            plain.grid(sticky=tk.W)
    recipe.close()

    button = tk.Button(window, text="Tillbaka till meny")
    button.grid(sticky=tk.E)
    button.bind("<ButtonRelease-1>", return_menu)

    window.mainloop()


def choice_2():
    # Asks the user for some values, and then saves them in a new object
    print("Vänligen besvara frågorna nedan:")
    name = input("Ange ett namn för din bryggd:")
    date = input("Vilket datum bryggdes ölen? Ange i formatet ÅÅÅÅ/MM/DD")

    ingredients = ingr_func("malt")
    ingredients += hops_func(60)
    ingredients += hops_func(30)
    ingredients += hops_func(5)
    ingredients += ingr_func("jäst")

    sugar = int_input("Hur många gram socker användes vid sockerprimning?")
    fermentation_time = int_input("Hur många dagar jäste ölen i jäskärlet?")
    beer_quantity = float_input("Hur många liter öl fick du ut av din bryggning?")
    OG = int_input("Vilket OG fick du fram vid mätning?")
    FG = int_input("Vilket FG fick du fram vid mätning?")
    grade = int_input("Betygsätt denna brygning på en skala från 1 till 10.")
    description = input("Beskriv kort ölets smak och karaktär.")
    comment = comment_func()

    file_name = name.lower().replace(" ", "_") + ".brew"

    name = Brew(name, date, ingredients, fermentation_time, beer_quantity, OG, FG, sugar, description, grade, comment)

    with open(file_name, "wb") as saved_brew:
        pickle.dump(name, saved_brew)
    print("Din brygd har blivit sparad!")

    return_to_menu()


def choice_3():
    # Views all the saved brews
    print("SPARADE BRYGGDER:")
    brew = load_and_pick()

    with open("saved_brews/"+brew[1], "rb") as brew:
        brew = pickle.load(brew)
        print("")
        brew.brew_print()
        print("")

    return_to_menu()


def choice_4():
    print("TA BORT BRYGGD:")
    brew = load_and_pick()
    delete = input(f"Vill du ta bort {brew[0]}? J/N")
    if delete.lower() == "j":
        os.remove("saved_brews/"+brew[1])
        print(f"Bryggden {brew[0]} har tagits bort.")
    else:
        print("Bryggden har inte tagits bort.")

    return_to_menu()


def return_to_menu():
    print("-"*80)
    print("")
    show_menu()
    menu_choice()


def load_and_pick():
    file_no = 1
    files_dict = {}

    for file in os.listdir("saved_brews"):
        if file.endswith(".brew"):
            file_name = file[:-5]
            file_name = file_name.replace("_", " ").title()
            files_dict[file_no] = file_name
            file_no += 1

    if len(files_dict) > 0:
        for no, brew in files_dict.items():
            print(f"{no}. {brew}")
        picked = int_input("Välj en bryggd från listan ovan:")
        brew = files_dict[picked].lower().replace(" ", "_") + ".brew"
        return [files_dict[picked], brew]
    else:
        print("Du har inga sparade bryggder.")
        return_to_menu()


def main():
    choice_3()


if __name__ == "__main__":
    main()
