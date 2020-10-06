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

    def abv_func(self, OG, FG):
        abv = (OG - FG) * 0.132
        return abv

    def brew_print(self):
        print(f"Datum för bryggning: {self.date}")
        print("Ingredienser:")
        for ingredient in self.ingr_list:
            ingredient.print_ingredient()
        print(f"Jästid: {self.fermentation} dagar", 5*" ", f"Mängd färdig brygd: {self.quantity} liter")
        print(f"Socker tillsatt vid primning: {self.sugar} g", 5*" ", f"Alkoholhalt: {self.abv} %")
        print(f"Betyg: {self.grade}", 5*" ", f"Beskrivning: {self.description}")
        print(f"Kommentar: {self.comment}")


def main():
    pass


if __name__ == "__main__":
    main()
