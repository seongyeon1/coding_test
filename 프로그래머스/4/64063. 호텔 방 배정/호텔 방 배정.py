import sys
sys.setrecursionlimit(2000)


def solution(k, room_number):
    rooms = dict()
    for num in room_number:
        chk_in = find_emptyroom(num, rooms)

    return list(rooms)

def find_emptyroom(chk, rooms):
    if chk not in rooms:
        rooms[chk] = chk + 1 # 다음 방이 비었다고 명시
        return chk
    
    empty = find_emptyroom(rooms[chk], rooms)
    rooms[chk] = empty + 1
    return empty

