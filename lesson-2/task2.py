def solution(A):
    oddMap = {}
    for i in range(len(A)):
        value = A[i]
        if value not in oddMap:
            oddMap[value] = 1
        else:
            oddMap[value] -= 1 
        if oddMap[value] == 0:
            del oddMap[value]
    for key in oddMap:
        return key
    return None
