import unittest


class TestSimple(unittest.TestCase):

    def test_srf(self):
        # Seasonal Rate Fluctuation must be numeric
        srf = 'Twenty'
        try:
            float(srf)
            self.assertTrue(True)
            print("Seasonal Rate Fluctuation value is valid")
        except ValueError:
            print("Seasonal Rate Fluctuation value is Invalid. It can accept only an integer.")
            self.assertTrue(False)

    def test_base_price(self):
        # Base Price must be numeric
        baseprice = 'Two'
        try:
            float(baseprice)
            self.assertTrue(True)
            print("Base Price value is valid.")
        except ValueError:
            print("Base Price value is Invalid. It can accept only an integer")
            self.assertTrue(False)

    def test_profit(self):
        # Profit must be numeric
        profit = 'Three'

        try:
            float(profit)
            self.assertTrue(True)
            print("Profit value is valid")
        except ValueError:
            print("Profit value is Invalid. It can accept only an integer")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
