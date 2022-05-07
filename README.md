# Gitfiti

Script to draw images on github repository, it can also do animations now!   
Inspired from [gelstudios/gitfiti](https://github.com/gelstudios/gitfiti)  

Requirements: ```python3``` and ```GitHub CLI```.  
Works only for linux ATM.

## Usage:  

### Single
Executes the script a single time and generates a bash script to draw image.  
[New Repository](https://github.com/new) => Create a new GitHub repository  
Run: ```python3 Gitfiti.py``` -> Generates a bash file  
Run: ```sh Gitfiti.sh``` -> Creates and pushes commits, will ask for username and pa  ssword if not stored in system    
|Usage    | Description             |
|---------|-------------------------|
|-u USER  | Username (OPTIONAL)     |
|-r NAME  | Repo name (OPTIONAL)    |
|-t TOKEN | GitHub token (PUSH)(OPT)|
|-c NUMBER| Max commits/Day (OPT)   |
|-i SRC   | Path to image.json (OPT)|      

### Automatic
This mode is intended to be used in conjunction with CRONTAB to be executed once a week (Sundayt idk at what time), when the first row of a new column is added.  
It will delete the repo, create it again and upload the image automaticaly.  

Run: ```python3 GitfitiAutomatic.py -u USER -t TOKEN```

|Usage    | Description                     |
|---------|---------------------------------|
|-u USER  | GitHub Username                 |
|-t TOKEN | GitHub token (NEW & DELETE REPO)|
|-r NAME  | Repo name to use (OPTIONAL)     |
|-c NUMBER| Max commits/Day (OPTIONAL)      |

### Animation
This is the most demanding mode for both ends, it renders a frame after a certain ammount of time generating a somewat seemless animation.  
A running example can be found on my profile page (1 frame each 30 seconds): [GitHub/ilarramendi](https://github.com/ilarramendi)  
Frames are stored in: ```/frames```, and are rendered in alphabetical order in a loop, the number of frames can be any.  
With the default max number of commits and frames it can render at a speed of 1 frame / 30 seconds.  
Lowering the total ammount of commit will allow a faster framerate (lowering max commits or the actual colors inside each frame).  

Run: ```python3 GitfitiAnimation.py -u USER -t TOKEN```  

|Usage     | Description                          |
|----------|--------------------------------------|
|-u USER   | GitHub Username                      |
|-t TOKEN  | GitHub token (NEW & DELETE REPO)     |
|-r PREFIX | Prefix for repos: Repo_1 (OPTIONAL)  |
|-c NUMBER | Max commits/Day (OPTIONAL)           |
|-ut NUMBER| Time it takes to update a frame (OPT)|
|-ft NUMBER| Time between frames (OPTIONAL)       |
