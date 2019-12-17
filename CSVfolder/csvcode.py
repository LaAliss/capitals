import csv


''' This function will read the csv file as dictionary and on a
input basis, it will return the Capital or the State'''


def get_capital_or_state(name):
    with open('CSVfolder/capitals.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if row[1] == name:
                return row[0]
            elif row[0] == name:
                return row[1]
            else:
                continue
