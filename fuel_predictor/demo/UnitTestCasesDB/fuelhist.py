import unittest
import sqlite3


class MyTestCase(unittest.TestCase):
    def test_hist(self):
        username = "NewUser123"

        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
        cur = conn.cursor()

        cur.execute("select * from fuelquote where username = ?", (username,))
        row = cur.fetchone()

        if row is not None:
            print("Able to retrieve values from the DB")
            self.assertTrue(True)
        else:
            self.assertTrue(False)

        rows = []

        for fuelquote in cur.fetchall():
            row = [fuelquote[1], fuelquote[2], fuelquote[3], fuelquote[4], fuelquote[5]]
            rows.append(row)


if __name__ == '__main__':
    unittest.main()
