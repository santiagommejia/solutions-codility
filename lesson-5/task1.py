def solution(A):
  zeroCount = 0
  result = 0
  for elem in A:
    if elem == 0:
      zeroCount += 1
    else:
      result += zeroCount
    if result > 1000000000:
      return -1
  return result

A = [0,1,0,1,1]
print(solution(A))