from ingredient_class import Ingredient, Hops


def hops_func(minutes):
    hop_number = int_input(f"Hur många sorter humle använde du vid {minutes} minuter?")
    hops_list = []
    for n in range(hop_number):
        sort = input("Vilken sorts humle använde du?")
        amount = int_input(f"Hur många gram {sort} använde du?")
        hops = Hops(sort, amount, minutes)
        hops_list.append(hops)
    return hops_list


def ingr_func(ingredient):
    ingr_number = int_input(f"Hur många sorter {ingredient} har du använt?")
    ingredients = []
    for n in range(ingr_number):
        sort = input(f"Vilken sorts {ingredient} använde du?")
        amount = input(f"Hur många gram {sort} {ingredient} använde du?")
        ingredient = Ingredient(sort, amount)
        ingredients.append(ingredient)
    return ingredients


def og_fg_func(gravity):
    while True:
        n = int_input(f"Vilket {gravity} fick du fram vid mätning? Ange fyra siffror, ex 1050.")
        if n >= 1000:
            return n
        else:
            print("Du har anget ett ogiltigt värde. Vänligen ange fyra siffror, ex 1050.")


def name_input():
    while True:
        special_chars = ["\"", "/", "\\", ":", "*", "?", "<", ">"]
        name = input(f"Ange ett namn för din bryggd. Följande tecken är ej tillåtna: \" / \ : * ? < >.")
        if any(char in name for char in special_chars):
            print("Namnet du angav innehåller ogiltiga tecken, försök igen.")
        else:
            return name


def int_input(user_input):
    while True:
        data = input(user_input)
        if data.isdigit():
            return int(data)
        else:
            print("Ditt svar måste vara numeriskt.")


def float_input(user_input):
    while True:
        data = input(user_input)
        try:
            return float(data)
        except ValueError:
            print("Ditt svar måste vara numeriskt.")


def comment_func():
    add_comment = input("Vill du lägga till en kommentar angående den här bryggningen, exempelvis förbättrningsförslag?"
                        " Ange J/N ")
    if add_comment.lower() == "j":
        comment = input("Ange din kommentar här: ")
        return comment
    else:
        comment = "Du har inte sparat någon kommentar på den här brygden."
        return comment


def main():
    pass


if __name__ == "__main__":
    main()
