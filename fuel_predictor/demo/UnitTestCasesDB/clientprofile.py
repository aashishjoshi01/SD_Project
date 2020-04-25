import unittest
import sqlite3


class MyTestCase(unittest.TestCase):
    def test_update(self):
        username = "NewUser123"
        fname = "New User"
        addr1 = "2000 Richmond St"
        addr2 = "Apt 100"
        city = "Dallas"
        state = "TX"
        zipcode = "75000"

        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
        cur = conn.cursor()

        cur.execute(
            "update profile set username = ?, fullname = ?, address1 = ?, address2 = ?, "
            "city = ?, state = ?, zipcode = ?", (username, fname, addr1, addr2, city, state, zipcode))

        conn.commit()

        cur.execute("select * from profile where username = ? and fullname = ? and address1 = ? and  address2 = ? "
                    "and city = ? and state = ? and zipcode = ?",
                    (username, fname, addr1, addr2, city, state, zipcode))

        row = cur.fetchone()

        if row is not None:
            print("Able to update profile values")
            self.assertTrue(True)
        else:
            print("Unable to update profile values")
            self.assertTrue(False)

    def test_insert(self):
        username = "NewUser123"
        fname = "New User"
        addr1 = "2000 Richmond St"
        addr2 = "Apt 100"
        city = "Dallas"
        state = "TX"
        zipcode = "75000"

        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
        cur = conn.cursor()

        cur.execute("insert into profile (username, fullname, address1, address2, city, state, zipcode) "
                    "values(?,?,?,?,?,?,?)", (username, fname, addr1, addr2, city, state, zipcode))

        conn.commit()

        cur.execute("select * from profile where username = ? and fullname = ? and address1 = ? and  address2 = ? "
                    "and city = ? and state = ? and zipcode = ?",
                    (username, fname, addr1, addr2, city, state, zipcode))

        row = cur.fetchone()

        if row is not None:
            print("Able to insert profile values")
            self.assertTrue(True)
        else:
            print("Unable to update profile values")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
