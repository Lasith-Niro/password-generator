#!/usr/bin python3
import random
import re
from random import randint,shuffle

SYMBOLS = ['!','@','#','$','%','^','&','*','(',')']
KEYWORDS = ['sudo', 'linux', 'ubuntu', 'love', 'peace', 'python', 'install', 'regex']
def getRandNumber(n, m):
    return randint(n,m)

def userList(length, lst):
    shuffle(lst)
    f_s = SYMBOLS[getRandNumber(0, len(SYMBOLS)-1)]
    num_prefix = getRandNumber(10, 99)
    divider = len(lst)//2
    passWord = f_s.join(lst[divider:])+str(num_prefix)+"".join(lst[:divider])+'$'+randomWords(1, KEYWORDS)[0]
    newPassword = passWord[:length]
    return newPassword

# apt-get install wbritish
def randomWords(num, dictionary="/usr/share/dict/british-english"):
  r = random.SystemRandom() # i.e. preferably not pseudo-random
  try:
      f = open(dictionary, "r")
  except:
      f = dictionary
  count = 0
  chosen = []
  for i in range(num):
    chosen.append("")
  prog = re.compile("^[a-z]{5,9}$") # reasonable length, no proper nouns
  if(f):
    for word in f:
      if(prog.match(word)):
        for i in range(num): # generate all words in one pass thru file
          if(r.randint(0,count) == 0): 
            chosen[i] = word.strip()
        count += 1
  return(chosen)

def genPassword(num=4):
  return(" ".join(randomWords(num)))

# if(__name__ == "__main__"):
#   print (genPassword())