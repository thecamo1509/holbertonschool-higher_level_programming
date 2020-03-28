#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':

    mydb = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = mydb.cursor()
    cur.execute("SELECT cities.name FROM states, cities WHERE states.id = cities.state_id and states.name = %s ORDER BY cities.id ASC", (argv[4],))  
    states = cur.fetchall()
    string = ""
    for i in states:
        string = string + i[0] + ", "
    print(string[0:-2])
    cur.close()
    mydb.close()
