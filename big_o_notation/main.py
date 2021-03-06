# O(long(n))
def func2(n):
    if n <= 1:
        return
    else:
        print(n)
        func2(n/2)

# O(n)
def func3(numbers):
    for num in numbers:
        print(num)

# O(n * log(n))
def func4(n):
    for i in range(int(n)):
        print(i,end=" ")
    print()
    if n <= 1:
        return
    func4(n/2)

# O(n**2)
def func5(numbers):
    for i in numbers:
        for j in numbers:
            print(i,j)
        print()

# stable sort -> 同一評価のアイテムの順序変わらない /unstable sort => 変わる