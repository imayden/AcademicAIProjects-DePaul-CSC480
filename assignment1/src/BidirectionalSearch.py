
# Bidirectional Search

import json
import sys

class Node:
    def __init__(self, station):
        self.station = station
        self.children = []

class Graph:
    def __init__(self, data):
        self.nodes = {}
        self.build_graph(data)

    def build_graph(self, data):
        for node in data["nodes"]:
            self.nodes[node["name"]] = Node(node["name"])
        for arc in data["arcs"]:
            self.nodes[arc["first"]].children.append(self.nodes[arc["second"]])
            self.nodes[arc["second"]].children.append(self.nodes[arc["first"]])

    def bi_directional_search(self, start, goal):
        if start == goal:
            return [start], 1

        from_start = {start: None}
        from_goal = {goal: None}
        queue_start = [start]
        queue_goal = [goal]
        call_count = 0  

        while queue_start and queue_goal:
            call_count += 1  
            result, count = self.search_step(queue_start, from_start, from_goal, call_count)
            call_count += count
            intersection, inter_count = self.check_intersection(from_start, from_goal)
            call_count += inter_count
            if intersection:
                path, path_count = self.build_path(from_start, from_goal, intersection)
                call_count += path_count
                return path, call_count

            result, count = self.search_step(queue_goal, from_goal, from_start, call_count)
            call_count += count
            intersection, inter_count = self.check_intersection(from_start, from_goal)
            call_count += inter_count
            if intersection:
                path, path_count = self.build_path(from_start, from_goal, intersection)
                call_count += path_count
                return path, call_count

        return None, call_count

    def search_step(self, queue, this_side, other_side, current_count):
        local_count = 0  
        current = queue.pop(0)
        local_count += 1  
        current_node = self.nodes[current]
        for neighbor in current_node.children:
            local_count += 1  
            if neighbor.station not in this_side:
                this_side[neighbor.station] = current
                queue.append(neighbor.station)
                local_count += 2  
                current_count += 2 
        return queue, local_count

    def check_intersection(self, from_start, from_goal):
        visited_start = set(from_start.keys())
        visited_goal = set(from_goal.keys())
        intersection = visited_start & visited_goal
        inter_count = len(visited_start) + len(visited_goal)  
        if intersection:
            return intersection.pop(), inter_count
        return None, inter_count

    def build_path(self, from_start, from_goal, intersection):
        path = []
        step = intersection
        path_count = 1  
        while step:
            path.append(step)
            step = from_start[step]
            path_count += 1
        path.reverse()

        step = from_goal[intersection]
        while step:
            path.append(step)
            step = from_goal[step]
            path_count += 1

        return path, path_count

def load_data(file):
    with open(file, 'r') as file:
        data = json.load(file)
    return data

def main():
    if len(sys.argv) != 2:
        print("Invalid Command. Use command like: python3 src/BidirectionalSearch.py data/ctaTrain.json (python3 <filepath> <datapath>)")
        sys.exit(1)

    data_file = sys.argv[1]
    data = load_data(data_file)
    graph = Graph(data)

    while True:
        start = input("1st name (or 'quit' to quit): ")
        if start == 'quit':
            break
        if start not in graph.nodes:
            print("Invalid command, please try again")
            continue

        goal = input("2nd name (or 'quit' to quit): ")
        if goal == 'quit':
            break
        if goal not in graph.nodes:
            print("Invalid command, please try again")
            continue

        path, calls = graph.bi_directional_search(start, goal)
        if path:
            print(" -> ".join(path))
        else:
            print("Path not found")
        print(f"{calls} calls")

if __name__ == "__main__":
    main()
