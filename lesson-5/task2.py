from math import ceil, floor

def solution(A,B,K):
  if A == B:
    return 1 if A % K == 0 else 0
  elif B - A < K:
    return 1 if A <= ceil(A/K) * K <= B else 0
  else:
    return floor(B/K) - ceil(A/K) + 1