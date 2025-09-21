from src.graphs_Egonzalez88 import sp
import os

# folder where data files are
DATA_FOLDER = "data"
EXAMPLES = ["example1.txt", "example2.txt", "example3.txt"]

for filename in EXAMPLES:
    filepath = os.path.join(DATA_FOLDER, filename)
    print(f"=== Running Dijkstra on {filename} ===")
    
    graph = {}
    with open(filepath, 'rt') as f:
        n = int(f.readline().strip())  # first line: number of vertices
        for line in f:
            s, d, w = map(int, line.strip().split())
            if s not in graph:
                graph[s] = {}
            graph[s][d] = w
    
    s = 0
    dist, path = sp.dijkstra(graph, s)
    
    print(f"Shortest distances from {s}: {dist}")
    print("Paths:")
    for d in sorted(path):
        print(f"spf to {d}: {path[d]}")
    print("\n")
