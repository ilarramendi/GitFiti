from datetime import datetime, timedelta
import json
from os import path
import subprocess
from sys import argv
import requests

GITHUB_URL = "https://api.github.com"
USER = "ilarramendi"
REPO = "Gitfiti"
README = "/home/ilarramendi/scripts/Gitfiti/readme-example.md"
HEIGHT = 7
WIDTH = 53

start = datetime.now()
while (start.weekday() != 5): start += timedelta(days=1)
# 5 Colors (0, 1, 2, 3, 4)
# Pixelart size = 7 x 53
# GitFiti line example: GIT_AUTHOR_DATE=2021-07-06T12:00:00 GIT_COMMITTER_DATE=2021-07-06T12:00:00 git commit --allow-empty -m "gitfiti" > /dev/null
# TODO add gitfiti on commits graph



# region Parameters

# Image
if '-i' in argv and len(argv) > argv.index('-i') + 1: IMG_SRC = argv[argv.index('-i') + 1]
else: IMG_SRC = 'image.json'

with open(IMG_SRC) as data: image = json.load(data)
correct = True
if isinstance(image, list) and all([isinstance(line, list) for line in image]) and len(image) == 7:
    for linea in image:
        correct = all([isinstance(number, int) and number <= 4 and number >= 0 for number in linea]) and len(linea) == WIDTH
        if not correct: break            
else: correct = False

if not correct:
    print('Input image json is incorrect')
    exit()

# Username
if '-u' in argv and len(argv) > argv.index('-u') + 1:
    USER = argv[argv.index('-u') + 1]
else: 
    print('Username: ', end='')
    USER = input()

repos = requests.get(GITHUB_URL + '/users/' + USER + '/repos')
if repos.status_code != 200:
    print("Wrong username")
    quit()
    

# Repository
repos = list(map(lambda r: r['name'], repos.json()))

if len(repos) == 0:
    print('Create a repositorie first.')
    quit()

if '-rn' in argv and len(argv) >= argv.index('-rn') + 1 and argv[argv.index('-rn') + 1] in repos:
    REPO = argv[argv.index('-rn') + 1]
elif '-r' not in argv or len(argv) <= argv.index('-r') + 1:
    i = 0
    for repo in repos: 
        print(str(i) + ' ' + repo)
        i += 1

    number = input()
    if not(number.isdigit() and int(number) >= 0 and int(number) <= len(repos)):
        print("Wrong input")
        exit()
    REPO = repos[int(number)]
else: REPO = repos[int(argv[argv.index('-r') + 1])]

# Number of commits
if '-c' in argv and len(argv) > argv.index('-c') + 1:
    MAX_COMMITS = int(argv[argv.index('-c') + 1])
else: 
    print('Max Commits: ', end='')
    MAX_COMMITS = int(input())

#endregion



with open('Gitfiti.sh', 'w') as out:
    out.write('#!/usr/bin/env bash\n')
    out.write('rm -rf ' + REPO + '\n')
    out.write('git init ' + REPO + '\n')
    out.write('cd ' + REPO + '\n')
   
    for j in reversed(range(WIDTH)):
        for i in reversed(range(7)):
            date = (start - timedelta(days=363 - i - j * 7)).strftime('%Y-%m-%d')
            times = int(image[i][j] * MAX_COMMITS / 4)
            for i in range(times): out.write('GIT_AUTHOR_DATE=' + date + 'T12:00:00 git commit --allow-empty -m '' --allow-empty-message >> /dev/null\n')
    
    token = argv[argv.index('-t') + 1] if '-t' in argv and len(argv) >= argv.index('-t') + 1 else ''

    out.write('\ngit branch -M main\n')
    out.write('git remote add origin https://' + token + ('@' if len(token) > 0 else '') + 'github.com/' + USER + '/' + REPO + '.git\n')
    out.write('git push -f -u origin main\n')
    out.write('cd ..\n')
    out.write('rm -rf ' + REPO + '\n')

    
#if '-r' in argv: shellscript = subprocess.Popen(["sh ./Gitfiti.sh"], stdin=subprocess.PIPE)











