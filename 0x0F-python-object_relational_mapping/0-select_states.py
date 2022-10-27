#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa
import sys
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(user.argv[1], passwd.argv[2], name.argv[3])
    c = db.cursor()
    c.execute('SELECT * FROM `states`')
    [print(state) for state in c.fetchall()]
