import hashlib
import sqlite3
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Username can contain only
        # - alphabet and or
        # - numbers

        username = 'NewUser123'
        password = 'NewUser123'
        hash_pwd = hashlib.md5(password.encode('utf-8')).hexdigest()

        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
        cur = conn.cursor()
        cur.execute("select * from login")
        users = cur.fetchall()
        existing_users = []

        for i in range(0, len(users)):
            existing_users.append(users[i][0])
            existing_users.append(users[i][1])

        uname_pwd_pairs = {existing_users[i]: existing_users[i + 1] for i in range(0, len(existing_users), 2)}

        # Username and pwd is compared to existing data to validate the authenticity of the user
        for user in uname_pwd_pairs:

            if username == user and hash_pwd == uname_pwd_pairs[user]:
                print("Valid User")
                self.assertTrue(True)
                break
        else:
            print("Unable to validate User. Please check User ID and Password")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
