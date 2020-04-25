import unittest
import sqlite3


class MyTestCase(unittest.TestCase):
    def test_adminvalues(self):
        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
        cur = conn.cursor()

        cur.execute("select * from admin")
        row = cur.fetchone()
        conn.close()

        if row is not None:
            print("Able to retrieve values from 'admin' table")
            self.assertTrue(True)
        else:
            print("Unable to retrieve values from 'admin' table")
            self.assertTrue(False)

    def test_state(self):

        username = "NewUser123"

        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
        cur = conn.cursor()

        cur.execute("select * from profile where username  = ?", (username,))
        row = cur.fetchone()
        conn.close()

        if row is not None:
            print("Able to retrieve 'State' value from 'profile' table")
            self.assertTrue(True)
        else:
            print("Unable to retrieve 'State' value from 'profile' table")
            self.assertTrue(False)

    def test_history(self):

        username = "NewUser123"

        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
        cur = conn.cursor()

        cur.execute("select count(*) from fuelquote where username  = ?", (username,))
        row = cur.fetchone()
        conn.close()

        if row is not None:
            print("Able to retrieve fuelquote history values from 'fuelquote' table")
            self.assertTrue(True)
        else:
            print("Unable to retrieve fuelquote history values from 'fuelquote' table")
            self.assertTrue(False)

    def test_insert(self):

        username = "NewUser123"
        gallons = 1200
        address = "2000 Richmond St, Apt 100, Dallas, TX - 75000"
        deliveryDate = "2020-05-01"
        base = 1.8
        amount = 2160

        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
        cur = conn.cursor()

        cur.execute("insert into fuelquote values(?,?,?,?,?,?)",
                    (username, gallons, address, deliveryDate, base, amount))

        conn.commit()

        cur.execute(
            "select * from fuelquote where username = ? and gallons = ? and address = ? and  date = ? and price = ? "
            "and amount = ?",
            (username, gallons, address, deliveryDate, base, amount))

        row = cur.fetchone()
        conn.close()

        if row is not None:
            print("Able to insert fuelquote values and also be able to retrieve them")
            self.assertTrue(True)
        else:
            print("Unable to insert fuelquote values and also be able to retrieve them")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
