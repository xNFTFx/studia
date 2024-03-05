a = [1,2 ]
i = 9

def ai(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return  (ai(n-2) - ai(n-1))*ai(n-1)

print(ai(i))