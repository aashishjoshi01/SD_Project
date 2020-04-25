import sqlite3
import unittest


class TestAdmin(unittest.TestCase):

    def test_admin(self):
        # Username can contain only
        # - alphabet and or
        # - numbers

        srf = 3
        baseprice = 1.5
        profit = 10

        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
        cur = conn.cursor()

        # Updating the values in the DB
        cur.execute("update admin set srf = ?, baseprice = ?, profit = ?", (srf, baseprice, profit))
        conn.commit()
        existing_users = []

        # Retrieving the data from the DB to show that the values are indeed updated
        cur.execute("select * from admin")
        row = cur.fetchone()
        conn.close()

        if row[0] == srf and row[1] == baseprice and row[2] == profit:
            print("Values are successfully updated in the DB")
            self.assertTrue(True)
        else:
            print("Values are not successfully updated in the DB")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
