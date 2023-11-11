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
* Python (3.x is recommended)
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

The general format of the files is that each file corresponds to the respective part in the problem statement. For example, `part1.py` corresponds to part 1 of the problem statement. 

### Part 1 -- adjacency list to adjacency matrix
In part1.py, the main function of concern is _adjacency_list_to_matrix_. It takes an adjacency list as an input (e.g. `a->b, b->c, c->d, d->b`), and returns an adjacency matrix (which is just a nested dictionary). 

This adjacency matrix can be displayed in a tabular format by utilizing the function `display_adjacency_matrix`, which takes an adjacency matrix as an output.

### Part 2 -- finding the optimal path that goes through every node
Part 2 was solved in part2.py. Particularly, the function _tsp_with_constraints_ (referring to the fact that Part 2 can be modelled after the Travelling Salesman Problem {TSP} ). The _tsp_with_constraints_ function takes an adjacency matrix (as referred to earlier) alongside a starting and an ending node. 

For ease of use, it is recommended to use the `find_optimal_path` wrapper function, which simply takes an input string (e.g. `a->b ($4), b->c ($5), c->d ($3), d->b ($7), a->c ($4), d->a ($1)`), a starting and an ending node. 

### Part 3 -- finding the optimal path that goes through every node but minimizing cooldown time
Part 3 adds further constraints to the problem in part 2 by adding another parameter to keep track of while minimizing cost. Similar to part 2, the majority of the logic is in _tsp_part3_, which takes an adjacency matrix, starting and ending nodes, and a max cooldown. 

Further matching part 2, it is recommended to use `find_optimal_path_part3`, which takes the starting intersection, ending intersection, max cooling time, and the input string. 

NOTE: All other functions not mentioned in any of these files are helper functions (for example, parsing the input string and extracting cost/cooldown time, or removing spaces)



