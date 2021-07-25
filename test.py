import sys

from wordseg import HMM

print(sys.argv)


text = sys.argv[1]


hmm =  HMM()
text = sys.argv[1]

res = hmm.cut(text)
print(text)
print(str(list(res)))