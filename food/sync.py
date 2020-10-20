import os

def run(cmd):
    if os.system(cmd) != 0:
        raise Exception('Failed to run: \'{}\''.format(cmd))

run('git add log')
run('git commit -m "Update food"')
run('git push')
