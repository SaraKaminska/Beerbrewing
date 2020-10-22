from menu import choice_1, choice_2, choice_3, choice_4
from menu_choice_class import MenuChoice
from menu_class import Menu


choice1 = MenuChoice(1, choice_1)
choice2 = MenuChoice(2, choice_2)
choice3 = MenuChoice(3, choice_3)
choice4 = MenuChoice(4, choice_4)

choices = [choice1, choice2, choice3, choice4]
menu1 = Menu(choices)


def main():
    pass


if __name__ == "__main__":
    main()
