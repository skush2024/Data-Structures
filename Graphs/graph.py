from collections import deque

class Graph:

    def __init__(self, dependency:dict):
        self.graph = dependency


    def hasCycle(self):
        state = {node: 0 for node in self.graph}  # 0,1,2

        def dfs(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False

            state[node] = 1

            for neighbor in self.graph[node]:
                if dfs(neighbor):
                    return True

            state[node] = 2
            return False

        for node in self.graph:
            if state[node] == 0:
                if dfs(node):
                    return True

        return False





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
        0: [1],
        1: [2],
        2: [3],
        3: [1]  # cycle here: 1 -> 2 -> 3 -> 1
    }

    solver = Graph(graph)
    print(solver.hasCycle())