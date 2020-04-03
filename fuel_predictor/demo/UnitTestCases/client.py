import unittest
import re


class TestSimple(unittest.TestCase):

    def test_fname(self):
        # Full name must contain only alphabet
        fname = 'George Reddy 123'
        pattern = re.compile("^[A-Za-z ]+$")

        if pattern.match(fname):
            self.assertTrue(True)
            print("Full Name is valid")
        else:
            print("Full Name must contain only alphabet and or space")
            self.assertTrue(False)

    def test_addr(self):
        # Address1 cannot exceed 100 characters
        addr1 = '2250 Holly Hall'
        addr2 = 'vsnnnnvnsvnsnvsndndnlsncndvnnznv nvhihroeogfhsafkafkbkehiheofnsvvgiwshihviksb ighrihifhohsihfvnsknvkbsivishirf'
        if len(addr1) < 100 and len(addr2) < 100:
            self.assertTrue(True)
            print('Address is valid')
        elif len(addr1) > 100:
            print("Address1 cannot exceed 100 characters")
            self.assertTrue(False)
        else:
            print('Address2 cannot exceed 100 characters')
            self.assertTrue(False)

    def test_city(self):
        # City must contain only alphabet
        city = 'Houston*'
        if str.isalpha(city):
            self.assertTrue(True)
            print("City is valid")
        else:
            print("City must be an alphabet")
            self.assertTrue(False)

    def test_state(self):
        # State cannot be empty
        state = ''
        if len(state) != 0:
            self.assertTrue(True)
            print("State is valid")
        else:
            print("State cannot be empty")
            self.assertTrue(False)

    def test_zipcode(self):
        # Zipcode must be numeric
        zipcode = '77054a'
        if str.isnumeric(zipcode):
            self.assertTrue(True)
            print("Zipcode is valid")
        else:
            print("Zipcode must be numeric")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
