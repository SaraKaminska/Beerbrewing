class Brew:
    def __init__(self, date, ingredients, fermentation, quantity, OG, FG, sugar, description, grade, comment):
        self.date = date
        self.ingr_list = ingredients
        self.fermentation = fermentation
        self.quantity = quantity
        self.OG = OG
        self.FG = FG
        self.sugar = sugar
        self.description = description
        self.grade = grade
        self.comment = comment
        self.abv = self.abv_func(OG, FG)

    def __str__(self):
        return self.date

    def abv_func(self, OG, FG):
        abv = (OG - FG) * 0.132
        return abv

    def brew_print(self):
        print(f"DATUM: {self.date}\n")
        print("INGREDIENSER:")
        for ingredient in self.ingr_list:
            ingredient.print_ingredient()
        print("")
        print(f"Jästid: {self.fermentation} dagar.".ljust(25), f"Mängd färdig brygd: {self.quantity} liter.")
        print(f"Alkoholhalt: {self.abv} %".ljust(25), f"Socker tillsatt vid primning: {self.sugar} gram.\n")
        print(f"Betyg: {self.grade}".ljust(25), f"Beskrivning: {self.description}\n")
        print(f"Kommentar: {self.comment}")


def main():
    pass


if __name__ == "__main__":
    main()
