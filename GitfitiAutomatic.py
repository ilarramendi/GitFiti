import requests
from time import sleep
from subprocess import run, DEVNULL

TOKEN = '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'
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