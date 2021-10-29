from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Fill this out with directions to walk
traversal_path = []

visited = {}

back_track = []

opposite_direction = {"n":"s", "s":"n", "e":"w", "w":"e"}

visited[player.current_room.id] = player.current_room.get_exits()

# pop version
while len(visited) < len(room_graph):
    curr_room = player.current_room.id
    if curr_room not in visited:
        visited[curr_room] = player.current_room.get_exits()
        prior_move = back_track[-1]
        visited[curr_room].remove(prior_move)
    if len(visited[curr_room]) == 0:
        prev = back_track.pop()
        traversal_path.append(prev)
        player.travel(prev)
    else:
        direction = visited[curr_room].pop()
        traversal_path.append(direction)
        back_track.append(opposite_direction[direction])
        player.travel(direction)


# directions = ["n", "e", "s", "w"]

# def next_clockwise(d, arr):
#     if d is None:
#         if "n" in arr:
#             return "n"
#         elif "e" in arr:
#             return "e"
#         elif "s" in arr:
#             return "s"
#         elif "w" in arr:
#             return "w"
#     possible_d = d
#     new_d = None
#     while new_d is None:
#         d_i = directions.index(possible_d)
#         if d_i == 3:
#             if directions[0] in arr:
#                 new_d = directions[0]
#             else:
#                 possible_d = directions[0]
#         else:
#             if directions[d_i + 1]  in arr:
#                 new_d = directions[d_i + 1]
#             else:
#                 possible_d = directions[d_i + 1]
#     return new_d


    
# # rotational version
# while len(visited) < len(room_graph):
#     curr_room = player.current_room.id
#     if curr_room not in visited:
#         visited[curr_room] = player.current_room.get_exits()
#         prior_move = back_track[-1]
#         visited[curr_room].remove(prior_move)
#     if len(visited[curr_room]) == 0:
#         prev = back_track.pop()
#         traversal_path.append(prev)
#         player.travel(prev)
#     else:
#         if len(back_track) == 0:
#             direction = next_clockwise(None, visited[curr_room])
#         else:
#             direction = next_clockwise(back_track[-1], visited[curr_room])
#         visited[curr_room].remove(direction)
#         traversal_path.append(direction)
#         back_track.append(opposite_direction[direction])
#         player.travel(direction)

# # random version
# while len(visited) < len(room_graph):
#     curr_room = player.current_room.id
#     if curr_room not in visited:
#         visited[curr_room] = player.current_room.get_exits()
#         prior_move = back_track[-1]
#         visited[curr_room].remove(prior_move)
#     if len(visited[curr_room]) == 0:
#         prev = back_track.pop()
#         traversal_path.append(prev)
#         player.travel(prev)
#     else:
#         index = random.randint(0, len(visited[curr_room]) - 1)
#         direction = visited[curr_room][index]
#         visited[curr_room].remove(direction)
#         traversal_path.append(direction)
#         back_track.append(opposite_direction[direction])
#         player.travel(direction)


# With just .pop(0) for directions: 1005 moves
# With just .pop() for directions: 1004 moves
# With clockwise directions: 991 moves
    # with n,e,s,w / e,s,w,n: 991 moves
    # with s,w,n,e / w,n,e,s: 998 moves
# With counter-clockwise directions: 1000 moves
# With random moves: 1005, 1009, 999, 997, 1006, 1000, 1002, 998, 992, 996, 1002, 993


# TRAVERSAL TEST - DO NOT MODIFY
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



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
