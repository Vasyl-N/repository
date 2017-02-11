def solution(X, A):
    r = 0
    ar = []
    for i in range(0, len(A)):
        ar.append(A[i])
        r = i
        for j in range(0, len(ar) - 1):
            ar.sort
            if ar[j] + 1 == ar[j + 1]:
                return r
                break
