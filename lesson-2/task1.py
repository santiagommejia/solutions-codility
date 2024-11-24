def solution(A, K):
    sizeA = len(A)
    if sizeA == 0:
        return A
    K %= sizeA
    breakPoint = sizeA - K
    return A[breakPoint : ] + A[0 : breakPoint]
