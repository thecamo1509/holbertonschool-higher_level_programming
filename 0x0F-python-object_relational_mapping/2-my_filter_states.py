#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':
    mydb = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = mydb.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC"
                .format(argv[4]))
    states = cur.fetchall()
    for i in states:
        print(i)
    cur.close()
    mydb.close()
