## project_IA Taquin_Augustin_Amelie

Building a taquin (n-sliding puzzle) and solving it with different search algorithms


## Necessary Modules:

pip install 'prompt_toolkit'

pip install 'heapdict'

sudo apt install python3-tk

## 

## Running the code

#### 

#### A first way, the GUI

run test_interface.py file (python3 test_interface.py)

In the interface you can choose the size of your taquin
(3, 8, 15, ...) and mix it several time or choose it directly thanks to
file button (you have to first write your taquin in fichier.txt)
Then you can solve it by moving the tiles directly on the screen or
thanks to different buttons which get the solution (path)

#### 

#### Second way: solve.py


This is what we used to compare in a rigorous way the different algorithms. We get the average of complexities we are measuring(space and time complexity).

Modify the parameters may be changed directly on the python file (lines 12 to 23)

test_methods is a list which decides which algorithms will be used to compare (by including them in the list or not)

Including 1 will select A* whith h1, 2 will select A* whith h2, 3 will select the UCS(=BFS) algorithm and finally 4 will select the bidirectional search algorithm. (if test_methods = [2 , 4] only these will be run, which is useful for the bigger games)

number_tests will be the number of games solved. Taking a large amount will make the result less dependent on the particular instances. Note that the algorithm will then be run on the same games to avoid comparing 2 different things (Only n games in total are generated, each solved by every measured method).

check_frontier takes a boolean which determines if we compute the space complexity or not

game_number takes the size of the game tested (3, 8, 15, …) as it makes no sense to take games of different sizes because of the exponential increase in complexity.

timelimit a bool, which sets a timelimit for the bool functions or not

n_time the timelimit in seconds
