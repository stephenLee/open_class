# Eulerian Tour Ver 1
#
# Write a function, `create_tour` that takes as
# input a list of nodes
# and outputs a list of tuples representing
# edges between nodes that  have an Eulerian tour.
#

def create_tour(nodes):
    tour = []
    l = len(nodes)
    for i in range(l):
        t = (nodes[i], nodes[(i+1) % l])
        tour.append(t)
    return tour


def create_tour_random(nodes):
    connected = []
    degree = {}
    unconnected = [n for n in nodes]
    tour = []
    #create a connected graph
    #first, pick two random nodes for an edge
    x = poprandom(unconnected)
    y = poprandom(unconnected)
    connected.append(x)
    connected.append(y)
    tour.append((x,y))
    degree[x] = 1
    degree[y] = 1
    

    #then, pick a random edge from the unconnected list and 
    #create an edge to it
    while len(unconnected) > 0:
        x = pickrandom(connected)
        y = poprandom(unconnected)
        connected.append(y)
        tour.append((x,y))
        degree[x] += 1
        degree[y] = 1

    #now make sure each node has an even degree.
    #have the problem of not adding a duplicate edge
    odd_nodes = [k for k, v in degree.items() if v % 2 == 1]
    even_nodes = [k for k, v in degree.item() if v % 2 == 0]
    #there will always be an even number of odd nodes
    #(the sum of degrees of a graph is even)
    #so we can just connect pairs of unconnected edges
    while len(odd_nodes) > 0:
        x = poprandom(odd_nodes)
        cn = check_nodes(x, odd_nodes, tour)
        if cn is not None:
            even_nodes.append(x)
            even_nodes.append(cn)
        else:
            #if we get here
            #the node is already connceted to all the odd nodes
            #so we need to find an even one to connect to
            cn = check_nodes(x, even_nodes, tour)
            #cn can not be None, and needs to be added to the odd node
            # list
            odd_nodes.append(cn)
            even_nodes.append(x)
    return tour
#########

def get_degree(tour):
    degree = {}
    for x, y in tour:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree

def check_edge(t, b, nodes):
    """
    t: tuple representing an edge
    b: origin node
    nodes: set of nodes already visited

    if we can get to a new node from `b` following `t`
    then return that node, else return None
    """
    if t[0] == b:
        if t[1] not in nodes:
            return t[1]
    elif t[1] == b:
        if t[0] not in nodes:
            return t[0]
    return None

def connected_nodes(tour):
    """return the set of nodes reachable from
    the first node in `tour`"""
    a = tour[0][0]
    nodes = set([a])
    explore = set([a])
    while len(explore) > 0:
        # see what other nodes we can reach
        b = explore.pop()
        for t in tour:
            node = check_edge(t, b, nodes)
            if node is None:
                continue
            nodes.add(node)
            explore.add(node)
    return nodes

def is_eulerian_tour(nodes, tour):
    # all nodes must be even degree
    # and every node must be in graph
    degree = get_degree(tour)
    for node in nodes:
        try:
            d = degree[node]
            if d % 2 == 1:
                print "Node %s has odd degree" % node
                return False
        except KeyError:
            print "Node %s was not in your tour" % node
            return False
    connected = connected_nodes(tour)
    if len(connected) == len(nodes):
        return True
    else:
        print "Your graph wasn't connected"
        return False


# Write a function, `count`
# that returns the units of time
# where each print statement is one unit of time
# and each evaluation of range also takes one unit of time

def count(n):
    return  2 + n + n*(n-1)/2

def clique(n):
    print "in a clique..."
    for j in range(n):
        for i in range(j):
            print i, "is friends with", j

# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    tour=[]
    for k,v in graph.items():
        tour.append[k]
    return tour




def test():
    nodes = [20, 21, 22, 23, 24, 25]
    tour = create_tour(nodes)
    return is_eulerian_tour(nodes, tour)

if __name__ == '__main__':
    print test()
    clique(4)
    print count(4)
