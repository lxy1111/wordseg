import sys

from wordseg import HMM

print(sys.argv)


filepath = sys.argv[1]


hmm =  HMM()
hmm.train(filepath)

text = '这是一个非常棒的方案！'
res = hmm.cut(text)
print(text)
print(str(list(res)))