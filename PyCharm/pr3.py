import sys

if __name__ == '__main__':
    A = tuple(map(int,input().split()))
    if len(A) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    s = 0
    for i in A:
        if abs(i) < 5:
            s += i
    print(s)