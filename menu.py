import os
import pickle
import sys
import tkinter as tk
from menu_choice_class import MenuChoice
from brew_class import Brew
from input_functions import *


class Menu:
    def __init__(self):
        choice1 = MenuChoice(1, self.choice_1)
        choice2 = MenuChoice(2, self.choice_2)
        choice3 = MenuChoice(3, self.choice_3)
        choice4 = MenuChoice(4, self.choice_4)
        choice5 = MenuChoice(5, self.choice_5)
        choice6 = MenuChoice(6, self.choice_6)

        choices = [choice1, choice2, choice3, choice4, choice5, choice6]
        self.menu_choices = choices

    @staticmethod
    def show_menu():
        print("Välj ett av menyalternativen:")
        print("1 Grundrecept för öl")
        print("2 Lägg till ny brygd")
        print("3 Visa sparade bryggningar")
        print("4 Ta bort en bryggning")
        print("5 Redigera brygd")
        print("6 Avsluta programmet")

    def menu_choice(self):
        choice = input("Menyval: ")
        if choice.isdigit() and 1 <= int(choice) <= 6:
            self.menu_choices[int(choice)-1].run_menu_function()
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")
            self.return_to_menu()

    def return_to_menu(self):
        print("-" * 80)
        print("")
        self.show_menu()
        self.menu_choice()

    def choice_1(self):
        def return_menu(event):
            window.destroy()
            print("-" * 80)
            print("")
            self.show_menu()
            self.menu_choice()

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

    def choice_2(self):
        # Asks the user for some values, and then saves them in a new object
        print("Vänligen besvara frågorna nedan:")

        name = name_input()
        date = input("Vilket datum brygdes ölen? Ange i formatet ÅÅÅÅ/MM/DD")

        ingredients = ingr_func("malt")
        ingredients += hops_func(60)
        ingredients += hops_func(30)
        ingredients += hops_func(5)
        ingredients += ingr_func("jäst")

        sugar = int_input("Hur många gram socker användes vid sockerprimning?")
        fermentation_time = int_input("Hur många dagar jäste ölen i jäskärlet?")
        beer_quantity = float_input("Hur många liter öl fick du ut av din brygning?")
        OG = og_fg_func("OG")
        FG = og_fg_func("FG")
        grade = int_input("Betygsätt denna brygning på en skala från 1 till 10.")
        description = input("Beskriv kort ölets smak och karaktär.")
        comment = comment_func()

        file_name = name.lower().replace(" ", "_") + ".brew"

        name = Brew(name, date, ingredients, fermentation_time, beer_quantity, OG, FG, sugar, description, grade, comment)

        with open("saved_brews/" + file_name, "wb") as saved_brew:
            pickle.dump(name, saved_brew)
        print("Din brygd har blivit sparad!")

        self.return_to_menu()

    def choice_3(self):
        # Views all the saved brews
        print("SPARADE BRYGDER:")
        brew = self.load_and_pick()

        with open("saved_brews/" + brew[1], "rb") as brew:
            brew = pickle.load(brew)
            print("")
            brew.brew_print()
            print("")

        self.return_to_menu()

    def choice_4(self):
        print("TA BORT BRYGD:")
        brew = self.load_and_pick()
        delete = input(f"Vill du ta bort {brew[0]}? J/N")
        if delete.lower() == "j":
            os.remove("saved_brews/" + brew[1])
            print(f"Brygden {brew[0]} har tagits bort.")
        else:
            print("Brygden har inte tagits bort.")

        self.return_to_menu()

    def choice_5(self):
        print("REDIGERA BRYGD:")
        picked_brew = self.load_and_pick()
        change_options = ["name", "date", "comment"]
        for n, option in enumerate(change_options):
            print(n, option)
        change_num = int_input("Vilken position vill du ändra?")
        new_value = input(f"Ange ny/nytt {change_options[change_num]}: ")

        with open("saved_brews/" + picked_brew[1], "rb") as saved_brew:
            brew = pickle.load(saved_brew)
            brew.__dict__[change_options[change_num]] = new_value
        with open("saved_brews/" + picked_brew[1], "wb") as saved_brew:
            pickle.dump(brew, saved_brew)

        self.return_to_menu()


    @staticmethod
    def choice_6():
        sys.exit("Allons-y.")

    def load_and_pick(self):
        files_dict = self.load()
        picked = self.pick(files_dict)
        return picked

    def load(self):
        file_no = 1
        files_dict = {}
        if len(os.listdir("saved_brews")) == 0:
            print("Du har inga sparade brygder.")
            self.return_to_menu()
        else:
            for file in os.listdir("saved_brews"):
                if file.endswith(".brew"):
                    file_name = file[:-5]
                    file_name = file_name.replace("_", " ").title()
                    files_dict[file_no] = file_name
                    file_no += 1

            for no, brew in files_dict.items():
                print(f"{no}. {brew}")
        return files_dict

    @staticmethod
    def pick(files_dict):
        while True:
            picked = int_input("Välj en brygd från listan ovan:")
            if picked in files_dict:
                brew = files_dict[picked].lower().replace(" ", "_") + ".brew"
                return [files_dict[picked], brew]
            else:
                print("Det finns ingen brygd med detta nummer. Försök igen.")


def main():
    pass

if __name__ == "__main__":
    main()
