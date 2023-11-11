# UTEK 2023 Programming Competition Team 4

This is the repository for the University of Toronto Engineering Kompetitions (UTEK) 2023 for the Programming competition.

The competition package with the Problem Statement is included in the `documents` folder.

Team members: 
* Krishna Advait Sripada
* Snehal Sobti
* Tanay Sinha
* Parthiv Varma

Setup Instructions
------------------

Pre-requisites: 
* Python 3.9
* Git

_Note: This instruction document assumes a Windows OS. Commands may vary on your OS. Google your equivalent commands if you are using another OS_

Type the following commands to confirm you meet the requirements.
```
python --version
git --version
```
If you do not, see https://python.org/ and https://git-scm.com/ for instructions for installation/upgrading. 

### Cloning the repository
Open your computer's command prompt. 
Navigate to the directory you wish to clone the repo using the command, and clone the repo using the following lines
```
cd /path/to/repository
git clone https://github.com/krishnaadvaitsripada/UTEK2023_Team4.git
```
You should see the repository in your file system now. 

The general format of the files is that each file corresponds to the respective part in the problem statement. For example, part1.py corresponds to part 1 of the problem statement. 

### Part 1 -- adjacency list to adjacency matrix
In part1.py, the main function of concern is _adjacency_list_to_matrix_. It takes an adjacency list as an input (e.g. a->b, b->c, c->d, d->b), and returns an adjacency matrix (which is just a nested dictionary). 

This adjacency matrix can be displayed in a tabular format by utilising the function _display_adjacency_matrix_, which takes an adjacency matrix as an output.

