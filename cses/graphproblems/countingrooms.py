"""
Problem link: https://cses.fi/problemset/task/1192
"""

def countRooms(rows, cols):

    roommap=[]

    # read the entire graph
    for row in range(rows):
        roommap.append(list(input()))

    total_rooms = 0

    visited = [[False] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if roommap[row][col] == '.' and not visited[row][col]:
                items = explore(row, col, roommap, rows, cols, visited)
                total_rooms += 1

    return total_rooms


def explore(row, col, roommap, rows, cols, visited):
    stck = []
    stck.append((row, col))
    items = 0
    while stck:
        item = stck.pop()

        if visited[item[0]][item[1]]:
            continue

        else:
            visited[item[0]][item[1]] = True
            items += 1
            for neighbours_index in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                adjacent_row = item[0] + neighbours_index[0]
                adjacent_col = item[1] + neighbours_index[1]

                if not (adjacent_row < 0 or adjacent_row >= rows or adjacent_col < 0 or \
                    adjacent_col >= cols or visited[adjacent_row][adjacent_col] or roommap[adjacent_row][adjacent_col] == '#'):
                    stck.append((adjacent_row, adjacent_col))

    return items

import sys
#print(sys.getrecursionlimit())
rows, cols = map(int, input().split(' '))
print(countRooms(rows, cols))











