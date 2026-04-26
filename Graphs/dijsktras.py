import heapq

class Solution:

    def __init__(self, graph):
        self.graph = graph
        pass

    
    def getDistance(self, source):
        # we maintain a heap storing [distance, node]
        heap = []
        distance = [float('inf')] * len(self.graph)

        distance[source] = 0
        heapq.heappush(heap, [0, source])

        while heap:
            dist, node = heapq.heappop(heap)
            
            if dist > distance[node]:
                continue

            for neighbor, weight in self.graph[node]:
                dist_2_neighbor = dist + weight
                if dist_2_neighbor < distance[neighbor] :
                    distance[neighbor] = dist_2_neighbor
                    heapq.heappush(heap, [dist_2_neighbor, neighbor])
                                    

        return distance




if __name__ == "__main__":
    graph = {
        0 : [[1,2], [3,3]],
        1 : [[0,1], [2,1]],
        2 : [[1,1], [4,2], [5,2]],
        3 : [[0,1], [5,1]],
        4 : [[2,2]],
        5 : [[3,1], [2,2]]
    }

    solver = Solution(graph)
    solver.getDistance(2)


