import csv
import datetime


with open('weight.csv', 'r') as f:
    r = csv.reader(f)
    next(r)
    data = []
    for row in r:
        d = datetime.datetime.strptime(row[0], '%m/%d/%Y')
        w = float(row[1])
        data.append((d, w))
    print(data)
