from collections import deque

def hanoi(posts):
    n = len(posts)
    start = tuple(posts)
    goal = tuple([1] * n)

    if start == goal:
        return 0

    q = deque()
    dist = {}

    q.append(start)
    dist[start] = 0

    while q:
        state = q.popleft()
        moves = dist[state]

        top_disk = [None] * 5  

        for disk in range(1, n + 1):         
            rod = state[disk - 1]            
            if top_disk[rod] is None:
                top_disk[rod] = disk         

        for from_rod in range(1, 5):
            d = top_disk[from_rod]
            if d is None:
                continue  
            for to_rod in range(1, 5):
                if to_rod == from_rod:
                    continue

                t = top_disk[to_rod]
                if t is None or t > d:
                    # make new state
                    new_state = list(state)
                    new_state[d - 1] = to_rod
                    new_state = tuple(new_state)

                    if new_state not in dist:
                        dist[new_state] = moves + 1
                        if new_state == goal:
                            return moves + 1
                        q.append(new_state)

    return -1

n = int(input())
posts = list(map(int, input().split()))
posts = posts[:n]

ans = hanoi(posts)
print(ans)
