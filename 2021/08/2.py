"""

Numbers and its segments size:

            0 (6)
    1 (2)
        2 (5)
        3 (5)
    4 (4)
        5 (5)
            6 (6)
    7 (3)
    8 (7)
            9 (6)

So, when segments are size 5 or 6 there is ambiguity.

(5) = 2,3,5
(6) = 6,9

Number 8 does not resolve anything because is an ALL lights on.
Numbers 1 is included in numbers 4 and 7.

So, with number 4 and number 7 we can set (8 as all-segment guide):

 aaaa     ....      aaaa
.    b   g    b    g    b
.    b   g    b    g    b
 ....     ffff      ffff
.    c   .    c    e    c
.    c   .    c    e    c
 ....     ....      dddd


                       a  b  c  d  e  f  g
                       -------------------
2 would have at least (1, 1, 0, 1, 1, 1, 0)
3 would have at least (1, 1, 1, 1, 0, 1, 0)
5 would have at least (1, 0, 1, 1, 0, 1, 1)

0 would have at least (1, 1, 1, 1, 1, 0, 1)
6 would have at least (1, 0, 1, 1, 1, 1, 1)
9 would have at least (1, 1, 1, 1, 0, 1, 1)

Comparisons:

    0 (6) contains three segments from 4 and three from 7
    6 (6) contains three segments from 4 and two from 7
    9 (6) contains four segments from 4 and three from 7

Now cases 2, 3 and 5.

3 contains all three segments from 7 and three but one from 4.
2 contains two but one segments from 7 and two minus two of 4.
5 contains two but one segment from 7 and three but one from 4.

Case 3 is simple. We only need to compare with 4.
Case 2 and 5 must be compared with 4 and 7.

"""


def look_for_069(l, d):
    seven = set(d['7'])
    four = set(d['4'])
    l = list(filter(lambda x: len(x) == 6, l))
    def f(l, s):
        # 0 is 3 + 3 from '4', '7'
        # 6 is 3 + 2 from '4', '7'
        # 9 is 4 + 3 from '4', '7'
        return [i for i in l if len(seven & set(i)) + len(four & set(i)) == s][0]
    return {'0': f(l, 6), '6': f(l, 5), '9': f(l, 7)}


def look_for_235(l, d):
    four = set(d['4'])
    seven = set(d['7'])
    l = list(filter(lambda x: len(x) == 5, l))

    def f25(l, s):
        # 2 is 2 + 2 segments from '4', '7'
        # 5 is 3 + 2 segments from '4', '7'
        return [i for i in l if len(seven & set(i)) + len(four & set(i)) == s][0]

    def f3(l):
        # It's simple, just three segments from '7'
        return [i for i in l if len(seven & set(i)) == 3][0]

    return {'2': f25(l, 4), '3': f3(l), '5': f25(l, 5)}


def decode(l, d):
    r = []
    for n in l:
        for k, v in d.items():
            if not set(v) ^ set(n):
                r.append(k)
                continue
    return int("".join(r))



def look_for_1478(l):
    def f(l,s):
        # There should be not a IndexError in a correct input
        return [i for i in l if len(i) == s][0]
    return {'1': f(l, 2), '4': f(l, 4), '7': f(l, 3), '8': f(l, 7)}

with open('input' ,'r') as f:
    s = []
    data = [n.split(' | ') for n in f.read().split('\n') if n]
    t = []
    for entry in data:
        t.append([entry[0].split(), entry[1].split()])

    c = 0
    for line in t:
        c += 1
        d = look_for_1478(line[0])
        d.update(look_for_069(line[0], d))
        d.update(look_for_235(line[0], d))

        # Decode and append to s
        s.append(decode(line[1], d))
    print(sum(s))




