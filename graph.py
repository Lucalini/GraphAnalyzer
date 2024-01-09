from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    def __init__(self, key):
        self.id = key
        self.adjacent_to = []
        self.color = None
        self.visited = False


class Graph:
    def __init__(self, filename):
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
        if key not in self.graph:
            self.graph.update({key: Vertex(key)})

    def add_edge(self, v1, v2):
        # Should be called by init
        self.graph[v1].adjacent_to.append(v2)
        self.graph[v2].adjacent_to.append(v1)

    def get_vertex(self, key):
        if key in self.graph:
            return self.graph[key]
        else:
            return None
    def get_vertices(self):
        vertices_list = sorted(list(self.graph))
        return vertices_list

    def conn_components(self): 
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




