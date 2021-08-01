# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                A[i] = -1
                A[j] = -1
                break
    for i in range(0, len(A)):
        if A[i]>-1:
            return A[i]
