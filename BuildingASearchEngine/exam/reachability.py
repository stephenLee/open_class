#Reachability

#Single Gold Star

#Define a procedure, reachable(graph, node), that takes as input a graph and a
#starting node, and returns a list of all the nodes in the graph that can be
#reached by following zero or more edges starting from node.  The input graph is
#represented as a Dictionary where each node in the graph is a key in the
#Dictionary, and the value associated with a key is a list of the nodes that the
#key node is connected to.  The nodes in the returned list may appear in any
#order, but should not contain any duplicates.
"""
def reachable(graph, node):
    result=[]
    new_graph=graph
    for i in new_graph:
        if node == i:
            result.append(i)
            for ci in range(0,len(new_graph[i])):
                if new_graph[i][ci] in new_graph:
                    new_node=new_graph[i][ci]
                    del new_graph[i]
                    return result+reachable(new_graph, new_node)
            return result
"""

def dfs(graph, node, visited):
    if node in visited:
        return []
    visited.append(node)
    for neighbor in graph[node]:
        for visit in dfs(graph, neighbor, visited):
            if visit not in visited:
                visited.append(visit)
    return visited

def reachable(graph, node):
    return dfs(graph, node, [])
#For example,

graph = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}

#print reachable(graph, 'a')
#>>> ['a', 'c', 'd', 'b']

#print reachable(graph, 'd')
#>>> ['d', 'a', 'c', 'b']

#print reachable(graph, 'e')
#>>> ['e', 'a', 'c', 'd', 'b']
