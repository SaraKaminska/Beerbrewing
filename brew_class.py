class Brew:
    def __init__(self, name, date, ingredients, fermentation, quantity, OG, FG, sugar, description, grade, comment):
        self.name = name
        self.date = date
        self.fermentation = fermentation
        self.quantity = quantity
        self.sugar = sugar
        self.description = description
        self.grade = grade
        self.comment = comment
        self.OG = OG
        self.FG = FG
        self.abv = self.abv_func()
        self.ingr_list = ingredients

    def __str__(self):
        return self.name

    def abv_func(self):
        if type(self.OG) != int or type(self.FG) != int:
            raise TypeError("Ogiltigt värde, OG och FG måste vara numeriska.")
        if self.OG < 1000 or self.FG < 1000:
            raise ValueError("Ogiltigt värde, OG och FG kan inte vara 0 eller lägre.")
        return (self.OG - self.FG) * 0.132

    def brew_print(self):
        print(f"{self.name} brygd: {self.date}\n")
        print("INGREDIENSER:")
        for ingredient in self.ingr_list:
            ingredient.print_ingredient()
        print("")
        print(f"Jästid: {self.fermentation} dagar".ljust(25), f"Mängd färdig brygd: {self.quantity} liter")
        print(f"Alkoholhalt: {self.abv:.1f}%".ljust(25), f"Socker tillsatt vid primning: {self.sugar} gram\n")
        print(f"Betyg: {self.grade}".ljust(25), f"Beskrivning: {self.description}\n")
        print(f"Kommentar: {self.comment}")


def main():
    pass


if __name__ == "__main__":
    main()
