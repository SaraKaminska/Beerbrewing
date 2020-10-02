class Ingredients:
    def __init__(self, malt, hops60, hops30, hops5, yeast, yeast_quantity):
        self.malt = malt
        self.hops60 = hops60
        self.hops30 = hops30
        self.hops5 = hops5
        self.yeast = yeast
        self.yeast_quantity = yeast_quantity

    def return_ingredients(self):
        return (f"Malt: {self.malt}. Humle: {self.hops60}, {self.hops30}, {self.hops5}. "
              f"Jäst: {self.yeast} ({self.yeast_quantity}g)")


def main():
    pass


if __name__ == "__main__":
    main()
