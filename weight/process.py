import csv
import datetime
from matplotlib import pyplot as plt
import matplotlib.dates as mdates


with open('weight.csv', 'r') as f:
    r = csv.reader(f)
    next(r)
    data = []
    for row in r:
        d = datetime.datetime.strptime(row[0], '%m/%d/%Y')
        w = float(row[1])
        data.append((d, w))
    fig, ax = plt.subplots()
    for window in [1, 7]:
        if window % 2 == 0:
            raise Exception('Even window size: median is ambiguous')
        xaxis = []
        yaxis = []
        for i in range(len(data)):
            bad = False
            cur_window = []
            for j in range(i - window // 2, i + window // 2 + 1):
                if j < 0 or j >= len(data):
                    bad = True
                    break
                cur_window.append(data[j][1])
            if bad:
                continue
            xaxis.append(data[i][0])
            cur_window.sort()
            med = cur_window[window // 2]
            yaxis.append(med)
        if window == 1:
            color = '#999999'
        else:
            color = 'red'
        ax.plot(xaxis, yaxis, color=color, linewidth=1.3)
    ax.grid(True)
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.set_ylim((73, 118))
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=0.17)
    plt.savefig('weight.png', dpi=200)