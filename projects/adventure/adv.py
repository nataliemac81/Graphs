from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "/Users/nataliemccroy/Desktop/Graphs/projects/adventure/maps/test_line.txt"
# map_file = "/Users/nataliemccroy/Desktop/Graphs/projects/adventure/maps/test_cross.txt"
# map_file = "/Users/nataliemccroy/Desktop/Graphs/projects/adventure/maps/test_loop.txt"
map_file = "/Users/nataliemccroy/Desktop/Graphs/projects/adventure/maps/test_loop_fork.txt"
# map_file = "/Users/nataliemccroy/Desktop/Graphs/projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

unexplored_path = '?'
room_exits = player.current_room.get_exits()
player_current_room = player.current_room.id
directions = ['n', 's', 'e', 'w']
random_dir = random.choice(directions)

def traverse_graph(self, starting_vertex)
    # create plan_to_visit stack and add starting vertex
    plan_to_visit = Stack()
    plan_to_visit.push(starting_vertex)
    # create a set for visited vertices
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

def find_unexplored_paths(self, starting_vertex, unexplored_path)

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
            if current_vertex == unexplored_path:
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

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



######
# UNCOMMENT TO WALK AROUND
######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
