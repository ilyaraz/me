import os

def run(cmd):
    if os.system(cmd) != 0:
        raise Exception('Failed to run: \'{}\''.format(cmd))

run('git add garmin')
run('git add wahoo')
run('git commit -m "Update exercise"')
run('git push')
