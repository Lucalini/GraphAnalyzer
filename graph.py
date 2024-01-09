from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other Attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.color = None
        self.visited = False


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        # This method should call add_vertex and add_edge!!!
        self.graph = {}

        f = open(filename)
        f2 = f.readlines()
        f.close()
        f2 = [line.strip() for line in f2]
        for line in f2:
            vertices = line.split()
            v1 = vertices[0]
            v2 = vertices[1]
            self.add_vertex(v1)
            self.add_vertex(v2)
            self.add_edge(v1, v2)


    def add_vertex(self, key):
        # Should be called by init
        '''Add vertex to graph only if the vertex is not already in the graph.'''
        if key not in self.graph:
            self.graph.update({key: Vertex(key)})

    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex ID's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.graph[v1].adjacent_to.append(v2)
        self.graph[v2].adjacent_to.append(v1)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the ID. If ID is not in the graph, return None'''
        if key in self.graph:
            return self.graph[key]
        else:
            return None
    def get_vertices(self):
        '''Returns a list of ID's representing the vertices in the graph, in ascending order'''
        vertices_list = sorted(list(self.graph))
        return vertices_list

    def conn_components(self): 
        '''Return a Python list of lists.  For example: if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending alphabetical order) in the connected component represented by that list.
           The overall list will also be in ascending alphabetical order based on the first item in each sublist.'''
        #This method MUST use Depth First Search logic!
        keys = self.graph.keys()
        for key in keys:
            self.graph[key].visited = False
        componenets_stack = Stack(3 *len(keys))
        componenets_list = []
        for key in keys:
            root = self.graph[key]
            if root.visited is True:
                continue
            componenets_stack.push(root)
            running_list = [key]
            while not componenets_stack.is_empty():

                current_vertex = componenets_stack.peek()
                current_vertex.visited = True
                for i in range(len(current_vertex.adjacent_to)):
                    vertex = self.graph[sorted(current_vertex.adjacent_to)[i]]
                    if not vertex.visited:
                        componenets_stack.push(vertex)
                        running_list.append(vertex.id)
                        break
                    if len(current_vertex.adjacent_to) == 0 or (vertex.visited and i == len(current_vertex.adjacent_to) -1):
                        componenets_stack.pop()
            componenets_list.append(sorted(running_list))
        componenets_list.sort()
        return componenets_list

    def is_bipartite(self):
        '''Return True if the graph is bipartite, False otherwise.'''
        #This method MUST use Breadth First Search logic!

        keys = self.graph.keys()
        bipartite_queue = Queue(len(keys))
        for key in keys:
            self.graph[key].color = None

        for key in keys:
            root = self.graph[key]
            if root.color is None:
                root.color = "black"
            else:
                continue
            bipartite_queue.enqueue(root)
            while not bipartite_queue.is_empty():
                current_vertex = bipartite_queue.dequeue()
                current_color = current_vertex.color
                for adj_key in current_vertex.adjacent_to:
                    vertex = self.graph[adj_key]
                    if vertex.color is None:
                        if current_color == "black":
                            vertex.color = "red"
                        if current_color == "red":
                            vertex.color = "black"
                        bipartite_queue.enqueue(vertex)
                    elif vertex.color == current_color:
                        return False
        return True




