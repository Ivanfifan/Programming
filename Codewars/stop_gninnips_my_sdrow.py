def spin_words(sentence):
    split = sentence.split(' ')
    res = []
    for ch in split:
        if len(ch) >= 5:
            res.append(ch[::-1])
        else:
            res.append(ch)
    return ' '.join(res)

print(spin_words('I love dotaaaaaaa 2'))