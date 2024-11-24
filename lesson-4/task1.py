def solution(X, A):
    pathDict = {}
    pathSum = 0
    expectedSum = int(X * (X + 1)/2)
    for i in range(len(A)):
        path = A[i]
        if path not in pathDict:
            pathSum += path
            pathDict[path] = True
            if pathSum == expectedSum:
                return i
    return -1
