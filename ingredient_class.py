class Ingredient:
    def __init__(self, sort, amount):
        self.sort = sort
        self.amount = amount


class Hops(Ingredient):
    def __init__(self, sort, amount, boilingtime):
        super().__init__()
        self.boilingtime = boilingtime


def main():
    pass


if __name__ == "__main__":
    main()
