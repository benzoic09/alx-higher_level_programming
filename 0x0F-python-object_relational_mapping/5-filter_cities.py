#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <db_name> <state_name>".format(
            sys.argv[0]))
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1:5]

    db = MySQLdb.connect(user=username,
                         passwd=password,
                         db=db_name,
                         host='localhost',
                         port=3306)

    cur = db.cursor()
    query = ("SELECT cities.id, cities.name, states.name FROM cities\
             JOIN states ON cities.state_id = states.id\
             WHERE states.name LIKE %s ORDER BY cities.id")

    cur.execute(query, (state_name,))
    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()

