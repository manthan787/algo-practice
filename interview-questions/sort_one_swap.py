def solution(A):
    n = len(A)
    if n == 0 or n == 1:
        return True
    culprit, potential_swap = -1, -1
    for i in range(1, n):
        if A[i - 1] > A[i]:
            culprit = i - 1
            break
    while i + 1 < n and A[i] == A[i + 1]:
        i += 1

    for j in range(i + 1, n):
        if A[j - 1] > A[j]:
            return False
        if A[j] > A[culprit]:
            potential_swap = j - 1
            break
    
    if culprit == -1:
        return True
    if i == n - 1:
        if A[i] < A[culprit]:
            potential_swap = i
    if potential_swap == -1:
        return False    
    A[culprit], A[potential_swap] = A[potential_swap], A[culprit]

    for i in range(potential_swap + 1, n):
        if A[i - 1] > A[i]:
            return False
    
    return True


print(solution([1, 5, 3, 3, 7]))
print(solution([1, 5, 3]))
print(solution([5, 1, 3]))
print(solution([1, 3, 7, 4]))
print(solution([1, 5, 3, 8, 7]))
print(solution([1, 3, 5]))
print(solution([1, 3, 5, 3, 4]))
print(solution([3, 1, 4, 3, 4]))
print(solution([1, 7, 2, 2, 2]))
print(solution([2, 1]))
