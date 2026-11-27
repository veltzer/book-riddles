#!/usr/bin/env python

""""
Solution
"""

data1: list[list[int | None]] = [[ 1,2,3], [4,5,6], [7,8,9]]
data2: list[list[int | None]] = [[ 1,2,3], [4,5,6], [7,8,9]]

def spiral_recursive(d: list[list[int | None]], x: int, y: int) -> None:
    # print(x,y)  # noqa: ERA001  teaching: kept in the comment for the reader
    if x>=len(d) or y>=len(d[x]):
        return
    if x<0 or y<0:
        return
    if d[x][y] is None:
        return
    # print(x,y)  # noqa: ERA001  teaching: kept in the comment for the reader
    print(d[x][y])
    d[x][y]=None
    spiral_recursive(d, x, y+1)
    spiral_recursive(d, x+1, y)
    spiral_recursive(d, x, y-1)
    spiral_recursive(d, x-1, y)


def spiral_non_recursive(d: list[list[int | None]]) -> None:
    num_elements=len(d)*len(d[0])
    direction_pos = 0
    directions = [ (0,1), (1,0), (0,-1), (-1,0), ]
    direction = directions[direction_pos]
    x,y = 0,0
    num_printed = 0
    while num_printed<num_elements:
        # print(x,y)  # noqa: ERA001  teaching: kept in the comment for the reader
        print(d[x][y])
        d[x][y]=None
        num_printed+=1
        new_x=x+direction[0]
        new_y=y+direction[1]
        if new_x>=len(d) or new_y>=len(d[new_x]) or new_x<0 or new_y<0 or d[new_x][new_y] is None:
            direction_pos+=1
            direction_pos%=4
            direction = directions[direction_pos]
            new_x=x+direction[0]
            new_y=y+direction[1]
        x=new_x
        y=new_y

spiral_recursive(data1, 0, 0)
print("==========================")
spiral_non_recursive(data2)
