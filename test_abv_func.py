from unittest import TestCase
from brew_class import Brew


class TestCalculateAbv(TestCase):
    def test_calculate_1(self):
        test_brew = Brew("The Maiden", "2020/05/16", ["Pale ale, 2500 g", "Citra, 10 g"], 14, 9.5, 1040, 1010, 65,
                         "Tydlig beska", 6, "Ingen kommentar")
        self.assertEqual(test_brew.abv, 3.96)

    def test_calculate_2(self):
        test_brew = Brew("The Maiden", "2020/05/16", ["Pale ale, 2500 g", "Citra, 10 g"], 14, 9.5, 1050, 1015, 65,
                         "Tydlig beska", 6, "Ingen kommentar")
        self.assertEqual(test_brew.abv, 4.62)

    def test_calculate_og_fg_lower_than_1000(self):
        with self.assertRaises(ValueError) as error:
            test_brew = Brew("The Maiden", "2020/05/16", ["Pale ale, 2500 g", "Citra, 10 g"], 14, 9.5, 1050, 999, 65,
                             "Tydlig beska", 6, "Ingen kommentar")


def main():
    pass


if __name__ == "__main__":
    main()
