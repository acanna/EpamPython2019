# problem 6
# answer = 250166416500
answer = sum(range(1001)) ** 2 - sum(map(lambda x: x ** 2, range(1001)))

# problem 9
# answer = [31875000]
answer = [
    b * c * (1000 - b - c)
    for c in range(1, 1001)
    for b in range(1, c)
    if
    0 < (1000 - b - c) < b < c and c ** 2 == b ** 2 + (1000 - b - c) ** 2
]

# problem 40
# пару секунд надо подождать
# answer = 210
# s = reduce(lambda x, y: x + y, map(str, range(2 * 10 ** 5)))
# answer = reduce(lambda x, y: x * y, [int(s[10 ** i]) for i in range(7)])

# problem 48
# answer = 9110846700
answer = sum(map(lambda x: x ** x % 10 ** 10, range(1, 1001))) % 10 ** 10


def is_armstrong(number):
    n = len(str(number))
    return number == sum(map(lambda x: int(x) ** n, str(number)))


assert is_armstrong(153), 'Число Армстронга'
assert not is_armstrong(10), 'Не число Армстронга'


def collatz_steps(n):
    assert isinstance(n, int)
    assert n > 0

    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps


def collatz_steps_recursive(n):
    return 0 if n == 1 else collatz_steps_recursive(
        n // 2 if n % 2 == 0 else 3 * n + 1) + 1


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152

assert collatz_steps_recursive(16) == 4
assert collatz_steps_recursive(12) == 9
assert collatz_steps_recursive(1000000) == 152
