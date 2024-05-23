# CSC 480: Artificial Intelligence I: 2024 Spring, Assignment #2

## Overview
- This is the homework of CSC 480: Artificial Intelligence I: 2024 Spring at DePaul University

## Prerequisites
- Python3 installed
- Prolog installed

## Instructions
### Problem1
```
$ cd ./assignment2
$ python3 ./src/problem1_backtracking.py
$ python3 ./src/problem1_random.py
```
### Problem3
```
$ swipl

    ?- [src/problem3_merge_sort].
    true.
    
    ?- mergeSort([], L).
    L = [].
    
    ?- mergeSort([2], L).
    L = [2].
    
    ?- mergeSort([4, 2, 3, 1], L).
    L = [1, 2, 3, 4] .
    
    ?- mergeSort([5, 4, 6, 2, 7, 3, 1, 8], L).
    L = [1, 2, 3, 4, 5, 6, 7, 8] 
```