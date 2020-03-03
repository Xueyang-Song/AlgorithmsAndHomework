# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)



def fibonacci_number(n):
    assert 0 <= n <= 45


    a=1
    b=1
    if  n<=1:
        return n
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number_naive(input_n))
    print(fibonacci_number(input_n))

