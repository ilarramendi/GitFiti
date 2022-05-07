import requests
from time import sleep
from subprocess import run, DEVNULL
from glob import glob
from datetime import datetime
from threading import Thread

# TODO imporve framerate

TOKEN = ''
USERNAME = 'ilarramendi'
REPO_PREFIX = 'DUMMY_'

frames = list(enumerate(sorted(glob('frames/frame-*.json'))))

print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] =>"), 'Deleting all "' + REPO_PREFIX + '*" repositories')
for i, frame in frames: requests.delete('https://api.github.com/repos/' + USERNAME + '/' + REPO_PREFIX + str(i), headers={'Authorization': 'TOKEN ' + TOKEN})

def deleteRepo(seconds, number):
	sleep(seconds)
	deleteUrl = 'https://api.github.com/repos/' + USERNAME + '/' + REPO_PREFIX + str(number)
	if requests.delete(deleteUrl, headers={'Authorization': 'TOKEN ' + TOKEN}).status_code != 204: print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] =>"), 'Error deleting repo number:', number)
	else: print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] =>"), 'Deleted previous frame: ', number)



while (True):
	for i, frame in frames:
		print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] =>"), 'Drawing frame: ', i)
		DATA = {
			'name': REPO_PREFIX + str(i),
			'description': "Dummy repository for ilarramendi/Gitfiti",
			'homepage': 'https://github.com',
			'private': False
		}

		r = requests.post('https://api.github.com/user/repos', json=DATA, headers={'Authorization': 'TOKEN ' + TOKEN})
		
		if r.status_code == 201:
			if run(['python3', 'Gitfiti.py', '-u', USERNAME, '-rn', DATA['name'], '-t', TOKEN, '-c', '50', '-i', frame]).returncode == 0: 
				run(['sh', 'Gitfiti.sh'], stdout=DEVNULL, stderr=DEVNULL)
				Thread(target=deleteRepo, args=(120, (i - 1) if i > 0 else (len(frames) - 1))).start()
				print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] =>"),'Waiting to draw next frame')
				sleep(30)
			else: print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] =>"), 'Error generating script with Gitfiti.py')
		else: print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] =>"), 'Error creating repo: ', r.content, r.status_code)

print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] =>"), 'Deleting all "' + REPO_PREFIX + '*" repositories')
for i, frame in frames: requests.delete('https://api.github.com/repos/' + USERNAME + '/' + REPO_PREFIX + str(i), headers={'Authorization': 'TOKEN ' + TOKEN})
