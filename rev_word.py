#reverse of a word


def reverse(w):
    s=''
    for i in range(len(word)-1,-1,-1):
       s= word[i]
       return s
print("enter the word")
word=input()
rev=reverse(word)
print(rev)