def hanoi(posts):
    n = len(posts)
    target = 1
    moves = 0
    
    for i in range(n-1, -1, -1):
        if posts[i] != target:
            moves += 1
            target = 6 - target - posts[i]
    
    return moves

n = int(input())
posts = list(map(int, input().split()))
print(hanoi(posts))