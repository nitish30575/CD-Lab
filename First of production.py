def FIR(str):
    try:
        if(not str[2].isupper()):
            first[str[0]].append(str[2])
            # return first[str[0]]
        else:
            for i in productions:
                if(i[0] == str[2]):
                    FIR(str[0]+i[1:])
                    if('$' in first[str[0]]):
                        FIR(str[0:2]+str[3:])
    except:
        pass


productions = []
n = int(input("How many productions?"))
first = {}
for i in range(n):
    productions.append(input())
    str = productions[i]
    if (str[0] not in first):
        first[str[0]] = []
    FIR(str)
for i in productions:
    FIR(i)
for i in first:
    print(i+"=", set(first[i]))
