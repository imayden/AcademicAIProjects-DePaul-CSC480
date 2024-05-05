
# graph.py

import sys
from IDDFS import Graph as IDDFS_Graph, load_data as load_data_iddfs
from BidirectionalSearch import Graph as BiDir_Graph, load_data as load_data_bidir

def main():
    if len(sys.argv) != 2:
        print("Invalid Command. Use command like: python3 src/graph.py data/ctaTrain.json (python3 <filepath> <datapath>)")
        sys.exit(1)

    data_file = sys.argv[1]
    data_iddfs = load_data_iddfs(data_file)
    graph_iddfs = IDDFS_Graph(data_iddfs)
    graph_bidir = BiDir_Graph(data_iddfs)  # Assuming same data for both

    while True:
        start = input("1st name (or 'quit' to quit): ")
        if start == 'quit':
            break
        if start not in graph_iddfs.nodes:
            print("Invalid command, please try again")
            continue

        goal = input("2nd name (or 'quit' to quit): ")
        if goal == 'quit':
            break
        if goal not in graph_iddfs.nodes:
            print("Invalid command, please try again")
            continue

        path_iddfs, calls_iddfs = graph_iddfs.IDDFS(start, goal)
        if path_iddfs:
            print("IDDFS Path:", " -> ".join(path_iddfs))
        else:
            print("IDDFS Path not found")
        print(f"IDDFS Calls: {calls_iddfs}")

        path_bidir, calls_bidir = graph_bidir.bi_directional_search(start, goal)
        if path_bidir:
            print("Bi-Directional Search Path:", " -> ".join(path_bidir))
        else:
            print("Bi-Directional Search Path not found")
        print(f"Bi-Directional Search Calls: {calls_bidir}")

if __name__ == "__main__":
    main()
