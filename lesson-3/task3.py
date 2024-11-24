def solution(A):
    left = A[0]
    right = sum(A[1:])
    diff = abs(left - right)
    for p in range(1, len(A)):
        newDiff = abs(left - right)
        if newDiff < diff:
            diff = newDiff
        left += A[p]
        right -= A[p]
    return diff
