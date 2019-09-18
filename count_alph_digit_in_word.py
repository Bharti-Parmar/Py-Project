import re
digit=0
alph=0
print("enter the word")
word=input()
for i in word:
  if re.search("[a-z]",i):
    alph=alph+1
  elif re.search("[A-Z]",i):
    alph+=1
  elif re.search("[0-9]",i):
    digit+=1
print("total alphabets: "+str(alph))
print("total digits: "+str(digit))