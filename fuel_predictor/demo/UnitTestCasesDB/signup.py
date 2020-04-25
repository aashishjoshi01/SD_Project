import sqlite3
import unittest


class TestSignUP(unittest.TestCase):

    def test_username(self):
        # Username can contain only
        # - alphabet and or
        # - numbers

        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
        cur = conn.cursor()

        # username choosen by the New user
        username = 'Sharath123'

        cur.execute("select * from login")
        users = cur.fetchall()
        existing_users = []

        for i in range(0, len(users)):
            existing_users.append(users[i][0])

        # print(existing_users)
        if username not in existing_users:
            # Username can contain only - alphabet and or numbers
            if str.isalnum(username):
                # Username should be at least 8 characters long
                if len(username) > 7:
                    self.assertTrue(True)
                    print("Username is Valid")
                else:
                    print("Username must contain at least 8 characters")
                    self.assertTrue(False)

            else:
                print("Username can contain only alphabet and numbers")
                self.assertTrue(False)
        else:
            print("Username is already taken")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
