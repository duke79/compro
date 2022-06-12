T = input()
T = int(T)

for i in range(T):
    try:
        N, a, b = input().split(" ")

        N = int(N)
        a = int(a)
        b = int(b)

        A = input()

        if (N % a) >= b or N < a:
            print("ALICE")
        else:
            print("BOB")
    except ValueError as e:
        pass
