def solution(A):
    numbersSet = set()
    for elem in A:
        numbersSet.add(elem)
    for i in range(1, len(A) + 2):
        if i not in numbersSet:
            return i
    return
