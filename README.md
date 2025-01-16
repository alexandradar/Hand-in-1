# Terrain Pathfinding Visualization
This Python script provides a simple framework to visualize and compute paths across a terrain grid using two different pathfinding algorithms. 







## Features
#### Create terrain (create_terrain_table)
This part of the code, creates a grid terrain that takes in account the costum values for the table.

#### Print out terrain (print_terrain_table)
Here the it maps the numeric values for the different colors and prints out a readable table representation of the terrain grid. 

Where the colors and the cost are:
- White: Cost = 1
- Green: Cost = 2
- Red: Cost = 10

#### Plot terrain (plot_terrain)
Here it uses matplotlib to visualize the table with the colors and the corresponding values. 
Blue circles is also added to mark the path that it takes and the grid between the blocks.
Futher down the costum table is made with the value of each block.


### Pathfinding Algorithms:
There are two Algorithms used to make a path.

- Depth-First Search (DFS)
- A* (A-Star) Algorithm

#### Depth-First Search (DFS)
This is a reclusive algorithm that searches every vertices in a graph or data tree. 
In this code, it goes up and down until it hits the goal node. 

#### A*
The main task and motivation for the A* search algorithm is to find the shortest path from start to goal. 
Here it finds the shortest path that equals to 10.
#### Heuristic function: 
The Heuristic function that is being used here is the Manhattan Distance. 

#### Visualization:
Before it all gets plotet. It is possible to choose which algorithm you want to use by changing between A* or DFS, and choose the start position and the goal position. 

At the end the table gets plotet with the colors, values and the path. 




## Usage/Examples

Here you choose between using A* or DFS and set the start and goal position 

```python

algorithm_choice = "A*" # "DFS"

start_position = (0, 1) 
goal_position = (7, 4)

if algorithm_choice == "DFS":
    path = dfs(terrain_values, start_position, goal_position)
elif algorithm_choice == "A*":
    path = a_star(terrain_values, start_position, goal_position)
  
````
## How to use
The way to use the this program is by opening main.py and the change to which algorithm you want to use and the run then program. 



