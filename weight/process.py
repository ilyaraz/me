import csv
import datetime
from matplotlib import pyplot as plt


with open('weight.csv', 'r') as f:
    r = csv.reader(f)
    next(r)
    data = []
    for row in r:
        d = datetime.datetime.strptime(row[0], '%m/%d/%Y')
        w = float(row[1])
        data.append((d, w))
    plt.ylim((73, 118))
    plt.xticks(rotation='vertical')
    plt.subplots_adjust(bottom=0.17)
    plt.grid(True)
    for window in [1, 7]:
        if window % 2 == 0:
            raise Exception('Even window size: median is ambiguous')
        xaxis = []
        yaxis = []
        for i in range(len(data)):
            if i < window - 1:
                continue
            xaxis.append(data[i][0])
            cur_window = []
            for j in range(window):
                cur_window.append(data[i - j][1])
            cur_window.sort()
            med = cur_window[window // 2]
            yaxis.append(med)
        plt.plot(xaxis, yaxis)
    plt.savefig('weight.png')