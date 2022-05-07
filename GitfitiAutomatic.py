import requests
from time import sleep
from subprocess import run, DEVNULL

if '-t' not in argv or len(argv) < argv.index('-t'):
	print('Missing Token (-t TOKEN)')
	exit()
TOKEN = argv[argv.index('-t') + 1]

USERNAME = 'ilarramendi'
DATA = {
  'name': 'dummy',
  'description': "Dummy repository for ilarramendi/Gitfiti",
  'homepage': 'https://github.com',
  'private': False
}

r = requests.delete('https://api.github.com/repos/' + USERNAME + '/' + DATA['name'], headers={'Authorization': 'TOKEN ' + TOKEN})
r = requests.post('https://api.github.com/user/repos', json=DATA, headers={'Authorization': 'TOKEN ' + TOKEN})

if r.status_code == 201: 
    if run(['python3', 'Gitfiti.py', '-u', USERNAME, '-rn', DATA['name'], '-t', TOKEN, '-c', 100]).returncode == 0: run(['sh', 'Gitfiti.sh'], stdout=DEVNULL, stderr=DEVNULL)
    else: print('Error generating script with Gitfiti.py')
else: print('Error creating repo: ', r.content, r.status_code)