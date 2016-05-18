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
