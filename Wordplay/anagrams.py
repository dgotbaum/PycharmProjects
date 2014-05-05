import sys
def makeSet(file, ana):
    words = set()
    for line in file:
        line = line.split(" ")
        for word in line:
            word = word.strip("\n")
            if contains(word,ana):
                words.add(word)
    return words
def contains (s, word):

    if (len(s) == 0):
        return True , word
    elif s[0] in word:
        word = word.replace(s[0],"",1)
        return contains(s[1:],word)
    else:
        return False , ""

def grams(s, words, sofar):
    if s == "":
        if (len(sofar) >= MIN and len(sofar) <= MAX):
            print(sofar)
    else:
        for w in words:
            b, st = contains(w,s)
            if b:
                temp = sofar + [w]
                grams(st, words, temp)
def main():
    file = open("words2.txt","r")#open(input("File: "),"r")
    ana = "robopirate"#input("Word for Anagramming: ").strip("\n")
    global MIN, MAX
    MIN = eval(input("Minimum: "))
    MAX = eval(input("Maximum: "))
    words = makeSet(file, ana)
    grams(ana,words,[])

main()