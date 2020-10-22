class MenuChoice:
    def __init__(self, menu_number, function):
        self.menu_number = menu_number
        self.function = function

    def run_menu_function(self):
        self.function()


def main():
    pass


if __name__ == "__main__":
    main()
