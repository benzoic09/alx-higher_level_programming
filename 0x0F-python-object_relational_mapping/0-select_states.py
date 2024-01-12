#!/usr/bin/python3

import sys
import MySQLdb

def list_states(username, password, db_name):
    db = MySQLdb.connect(host="localhost", port=3306,
            user=username, passwd=password, db=db_name)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()

    for state in states:
        print(state)

        cur.close()
        db.close()

        if __name__ == "__main__":

            if len(sys.argv) != 4:
                print("Usage: python script.py <username> <password> <db_name>")
                sys.exit(1)

            username, password, db_name = sys.argv[1:4]
            list_states(username, password, db_name)
