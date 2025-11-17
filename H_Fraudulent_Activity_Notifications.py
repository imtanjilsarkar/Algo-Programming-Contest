def activityNotifications(expenditure, d):
    count = [0] * 201
    notifications = 0
    
    for i in range(d):
        count[expenditure[i]] += 1

    def get_median():
        total = 0
        if d % 2 == 1: 
            for i in range(201):
                total += count[i]
                if total > d // 2:
                    return i
        else: 
            first = None
            for i in range(201):
                total += count[i]
                if total >= d // 2 and first is None:
                    first = i
                if total >= d // 2 + 1:
                    return (first + i) / 2

    for i in range(d, len(expenditure)):
        median = get_median()
        
        if expenditure[i] >= 2 * median:
            notifications += 1

        count[expenditure[i-d]] -= 1
        count[expenditure[i]] += 1
    
    return notifications

n, d = map(int, input().split())
expenditure = list(map(int, input().split()))
print(activityNotifications(expenditure, d))