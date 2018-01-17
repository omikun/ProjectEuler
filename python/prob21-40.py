#problem 21 Amicable Numbers
def memoize(f):
    m = {}
    def helper(x):
        if x not in m:
            m[x] = f(x)
        return m[x]
    return helper
            
@memoize
def d(n):
    return sum(i for i in xrange(1, n/2+1) if n % i == 0)
        
def amicNum(n):
    return sum(i for i in xrange(1, n) if i == d(d(i)) and i != d(i) and d(i) < n)
 
#print d(220), ' ', d(284)   
#print "prob21: ", amicNum(10000)

#problem 22
def namesScores():
    l = ''
    with open('names.txt') as f:
        l = f.readline()
    names = l.replace('"', '').strip().split(',')
    #sort input by alphabetical order
    names.sort()
    #compute sum of each name * rank
    return sum((names.index(i)+1)*sum(ord(j)-ord('A') for j in i) for i in names)
        
print namesScores()


def prob24():
    l = range(10)
    reverseL = l[::-1]
    s1 = 1
    c = [0]
    l = rev([], l, c)
    print c, ' : ', l
    #algorithm: swap last 2, move next smallest to column 2, repeat until column 2 has largest in l[0:2], then move next smallest to column3 and repeat for all columns

def next_index(l):
    start = l[0]
    next = max(l)
    next_i = 0
    if start > max(l):
        print 'too large!'
        return -1
    for i in l:
        if i > start:
            next = min(i, next)
    #print 'given ', start, ' got ', next
    return l.index(next)

def printl(k, l, c):
    c[0] += 1
    if c[0] == 1000000:
        print k , l

def rev(k, l, c):
    if len(l) == 2:
        l.sort()
        printl(k, l, c)
        l = l[::-1]
        printl(k, l, c)
        return l
    else:
        l[1:] = rev(k + [l[0]], l[1:], c)
        while l[0] < max(l):
            #get next highest, sort in decending order
            idx = next_index(l)
            l[0], l[idx] = l[idx], l[0]
            #print k , l
            b = l[1:];
            b.sort()
            l[1:] = b
            l[1:] = rev(k + [l[0]], l[1:], c)
            if l[0]+1 > max(l):
                break
        l = l[::-1]
        return l

#prob24()

def prob25():
    n = 2
    f = 1
    p = 1
    while f < 10 ** 999:
        n += 1
        f, p = f + p, f
    print n, ' fib: ', len(str(f))


#prob25()

def prob26():
    'calculate remainder cycle length'
    d = max(range(2, 1000), key=recip_len)
    print d

def recip_len(i):
    rems = {}
    rem = 1
    count = 0
    while True:
        rem = rem * 10 % i
        if rem in rems:
            return count
        rems[rem] = 1 #arbitrary
        count += 1

#prob26()

def memoize(f):
    m = {}
    def helper(x):
        if x not in m:
            m[x] = f(x)
        return m[x]
    return helper

import math
@memoize
def isPrime(n):
    if n < 2:
        return False
    if n == 2: 
        return True
    if n % 2 == 0:
        return False
    for i in xrange(3, int(math.sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True
        
def prob27():
    print max(((a, b) for a in xrange(-1000, 1001) for b in xrange(-1000, 1001)), key=maxPrime)

def maxPrime(ab):
    a, b = ab
    for n in xrange(0, 1000):
        if not isPrime(n**2 + a*n + b):
            return n

#prob27()

def prob29():
    'distinct powers'
    print len(set(a ** b for a in xrange(2, 101) for b in xrange(2, 101)))
#prob29()

def prob30():
    'digit fifth powers'
    print sum(i for i in xrange(10, 1000000) if equal_sum_fifth_power_digit(i))

def equal_sum_fifth_power_digit(n):
    l = [int(i) for i in str(n)]
    if n == sum(m ** 5 for m in l):
        print n
        return True
    else:
        return False

#prob30()

def prob31():
    'coin sums: find all permutations of 7 coins + 2lb that can make up 2lb'
    '200 * 2'
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    mc = 200
    count = [0]
    count_permutations(count, coins, mc)
    print count
    #start with 1*200, then 2*100, then 1*100 + 2*50, then 1*100 + 1* 50 +...
def count_permutations(count, coins, mc):
    if len(coins) == 0:
        if mc <= 0:
            count+=1
        return 

    if count[0] < 100:
        print mc, count, ' ', coins, ' ', mc / coins[-1]
    count[0] += 1
    for num in reversed(xrange(mc / coins[-1])):
        count_permutations(count, coins[:-1], mc - coins[-1]*num)
    return 0

        

#prob31()
from fractions import Fraction

def prob33():
    'digit cancelling fractions'
    #2 digit numerator/2digit denominator
    #with a digit in top and bottom that can cancel
    l = [(a, b) for a in xrange(10, 100) for b in xrange(a+1, 100) if isDCF(b, a)]
    a, b = 1, 1
    for i in l:
        a *= i[0]
        b *= i[1]
    print l
    print Fraction(a, b)

def isDCF(n, d):
    'from nayuki @ github'
    n0, n1 = n % 10, n // 10
    d0, d1 = d % 10, d // 10
    return (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == d0 * n)

def temp(a_, b_):
    'initial solution'
    a = str(a_)
    b = str(b_)

    newA = ''
    newB = ''

    can_digit_cancel = any(i for i in a if i in b)
    if not can_digit_cancel:
        return False

    for i in a:
        if i not in b:
            newA = i
    for i in b:
        if i != newA and i not in a:
            newB = i

    if newA == '' or newB == '':
        return False
    if a[0] == a[1] or b[0] == b[1] or a[1] == b[1]:
        return False

    newA = int(newA)
    newB = int(newB)

    if newB == 0:
        return False
    ret = Fraction(a_, b_) == Fraction(newA, newB)
    if ret:
        print a_, b_, ' == ', newA, newB
    return ret

#prob33()

@memoize
def fac(n):
    if n < 2:
        return 1
    return n * fac(n-1) 

def prob34():
    for n in xrange(10, 100000000):
        l = [fac(int(i)) for i in str(n)]
        s = sum(l)
        #print n, l
        if n == s:
            print n

#prob34()
        
def prob35():
    l = [i for i in xrange(2, 1000000) if isCircularPrime(i)]
    print l, len(l)

def isCircularPrime(n):
    m = str(n)
    for i in xrange(len(m)):
        if not isPrime(int(m[i:] + m[:i])):
            return False
    return True

#prob35()

def prob36():
    'binary and decimal palindrome'
    l = [i for i in xrange(1000000) if bp(i)]
    print l, sum(l)
    
def bp(i):
    b = bin(i)[2:]
    d = str(i)
    return b == b[::-1] and d == d[::-1]

#prob36()

def prob37():
    'truncatable primes'
    l = [i for i in xrange(10, 1000000) if is_trunctable_prime(i)]
    print l, len(l), sum(l)

def is_trunctable_prime(n):
    s = str(n)
    l = len(s)
    lr = len([i for i in xrange(len(s)) if isPrime(int(s[i:])) ]) == l
    rl = len([i for i in xrange(len(s)) if isPrime(int(s[:l-i])) ]) == l
    return lr and rl

prob37()
