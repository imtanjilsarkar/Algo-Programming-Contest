def solve():
    first_line = input().split()
    N = int(first_line[0])
    Q = int(first_line[1])

    words = []
    for i in range(N):
        words.append(input())

    words.sort()
    word_pos = {}
    for i in range(N):
        word_pos[words[i]] = i + 1 

    for i in range(Q):
        query = input().split()
        w = query[0]
        x = int(query[1])

        pos = word_pos[w]
        page = (pos - 1) // x + 1
        
        print(page)

solve()