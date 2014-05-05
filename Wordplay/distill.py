def insertionSort( WC ):
    sortcount = [("z",0)]
    for key in WC:
        i = 0
        while sortcount[i][1] > WC[key]:
            i = i + 1
        sortcount = sortcount[:i] + [(key,WC[key])] + sortcount[i:]
    return sortcount

def main():
    fileName = input("File: ")
    file = open(fileName,"r")
    n = eval(input("Number: "))
    wordcount = {}
    for line in file:
        line = line.split(" ");
        for word in line:
            word = word.strip("!,*.\"\'?-\n")
            word = word.lower()
            if word == "":
                continue
            elif word in wordcount.keys():
                wordcount[word] = wordcount[word] +1
            else:
                wordcount[word] = 1
    sortcount = insertionSort(wordcount)
    commonWords = []
    for i in range (0,n):
        commonWords.append(sortcount[i][0])
    print(commonWords)
    f2 = open(fileName,"r")
    for line in f2:
        line = line.split(" ");
        for word in line:
            if word.strip("!,*.:\"'?-\n").lower() not in commonWords:
                print (word, end=" ")
main()