Script to draw pixelart on github repository

Requirements:
    python3 and library Requests

Usage:
    [New Repository](https://github.com/new) => Create a new GitHub repository
    python3 Gitfiti.py -> Generates a bash file
    sh Gitfiti.sh -> Creates and pushes commits, will ask for username and password if not stored in system

Parameters:
    -u user -> Username (optional)
    -r n    -> Repository number (optional)
    -rm path -> Path to readme (optional)

If a parameter is missing it will be asked for interactively
