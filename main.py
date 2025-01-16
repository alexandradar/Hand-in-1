#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:04:15 2025

@author: alexandra
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import heapq  # For priority queue implementation

def create_terrain_table(rows, cols, custom_values): #create a table as in the assignment

# This makes sure that the grid matches the specified rows and columns    
    if len(custom_values) != rows or any(len(row) != cols for row in custom_values): 
        raise ValueError("Custom values must match the dimensions of the table.")

    terrain_values = np.array(custom_values)
    return terrain_values        # returns the grid as a 2D array


def print_terrain_table(terrain_values):
    
    terrain_mapping = {
        1: 'White (1)',
        2: 'Green (2)',
        10: 'Red (10)'
    }

    print("Terrain Table:")
    for row in terrain_values:
        print([terrain_mapping[cell] for cell in row])


def plot_terrain(terrain_values, path=None):
    
    cmap = mcolors.ListedColormap(['#FFFFFF', '#008000', '#FF0000'])
    bounds = [0, 1.5, 5, 15]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    plt.figure(figsize=(8, 6))
    plt.imshow(terrain_values, cmap=cmap, norm=norm)

    if path:
        path_row, path_col = zip(*path)  
        plt.plot(path_col, path_row, color='blue', marker='o', markersize=5, label='Path')  

    ax = plt.gca()
 
    for i in range(terrain_values.shape[0]):
         for j in range(terrain_values.shape[1]):
            rect = plt.Rectangle(
                (j - 0.5, i - 0.5), 1, 1, fill=False, edgecolor='black', linewidth=1
            )
            ax.add_patch(rect)


    plt.colorbar(ticks=[1, 2, 10], label='Cost')
    plt.title('Terrain Map with Path')
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    plt.legend()
    plt.show()



custom_values = [
    [1, 1, 2, 2, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 10, 10, 2, 1],
    [1, 1, 1, 2, 2, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 2, 10, 10, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 10, 1, 1, 1, 1]
]


terrain_values = create_terrain_table(9, 6, custom_values)


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(terrain_values, start, goal, visited=None, path=None):
   
    if visited is None:
        visited = set()
    if path is None:
        path = []

    row, col = start
   
    if (row, col) == goal:
        path.append((row, col))  
        return path

    visited.add((row, col)) 
    path.append((row, col))   

  
    for direction in directions:
        next_row, next_col = row + direction[0], col + direction[1]

       
        if (0 <= next_row < len(terrain_values) and 0 <= next_col < len(terrain_values[0]) and
                (next_row, next_col) not in visited):
            result = dfs(terrain_values, (next_row, next_col), goal, visited, path)
            if result: 
                return result

    path.pop()  
    return None

def heuristic(a, b):
    
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def a_star(terrain_values, start, goal):
    
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))  

    g_cost = {start: 0}
    came_from = {}

    while open_set:
        _, current_g, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]

            if not (0 <= next_row < len(terrain_values) and 0 <= next_col < len(terrain_values[0])):
                continue

            tentative_g = current_g + terrain_values[next_row, next_col]

            if (next_row, next_col) not in g_cost or tentative_g < g_cost[(next_row, next_col)]:
                g_cost[(next_row, next_col)] = tentative_g
                f_cost = tentative_g + heuristic((next_row, next_col), goal)
                heapq.heappush(open_set, (f_cost, tentative_g, (next_row, next_col)))
                came_from[(next_row, next_col)] = current

    return None  

algorithm_choice = "A*" # Change this between "DFS" and "A*" to use Depth-First Search



start_position = (0, 1) 
goal_position = (7, 4)   

if algorithm_choice == "DFS":
    path = dfs(terrain_values, start_position, goal_position)
elif algorithm_choice == "A*":
    path = a_star(terrain_values, start_position, goal_position)



print_terrain_table(terrain_values)


plot_terrain(terrain_values, path)


if path:
    print("Path from Start to Goal:")
    print(path)
 
    total_cost = sum(terrain_values[row, col] for row, col in path[1:])
    print("Total cost of the path:", total_cost)
else:
    print("No path found from start to goal.")
