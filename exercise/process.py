import os
import re
import json
import sys
import datetime
from collections import defaultdict
from matplotlib import pyplot as plt

strava_files_folder = '../export/strava/data'

total = 0
data = []
for (_, _, files) in os.walk(strava_files_folder):
    for file_name in files:
        if re.match('[0-9]*\.json', file_name) is not None:
            full_file_name = os.path.join(strava_files_folder, file_name)
            with open(full_file_name, 'r') as activity_file:
                activity = json.loads(activity_file.read())
            dt = datetime.datetime.strptime(activity['start_date'], '%Y-%m-%dT%H:%M:%SZ')
            if activity['calories'] == 0.0:
                continue
            data.append((dt.date(), activity['calories']))
    break
aggregate = defaultdict(float)
for (u, v) in data:
    aggregate[u] += v
dates = []
calories = []
for key in sorted(aggregate.keys()):
    dates.append(key)
    calories.append(aggregate[key])
fig, ax = plt.subplots()
ax.vlines(dates, 0, calories, color='#999999')
print(min(dates))
print(max(dates))
delta = (max(dates) - min(dates)).days + 1
print(delta)
smoothed_dates = []
smoothed_calories = []
for i in range(3, delta - 3):
    mid_date = min(dates) + datetime.timedelta(i)
    total_calories = 0.0
    for j in range(len(dates)):
        if dates[j] < mid_date - datetime.timedelta(3):
            continue
        if dates[j] > mid_date + datetime.timedelta(3):
            continue
        total_calories += calories[j]
    average_calories = total_calories / 7.0
    smoothed_dates.append(mid_date)
    smoothed_calories.append(average_calories)
ax.plot(smoothed_dates, smoothed_calories, color='red')
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.2)
plt.savefig('exercise_calories.png', dpi=200)
