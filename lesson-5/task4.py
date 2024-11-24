def solution(A):
    minAvg = 20000
    minAvgStartPos = 0
    for i in range(len(A) - 1):
        twoSum = A[i] + A[i + 1]
        twoAvg = twoSum / 2
        if twoAvg < minAvg:
            minAvg = twoAvg
            minAvgStartPos = i
        if i + 2 < len(A):
            threeSum = twoSum + A[i+2]
            threeAvg = threeSum / 3
            if threeAvg < minAvg:
                minAvg = threeAvg
                minAvgStartPos = i
    return minAvgStartPos
