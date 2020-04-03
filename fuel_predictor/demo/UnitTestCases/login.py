import unittest


class TestLogin(unittest.TestCase):

    def setUp(self):
        pass

    def test_authen(self):
        # Username can contain only
        # - alphabet and or
        # - numbers

        username = 'Sharath'
        password = 'Password123'

        users = {'Sharath123': 'Password123', 'AashishJoshi': 'Joshi1996', 'Praneeth': 'Pragada98'}

        # Username and pwd is compared to existing data to validate the authenticity of the user
        for user in users:

            if username == user and password == users[user]:
                self.assertTrue(True)
                print("Valid User")
                break
        else:
            print("Unable to validate User. Please check User ID and Password")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
