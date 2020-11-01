import os

def run(cmd):
    if os.system(cmd) != 0:
        raise Exception('Failed to run: \'{}\''.format(cmd))

run('git add data')
run('git commit -m "Update Strava data"')
run('git push')
