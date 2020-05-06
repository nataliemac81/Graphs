class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2, direction):
        """
        Add a directed edge to the graph.
        """
        reversed = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].update({v2: direction})
            self.vertices[v2].update({v1: reversed[direction]})
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def find_unexplored_paths(self, player_starting_room, visited_rooms):
        # create empty queue + enqueue a path to the starting vertex
        neighbors_to_visit = Queue()
        path = [player_starting_room]
        neighbors_to_visit.enqueue(path)
        # create set for visited vertices
        visited = set()
        while neighbors_to_visit.size() > 0:
            # dequeue the first path in the queue
            current_path = neighbors_to_visit.dequeue()
            # get the last room in the path
            last_room = current_path[-1]
            if last_room not in visited:
                # mark room as visited
                visited_rooms.add(last_room)
                # make new versions of current path with each neighbor added to them
                for next_room in self.vertices[last_room]:
                    if next_room not in visited_rooms:
                    # duplicate the path
                        new_path = path[1:]
                        return new_path
                    else:
                        new_path = path[:]
                    # add the neighbor
                        new_path.append(next_room)
                    # add the new path to the queue
                        neighbors_to_visit.enqueue(new_path)