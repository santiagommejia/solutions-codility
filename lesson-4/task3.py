def solution(N, A):
    counterDict = {}
    previousMaxSoFar = 0
    maxSoFar = 0
    for x in A:
        if 1 <= x and x <= N:
            if x in counterDict:
                counterDict[x] += 1
                maxSoFar = max(maxSoFar, previousMaxSoFar + counterDict[x])
            else:
                counterDict[x] = 1
                maxSoFar = max(maxSoFar, previousMaxSoFar + 1)
        else:
            counterDict = {}
            previousMaxSoFar = maxSoFar
    result = [previousMaxSoFar + (counterDict[i] if i in counterDict else 0) for i in range(1, N+1)]
    return result
