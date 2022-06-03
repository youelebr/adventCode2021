with open("input.txt") as file:
    data = file.read().splitlines()
    
graph = {}

for line in data:
    edge= line.split("-")
    for i in range(2):
        if edge[i] not in graph:
            graph[edge[i]] = set()
        graph[edge[i]].add(edge[(i+1)%2])
        
# print(graph)

def explore(node, visited, joker):
    if node == "end":
        return 1
    if node.lower()==node and node in visited:
        if joker!=""or node=="start":
            return 0
        joker=node
    visited.add(node)
    sum_neighbors=0
    for ngb in graph[node]:
        sum_neighbors+= explore(ngb,visited,joker)
    if node in visited and joker!=node:
        visited.remove(node)
    return sum_neighbors
    
print(explore("start", set(),""))