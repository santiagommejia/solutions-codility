def solution(A):
    uniqueSet = set()
    for elem in A:
        uniqueSet.add(elem)
    return len(uniqueSet)