def permutation(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i + 1:]
            togther = front + back
            permutation(togther, letter + pocket)


print(permutation("ab"))
