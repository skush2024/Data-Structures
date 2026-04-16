from collections import deque

class Graph:

    def __init__(self, dependency:dict):
        self.graph = dependency


    def genPaths(self, start, dest):
        paths = []

        def bfs():
            queue = deque()
            queue.append((start, [start])) # we store (node, path)

            while queue :
                node, path = queue.popleft()
                
                if node == dest :
                    paths.append(path)
                    continue

                for neighbor in self.graph[node]:
                    if neighbor not in path:
                        queue.append((neighbor, path + [neighbor]))
            
        def dfs(node,dest, visited=[]):
            visited.append(node)
            
            if node == dest:
                paths.append(visited.copy())
            
            else:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        dfs(neighbor, dest,visited)
            
            visited.pop()

        

        bfs()
        print(paths)

if __name__ == "__main__":
    graph = {
        "home" : ["coffee shop", "gym", "park"],
        "coffee shop" : ["park"],
        "gym" : ["book store"],
        "book store" : ["park"],
        "park" : []
    }

    solver = Graph(graph)
    solver.genPaths("home", "park")