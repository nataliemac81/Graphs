from room import Room
from player import Player
from world import World
from util import Stack, Queue
# from graph import Graph, find_unexplored_paths

import random
from ast import literal_eval

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

    def find_unexplored_paths(self, starting_vertex, rooms):
        # create empty queue + enqueue a path to the starting vertex
        neighbors_to_visit = Queue()
        path = [starting_vertex]
        neighbors_to_visit.enqueue(path)
        # create set for visited vertices
        visited = set()
        while neighbors_to_visit.size() > 0:
            # dequeue the first path in the queue
            first_path = neighbors_to_visit.dequeue()
            # get the last room in the path
            last_room = first_path[-1]
            if last_room not in visited:
                # mark room as visited
                visited.add(last_room)
                # make new versions of current path with each neighbor added to them
                for next_room in self.vertices[last_room]:
                    if next_room not in rooms:
                    # duplicate the path
                        new_path = path[1:]
                        return new_path
                    else:
                        new_path = path[:]
                    # add the neighbor
                        new_path.append(next_room)
                    # add the new path to the queue
                        neighbors_to_visit.enqueue(new_path)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "/Users/nataliemccroy/Desktop/Graphs/projects/adventure/maps/test_line.txt"
map_file = "/Users/nataliemccroy/Desktop/Graphs/projects/adventure/maps/test_cross.txt"
# map_file = "/Users/nataliemccroy/Desktop/Graphs/projects/adventure/maps/test_loop.txt"
# map_file = "/Users/nataliemccroy/Desktop/Graphs/projects/adventure/maps/test_loop_fork.txt"
# map_file = "/Users/nataliemccroy/Desktop/Graphs/projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# value of a path that we haven't visited
# unexplored_path = '?'

# current room available exits
# room_exits = player.current_room.get_exits()

# random direction (available room exits)
# random_dir = random.choice(room_exits)

visited_rooms = set()
player_starting_room = player.current_room.id

visited_rooms.add(player_starting_room)

def traverse_graph(visited_rooms, player):
    # instantiate graph
    graph = Graph()
    traversalPath = []
    # create plan_to_visit stack and add starting vertex
    # plan_to_visit = Stack()
    # plan_to_visit.push(player_starting_room)
    # # create a set for visited vertices
    # visited_rooms = set()
    # while the stack is not Empty:
    while len(visited_rooms) < len(room_graph):
        current_room = player.current_room
        current_room_id = current_room.id
        current_room_directions = current_room.get_exits()
        room_map = {}
        graph.add_vertex(current_room_id)

        for direction in current_room_directions:
            room_in_direction = current_room.get_room_in_direction(direction).id
            room_map.update({room_in_direction: direction})

        for key in room_map:
            if key not in visited_rooms:
                graph.add_vertex(key)
        for key in room_map:
            graph.add_edge(current_room_id, key, room_map[key])

        for key in graph.vertices[current_room_id]:
            go_back = 0
            if key not in visited_rooms:
                direction = room_map[key]
                player.travel(direction)
                visited_rooms.add(key)
                traversalPath.append(direction)
                break
            go_back += 1
        
        if go_back >= 1:
            search_rooms = graph.find_unexplored_paths(current_room_id, visited_rooms)
            for r in search_rooms:
                current_room = player.current_room.id
                direction = graph.vertices[current_room]
                player.travel(direction)
                traversalPath.append(direction)
                visited_rooms.add(r)
    
    return traversalPath

traversal_path = traverse_graph(visited_rooms, player)


# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room.id)

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
