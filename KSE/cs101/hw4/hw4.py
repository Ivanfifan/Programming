def find_primes(a: int,b: int):
    prime_list = []
    for num in range(a,b + 1):
        if num < 2:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            prime_list.append(num)

    return prime_list

def unique_characters(s: str):
    freq = {}
    for i in s:
        freq[i] = freq.get(i,0) + 1

    for num in freq.values():
        if num >= 2:
            return False
    return True

def fibonaci(a):

    if a <= 0:
        return []
    if a == 1:
        return [1]

    fib_seq = [1,1]
    for i in range(2,a):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])

    return fib_seq


print(fibonaci(6))

def swap(s: str):
    result = []
    for i in s:
        if i.isupper():
            result.append(i.lower())
        elif i.islower():
            result.append(i.upper())
        else:
            result.append(i)

    return "".join(result)


print(swap('Я гЕй'))


def cezar(text,key):
