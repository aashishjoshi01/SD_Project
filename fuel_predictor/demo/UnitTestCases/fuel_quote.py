import unittest
from datetime import date


class TestSimple(unittest.TestCase):

    def setUp(self):
        pass

    def test_gallons(self):
        gallons = '20'
        try:
            float(gallons)
            self.assertTrue(True)
            print("Gallons value is valid")
        except:
            print("Gallons must be numeric")
            self.assertTrue(False)

    def test_deliveryAddress(self):
        deliveryAddress = '2250'
        if len(deliveryAddress) != 0:
            self.assertTrue(True)
            print("Delivery address value is valid")
        else:
            print("Delivery address cannot be empty")
            self.assertTrue(False)

    def test_deliveryDate(self):

        deliveryDate = '2020-03-01'
        today = date.today()
        d3 = today.strftime("%Y-%m-%d")
        # d3 = str(d3)

        if d3 < deliveryDate:
            self.assertTrue(True)
            print("Delivery Date is valid")
        else:
            print("Delivery Date must be in the future")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()