def solution(N):
    previousLsb = None
    currentBinaryGapCount = 0
    maxBinaryGapCount = 0
    isInBinaryGap = False
    while N:
        lsb = N & 1
        if previousLsb is None:
            previousLsb = lsb
            N >>= 1
            continue
        isInBinaryGap = (lsb == 0 and previousLsb == 1) or isInBinaryGap
        if lsb == 1 and previousLsb == 0:
            isInBinaryGap = False
            maxBinaryGapCount = max(maxBinaryGapCount, currentBinaryGapCount)
            currentBinaryGapCount = 0
        else:
            currentBinaryGapCount += 1 if isInBinaryGap else 0
        N >>= 1
        previousLsb = lsb
    return maxBinaryGapCount
