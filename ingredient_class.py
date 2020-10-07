class Ingredient:
    def __init__(self, sort, amount):
        self.sort = sort
        self.amount = amount

    def print_ingredient(self):
        print(f"{self.sort} ({self.amount} g)")


class Hops(Ingredient):
    def __init__(self, sort, amount, boilingtime):
        super().__init__(sort, amount)
        self.boilingtime = boilingtime

    def print_ingredient(self):
        print(f"{self.sort} ({self.amount} g) Koktid: {self.boilingtime} minuter")


def main():
    malt = Ingredient("Pale Ale", 2500)
    humle = Hops("Citra", 10, 60)

    malt.print_ingredient()
    humle.print_ingredient()

if __name__ == "__main__":
    main()
