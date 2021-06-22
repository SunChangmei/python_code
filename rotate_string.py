def rotateString(A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    if len(A) != len(B):
        return False
    elif len(A) == len(B) == 0:
        return True
    List = list()
    List.append(A)
    for i in range(1, len(A) - 1):
        print(A[i] + A[i + 1:] + A[:i])
        List.append(A[i] + A[i + 1:] + A[:i])
    List.append(A[-1] + A[:len(A) - 1])
    if B in List:
        return True
    return False

A = 'abcdef'
b = 'fabcdg'
res = rotateString(A, B)
print(res)

