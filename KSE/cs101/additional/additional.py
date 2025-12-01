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

def unique_characters2(s: str):
    return len(s) == len(set(s))

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

lower = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
upper = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
len_ukr = len(lower) # 33
def cezar_crypt(text, shift):
    result = ''
    key_norm = shift % len_ukr
    for i in text:
        if i in lower:
            old_index = lower.find(i)

            new_index = (old_index + key_norm) % len_ukr

            result += lower[new_index]
        elif i in upper:
            old_index = upper.find(i)

            new_index = (old_index + key_norm) % len_ukr

            result += upper[new_index]
        else:
            result += i

    return result
def cezar_decrypt(text, shift):
    return cezar_crypt(text, -shift)