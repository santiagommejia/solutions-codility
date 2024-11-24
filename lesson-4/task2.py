def solution(A):
    foundNumbers = set()
    N = len(A)
    for elem in A:
        if elem in foundNumbers or elem > N:
            return 0
        else:
            foundNumbers.add(elem)
    return 1
