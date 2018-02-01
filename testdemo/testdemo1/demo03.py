# coding=utf-8
s = 'abcde'
i = -1
for i in [None] + range(-1, -len(s), -1):
    print s[:i]

L = ["1", "3", "4", "2"]
L1 = [6, 4, 7, 8, 2]

for i in reversed(L1):
    print i

