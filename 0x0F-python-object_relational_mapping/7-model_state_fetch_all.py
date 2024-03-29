#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1:4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name), pool_pre_ping=True)

    session = sessionmaker(bind=engine)

    session = session()

    first_state = session.query(State).order_by(State.id).first()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    session.close()
