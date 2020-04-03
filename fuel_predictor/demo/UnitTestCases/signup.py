import unittest


class TestSignUP(unittest.TestCase):

    def test_username(self):
        # Username can contain only
        # - alphabet and or
        # - numbers

        existing_users = ['Sharath123', 'Aashish96']
        username = 'Praneeth@123'

        # Username should be unique. Comparing it with other existing usernames
        if username not in existing_users:
            # Username can contain only - alphabet and or numbers
            if str.isalnum(username):
                # Username should be at least 8 characters long
                if len(username) > 7:
                    self.assertTrue(True)
                    print("Username is Valid")
                else:
                    self.assertTrue(False)
                    print("Username must contain at least 8 characters")
            else:
                print("Username can contain only alphabet and numbers")
                self.assertTrue(False)
        else:
            print("Username is already taken")
            self.assertTrue(False)

    def test_password(self):

        pwd = 'htarahs654'
        # Password can contain only - alphabet and or numbers
        if str.isalnum(pwd):
            # Password must contain at least - one Uppercase letter and one Lowercase letter
            if str.upper(pwd) != pwd and str.lower(pwd) != pwd:
                # If all conditions are met the data is valid
                if len(pwd) > 7:
                    self.assertTrue(True)
                    print("Password is Valid")
                else:
                    self.assertTrue(False)
                    print("Password must contain at least 8 characters")
            else:
                print("Password must contain at least one uppercase and one lowercase letter")
                self.assertTrue(False)
        else:
            print("Password can contain only alphabet and numbers")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
