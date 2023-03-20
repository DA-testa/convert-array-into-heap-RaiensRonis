# python3
def parent(i):
    return (i - 1) // 2

def child_left(i):
    return 2 * i + 1

def child_right(i):
    return 2 * i + 2

def check(data, i, swaps)
    min = i 
    l = child_left(i)
    r = child_right(i)
    if l < len(data) and data[l] < data[min]:
        min = l
    if r < len(data) and data[r] < data[min]:
        min = r 
    if i != min:
        data[i], data[min] = data[min], data[i]


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -1, -1):
            check(data, i, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    assert len(swaps) <= 4 * n
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
        
if __name__ == "__main__":
    main()
