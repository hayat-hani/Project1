A = [1, 2, 4, 6]
B = [2, 3, 6]
C = []
# C = A + B
# C.sort()
i = 0
j = 0
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        C.append(A[i])
        i = i + 1
    else:
        C.append(B[j])
        j = j + 1
while i < len(A):
    C.append(A[i])
    i = i +1
while j < len(B):
    C.append(B[i])
    j = j + 1
print(C)

# for i in range(len(A) + len(B)):
#     if A[i] < B[j]:
#         C.append(A[i])
#         i = i + 1
#     else:
#         C.append(B[j])
#         j = j + 1
#     if i == len(A) or j == len(B):
#         break
# for i in range(i, len(A)):
#     C.append(A[i])
# for i in range(j, len(B)):
#     C.append(B[j])