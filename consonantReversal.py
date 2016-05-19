
"""
    Given N strings, reverse and print each string such that the
    positions of its vowels remain unchanged but all
    its consonants are reversed

"""


N = "abcdefg"
v = "aeiuo"
# agfdecb
newString = []


def consonantReversal(N):
    for i in N:
        if i not in v:
            newString.append(i)
            revString = newString[::-1]

    for i in N:
        if i in v:
            index_i = N.index(i)
            revString.insert(index_i, i)


    return revString

consonantReversal(N)

