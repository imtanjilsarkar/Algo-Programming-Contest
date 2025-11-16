import sys
sys.setrecursionlimit(3000)

def passwordCracker(passwords, loginAttempt):
    memo = {}

    def dfs(s):
        if s == "":
            return []
        if s in memo:
            return memo[s]

        for p in passwords:
            if s.startswith(p):
                res = dfs(s[len(p):])
                if res is not None:
                    memo[s] = [p] + res
                    return memo[s]

        memo[s] = None
        return None

    ans = dfs(loginAttempt)
    if ans is None:
        return "WRONG PASSWORD"
    else:
        return " ".join(ans)

t = int(input())
for _ in range(t):
    n = int(input())
    passwords = input().split()
    loginAttempt = input().strip()
    print(passwordCracker(passwords, loginAttempt))
