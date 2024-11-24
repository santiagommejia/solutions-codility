def solution(S, P, Q):
    sumA = [0]
    sumC = [0]
    sumG = [0]
    sumT = [0]
    for elem in S:
        sumA.append(sumA[len(sumA) - 1] + (1 if elem == 'A' else 0))
        sumC.append(sumC[len(sumC) - 1] + (1 if elem == 'C' else 0))
        sumG.append(sumG[len(sumG) - 1] + (1 if elem == 'G' else 0))
        sumT.append(sumT[len(sumT) - 1] + (1 if elem == 'T' else 0))
    results = []
    for i in range(len(P)):
        start = P[i]
        end = Q[i]
        if sumA[end + 1] - sumA[start] > 0:
            results.append(1)
        elif sumC[end + 1] - sumC[start] > 0:
            results.append(2)
        elif sumG[end +1] - sumG[start] > 0:
            results.append(3)
        else:
            results.append(4)
    return results