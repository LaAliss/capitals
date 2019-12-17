import sqlite3
import hashlib
import argparse
import random


def check_or_create():

    global conn
    global cursor
    conn = sqlite3.connect('ourdatabase.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user")
    except sqlite3.OperationalError:
        cursor.execute('''CREATE TABLE user
                      (username CHAR(256),
                       hasha CHAR(256),
                       salt CHAR(256), 
                       PRIMARY KEY (hasha))''')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="add a usernamename",
                        required=False)
    parser.add_argument('-p', help="the username password",
                        required=True)
    return parser.parse_args()


def save_new_username(username, password):
    global conn
    global cursor

    salt = str(random.random())
    hasha = salt + password

    for i in range(100000):
        hasha = hashlib.sha256(hasha.encode('utf-8')).hexdigest()

    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?,?)",
                   (username, hasha, salt))
    conn.commit()
    print('{} has been correctly inserted in ourdatabase'.format(username))
       
check_or_create()
args = parse_args()


if args.a and args.p:
    save_new_username(args.a, args.p)

conn.close()
