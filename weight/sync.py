import os

def run(cmd):
    if os.system(cmd) != 0:
        raise Exception('Failed to run: \'{}\''.format(cmd))

run('git add weight.csv')
run('git add blood.csv')
run('git add weight.png')
run('git commit -m "Update weight"')
run('git push')
