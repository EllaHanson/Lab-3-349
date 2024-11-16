import sys

if len(sys.argv) - 1 < 2:
    print("error need two words")
    exit()

word_1 = '-' + sys.argv[1].lower()
word_2 = '-' + sys.argv[2].lower()
n = len(word_1)
m = len(word_2)

E = [[0 for i in range(n)] for j in range(m)] #E[j][i]

for i in range(n):
    for j in range(m):
        if i == 0: 
            E[j][i] = j
            continue
        if j == 0: 
            E[j][i] = i
            continue

        option_1 = E[j-1][i-1] 
        if word_1[i] != word_2[j]:
            option_1 += 1
        option_2 = E[j][i-1] + 1
        option_3 = E[j-1][i] + 1

        E[j][i] = min(option_1, option_2, option_3)

print(E[m-1][n-1])
