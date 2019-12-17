import argparse
import csv
import sqlite3
import hashlib

from CSVfolder.csvcode import get_capital_or_state

csv_folder = 'CSVfolder/capitals.csv'
csv_reader = csv.reader(open(csv_folder, 'r'))

conn = None
cursor = None
database = 'scripts/ourdatabase.db'

'''
This function check the username in order to control if it is in the database

'''

def check_for_username(username, password):

    global conn
    global cursor
    
    conn = sqlite3.connect('scripts/ourdatabase.db')
    cursor = conn.cursor()
    salt = cursor.execute("SELECT salt FROM user WHERE username=?", (username,)).fetchall()

    conn.commit()

    hasha = str(salt[0][0]) + password

    
    for i in range(100000):
        hasha = hashlib.sha256(hasha.encode('utf-8')).hexdigest()

    rows = cursor.execute("SELECT * FROM user WHERE username=? and hasha=?", (username, hasha))
    
    conn.commit()
    results = rows.fetchall()
    # NOTE: this could be done more efficiently with a JOIN
    if results:
        print("User is present, password is valid" )
    else:
        print("User is not present, or password is invalid")     
    
    cursor.close()
    conn.close()


''' This function parses as positional argument the State or the Capital.
Then we define the level of verbosity'''


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Please, insert the capital or the State')
    parser.add_argument('-c', help="Check username and password",
                        required=False)
    parser.add_argument('-p', help="The username password", required=True)
    parser.add_argument('-v', '--verbosity', help='Incrementally increase the verbosity', action='count', default=0)
    args = parser.parse_args()
    return args


args = parse_arguments()

'''
This function allow to run the entire program, first checking username and password and then running the function that looks for the country or capital name.

'''

if __name__ == '__main__':
    args = parse_arguments()
    '''capitals.check_capital(args)'''
    '''capitals.check_state(args)'''
    get_name = get_capital_or_state(args.name)
    check_for_username(args.c, args.p)
    print(get_name)
