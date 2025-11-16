def get_median(count, d):
    cum = 0

    if d % 2 == 1:
        mid = d // 2 + 1  
        for value in range(201):
            cum += count[value]
            if cum >= mid:
                return value * 1.0  
    else:
        first_mid = d // 2
        second_mid = first_mid + 1

        m1 = None
        m2 = None

        for value in range(201):
            cum += count[value]
            if m1 is None and cum >= first_mid:
                m1 = value
            if m2 is None and cum >= second_mid:
                m2 = value
                break
        return (m1 + m2) / 2.0


def activityNotifications(expenditure, d):
    count = [0] * 201  

    for i in range(d):
        count[expenditure[i]] += 1

    notifications = 0

    for i in range(d, len(expenditure)):
        median = get_median(count, d)

        if expenditure[i] >= 2 * median:
            notifications += 1

        old_value = expenditure[i - d]
        new_value = expenditure[i]

        count[old_value] -= 1
        count[new_value] += 1

    return notifications

n, d = map(int, input().split())
expenditure = list(map(int, input().split()))

ans = activityNotifications(expenditure, d)
print(ans)
