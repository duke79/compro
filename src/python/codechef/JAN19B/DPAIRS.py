N, M = input().split(" ")
N = int(N)
M = int(M)

A = input().split(" ")
A = [int(elem) for elem in A]
B = input().split(" ")
B = [int(elem) for elem in B]
A_sorted = [i[0] for i in sorted(enumerate(A), key=lambda x: x[1])]
B_sorted = [i[0] for i in sorted(enumerate(B), key=lambda x: x[1])]

A_i = 0
B_i = 0
As_turn = True
# print(A_sorted)
# print(B_sorted)
while len(A_sorted) > A_i and len(B_sorted) > B_i:
    print("%s %s" % (A_sorted[A_i], B_sorted[B_i]))
    if As_turn:
        # print("As_turn")
        As_turn = False
        A_i += 1
    else:
        # print("Bs_turn")
        As_turn = True
        B_i += 1
