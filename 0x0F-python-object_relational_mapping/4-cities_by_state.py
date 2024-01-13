#!/usr/bin/python3
""" Python script to list all cities from the hbtn_0e_4_usa database """

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: {} <username> <password> <db_name>".format(
            sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1:4]

    try:
        db = MySQLdb.connect(user=username,
                             passwd=password,
                             db=db_name,
                             host='localhost',
                             port=3306)

        cur = db.cursor()
        query = "SELECT * FROM cities ORDER BY id ASC"
        cur.execute(query)
        results =  cur.fetchall()
        for rows in results:
            print(rows)

    except MySQLdb.Error as e:
        print("MYSQL Error: {}".format(e))
        sys.exit(1)

    finally:
        if db:
            db.close()
        
