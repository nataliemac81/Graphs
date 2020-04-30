"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # plan to visit queue + add starting vert
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)

        # set for visited verts
        visited_vertices = set()

        # while plan_to_visit is not Empty:
        while plan_to_visit.size() > 0:
            # dequeue 1st vertex
            current_vertex = plan_to_visit.dequeue()
            if current_vertex not in visited_vertices:
                print(current_vertex)
                # mark it as visited + add to visited vertices
                visited_vertices.add(current_vertex)
                # add all unvisited neighbors to our queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create plan_to_visit stack and add starting vertex
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)
        # create a set for vited vertices
        visited_vertices = set()
        # while the stack is not Empty:
        while plan_to_visit.size() > 0:
            current_vertex = plan_to_visit.pop()
            if current_vertex not in visited_vertices:
                print(current_vertex)
                # mark vertex as visited + add to visited vertices
                visited_vertices.add(current_vertex)
                # then add unvisited neighbors to our stack
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex, plan_to_visit=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if plan_to_visit is None:
            plan_to_visit = set()

        plan_to_visit.add(starting_vertex)
        print(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in plan_to_visit:
                self.dft_recursive(neighbor, plan_to_visit)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create empty queue + enqueue a path to the starting vertex
        neighbors_to_visit = Queue()
        neighbors_to_visit.enqueue([starting_vertex])
        # create set for vsisted vertices
        visited_vertices = set()
        while neighbors_to_visit.size() > 0:
            # dequeue the first path in the queue
            current_path = neighbors_to_visit.dequeue()
            # get the last vertex in the path
            current_vertex = current_path[-1]
            if current_vertex not in visited_vertices:
                # check if it is the target
                if current_vertex == destination_vertex:
                    return current_path
                # mark vertex as visited
                visited_vertices.add(current_vertex)
                # make new versions of current path with each neighbor added to them
                for next_vertex in self.get_neighbors(current_vertex):
                    # duplicate the path
                    new_path = list(current_path)
                    # add the neighbor
                    new_path.append(next_vertex)
                    # add the new path to the queue
                    neighbors_to_visit.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        neighbors_to_visit = Stack()
        visited_vertices = set()
        # add the first vertex + an empty list
        neighbors_to_visit.push((starting_vertex, []))
        while neighbors_to_visit.size() > 0:
            # (current_vertex, path)
            current_vertex_plus_path = neighbors_to_visit.pop()
            # pull out the current vertex so its easier to read
            current_vertex = current_vertex_plus_path[0]
            # pull out the path so its easier to read
            current_path = current_vertex_plus_path[1]
            # make sure we haven't seen vertex already
            if current_vertex not in visited_vertices:
                # if the vertex is the dest, return it + the path we took to get there
                if current_vertex == destination_vertex:
                    updated_path = current_path + [current_vertex]
                    return updated_path

                # mark the vertex as visited
                visited_vertices.add(current_vertex)
                # add neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    updated_path = current_path + [current_vertex]
                    neighbors_to_visit.push((neighbor, updated_path))

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path += [starting_vertex]

        for neighbor in self.get_neighbors(starting_vertex):
            if not neighbor in path:
                path = self.dfs_recursive(neighbor, destination_vertex, path)
        return path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
