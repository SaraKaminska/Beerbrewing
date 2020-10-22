class Menu:
    def __init__(self, menu_choices):
        self.menu_choices = menu_choices

    def show_menu(self):
        print("Välj ett av menyalternativen:")
        print("1 Grundrecept för öl")
        print("2 Lägg till ny brygd")
        print("3 Visa sparade bryggningar")
        print("4 Ta bort en bryggning")

    def menu_choice(self):
        choice = input("Menyval: ")
        if choice.isdigit():
            if int(choice) == 1:
                self.menu_choices[0].run_menu_function()
            elif int(choice) == 2:
                self.menu_choices[1].run_menu_function()
            elif int(choice) == 3:
                self.menu_choices[2].run_menu_function()
            elif int(choice) == 4:
                self.menu_choices[3].run_menu_function()
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")
            self.return_to_menu()

    def return_to_menu(self):
        print("-" * 80)
        print("")
        self.show_menu()
        self.menu_choice()


def main():
    pass


if __name__ == "__main__":
    main()
