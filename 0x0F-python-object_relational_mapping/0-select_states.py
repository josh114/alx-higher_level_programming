#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa
import sys
import MySQLdb
'''module validates username, passwd and db'''
if __name__ == '__main__':
    '''setup db connect and validation'''
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    '''execute query'''
    c.execute('SELECT * FROM `states`')
    [print(state) for state in c.fetchall()]
