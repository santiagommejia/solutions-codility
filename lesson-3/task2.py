def solution(A):
    n = len(A) + 1
    expectedSum = int (n * (n + 1) / 2)
    actualSum = sum(A)
    return expectedSum - actualSum
