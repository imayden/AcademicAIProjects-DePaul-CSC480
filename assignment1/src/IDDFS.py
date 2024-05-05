
# Iterative Deepening Depth First Search

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

    def IDDFS(self, start, goal):
        call_count = 0

        def DLS(node, goal, depth):
            nonlocal call_count
            call_count += 1
            if depth == 0 and node == goal:
                return [node.station]
            elif depth > 0:
                for child in self.nodes[node.station].children:
                    path = DLS(child, goal, depth - 1)
                    if path:
                        return [node.station] + path
            return None

        depth = 0
        while True:
            path = DLS(self.nodes[start], self.nodes[goal], depth)
            if path:
                return path, call_count
            depth += 1

def load_data(file):
    with open(file, 'r') as file:
        data = json.load(file)
    return data

def main():
    if len(sys.argv) != 2:
        print("Invalid Command. Use command like: python3 src/IDDFS.py data/ctaTrain.json (python3 <filepath> <datapath>)")
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

        path, calls = graph.IDDFS(start, goal)
        if path:
            print(" -> ".join(path))
        print(f"{calls} calls")

if __name__ == "__main__":
    main()
