#prob 56

def prob56():
    digitSums = []
    for i in xrange(1, 100):
        for j in xrange(1, 100):
            digitSums.append(sum(int(c) for c in str(i ** j)))
    return len(digitSums), ' ', max(digitSums)

#print prob56()

def prob57(n):
    a = 3
    b = 2
    count = 0
    for i in xrange(n):
        a, b = a + 2 * b, a + b
        if len(str(a)) > len(str(b)):
            count += 1
    return count

import math
#print prob57(1000)
def memoize(f):
    m = {}
    def helper(x):
        if x not in m:
            m[x] = f(x)
        return m[x]
    return helper

#@memoize
def isPrime(n):
    if n == 1:
        return True
    for i in xrange(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def prob58():
    'get spiral prime side length when prime ratio over diagonals < 10 percent'
    stride = 2
    num = 1
    primeCount = 0
    diagNumCount = 1
    while True:
        for i in xrange(4):
            num += stride
            diagNumCount += 1
            if isPrime(num):
                primeCount += 1
        r = primeCount / float(diagNumCount)
        #print "stride: ", stride, " ratio: ", r, " pC: ", primeCount, ' dNC: ', diagNumCount
        if (r < 0.1):
            break;
        stride += 2
    return stride + 1

#print prob58()

cipher = [79,59,12,2,79,35,8,28,20,2,3,68,8,9,68,45,0,12,9,67,68,4,7,5,23,27,1,
          21,79,85,78,79,85,71,38,10,71,27,12,2,79,6,2,8,13,9,1,13,9,8,68,19,7,
          1,71,56,11,21,11,68,6,3,22,2,14,0,30,79,1,31,6,23,19,10,0,73,79,44,2,
          79,19,6,28,68,16,6,16,15,79,35,8,11,72,71,14,10,3,79,12,2,79,19,6,28,
          68,32,0,0,73,79,86,71,39,1,71,24,5,20,79,13,9,79,16,15,10,68,5,10,3,
          14,1,10,14,1,3,71,24,13,19,7,68,32,0,0,73,79,87,71,39,1,71,12,22,2,14,
          16,2,11,68,2,25,1,21,22,16,15,6,10,0,79,16,15,10,22,2,79,13,20,65,68,
          41,0,16,15,6,10,0,79,1,31,6,23,19,28,68,19,7,5,19,79,12,2,79,0,14,11,
          10,64,27,68,10,14,15,2,65,68,83,79,40,14,9,1,71,6,16,20,10,8,1,79,19,
          6,28,68,14,1,68,15,6,9,75,79,5,9,11,68,19,7,13,20,79,8,14,9,1,71,8,13,
          17,10,23,71,3,13,0,7,16,71,27,11,71,10,18,2,29,29,8,1,1,73,79,81,71,59,
          12,2,79,8,14,8,12,19,79,23,15,6,10,2,28,68,19,7,22,8,26,3,15,79,16,15,
          10,68,3,14,22,12,1,1,20,28,72,71,14,10,3,79,16,15,10,68,3,14,22,12,1,
          1,20,28,68,4,14,10,71,1,1,17,10,22,71,10,28,19,6,10,0,26,13,20,7,68,
          14,27,74,71,89,68,32,0,0,71,28,1,9,27,68,45,0,12,9,79,16,15,10,68,37,
          14,20,19,6,23,19,79,83,71,27,11,71,27,1,11,3,68,2,25,1,21,22,11,9,10,
          68,6,13,11,18,27,68,19,7,1,71,3,13,0,7,16,71,28,11,71,27,12,6,27,68,2,
          25,1,21,22,11,9,10,68,10,6,3,15,27,68,5,10,8,14,10,18,2,79,6,2,12,5,18,
          28,1,71,0,2,71,7,13,20,79,16,2,28,16,14,2,11,9,22,74,71,87,68,45,0,12,9,
          79,12,14,2,23,2,3,2,71,24,5,20,79,10,8,27,68,19,7,1,71,3,13,0,7,16,92,
          79,12,2,79,19,6,28,68,8,1,8,30,79,5,71,24,13,19,1,1,20,28,68,19,0,68,
          19,7,1,71,3,13,0,7,16,73,79,93,71,59,12,2,79,11,9,10,68,16,7,11,71,6,
          23,71,27,12,2,79,16,21,26,1,71,3,13,0,7,16,75,79,19,15,0,68,0,6,18,2,
          28,68,11,6,3,15,27,68,19,0,68,2,25,1,21,22,11,9,10,72,71,24,5,20,79,
          3,8,6,10,0,79,16,8,79,7,8,2,1,71,6,10,19,0,68,19,7,1,71,24,11,21,3,0,
          73,79,85,87,79,38,18,27,68,6,3,16,15,0,17,0,7,68,19,7,1,71,24,11,21,
          3,0,71,24,5,20,79,9,6,11,1,71,27,12,21,0,17,0,7,68,15,6,9,75,79,16,15,
          10,68,16,0,22,11,11,68,3,6,0,9,72,16,71,29,1,4,0,3,9,6,30,2,79,12,14,
          2,68,16,7,1,9,79,12,2,79,7,6,2,1,73,79,85,86,79,33,17,10,10,71,6,10,
          71,7,13,20,79,11,16,1,68,11,14,10,3,79,5,9,11,68,6,2,11,9,8,68,15,6,
          23,71,0,19,9,79,20,2,0,20,11,10,72,71,7,1,71,24,5,20,79,10,8,27,68,6,
          12,7,2,31,16,2,11,74,71,94,86,71,45,17,19,79,16,8,79,5,11,3,68,16,7,
          11,71,13,1,11,6,1,17,10,0,71,7,13,10,79,5,9,11,68,6,12,7,2,31,16,2,11,
          68,15,6,9,75,79,12,2,79,3,6,25,1,71,27,12,2,79,22,14,8,12,19,79,16,8,
          79,6,2,12,11,10,10,68,4,7,13,11,11,22,2,1,68,8,9,68,32,0,0,73,79,85,84,
          79,48,15,10,29,71,14,22,2,79,22,2,13,11,21,1,69,71,59,12,14,28,68,14,28,
          68,9,0,16,71,14,68,23,7,29,20,6,7,6,3,68,5,6,22,19,7,68,21,10,23,18,3,
          16,14,1,3,71,9,22,8,2,68,15,26,9,6,1,68,23,14,23,20,6,11,9,79,11,21,79,
          20,11,14,10,75,79,16,15,6,23,71,29,1,5,6,22,19,7,68,4,0,9,2,28,68,1,29,
          11,10,79,35,8,11,74,86,91,68,52,0,68,19,7,1,71,56,11,21,11,68,5,10,7,
          6,2,1,71,7,17,10,14,10,71,14,10,3,79,8,14,25,1,3,79,12,2,29,1,71,0,10,
          71,10,5,21,27,12,71,14,9,8,1,3,71,26,23,73,79,44,2,79,19,6,28,68,1,26,
          8,11,79,11,1,79,17,9,9,5,14,3,13,9,8,68,11,0,18,2,79,5,9,11,68,1,14,13,
          19,7,2,18,3,10,2,28,23,73,79,37,9,11,68,16,10,68,15,14,18,2,79,23,2,10,
          10,71,7,13,20,79,3,11,0,22,30,67,68,19,7,1,71,8,8,8,29,29,71,0,2,71,27,
          12,2,79,11,9,3,29,71,60,11,9,79,11,1,79,16,15,10,68,33,14,16,15,10,22,73]
#adapted from nayuki on github
def prob59():
    bestkey = max(
        ( (x, y, z)
        for x in xrange(ord('a'), ord('z')+1)
        for y in xrange(ord('a'), ord('z')+1)
        for z in xrange(ord('a'), ord('z')+1)), 
        key=lambda key: get_score(decrypt(cipher, key)))
    print bestkey
    print sum(map(ord, decrypt(cipher, bestkey)))

def get_score(plaintext):
    count = plaintext.count('the')
    return count

def decrypt(ciphertext, key):
    def hash(i, c):
        return c ^ key[i % len(key)]
    plainint = [chr(hash(i, c)) for i, c in enumerate(ciphertext)]
    return ''.join(plainint)

def prob59_orig():
    'guess cipher from encrypted text, cipher must be 3 lower case letters'
    maxThe = 0
    decrypted = []
    key = []
    msg = []
    for c1 in xrange(ord('a'), ord('z')+1):
        for c2 in xrange(ord('a'), ord('z')+1):
            for c3 in xrange(ord('a'), ord('z')+1):
                guess = c1 + c2 + c3
                for i, t in enumerate(cipher):
                    decrypted += chr(t ^ guess[i%3])
                pMsg = ''.join(decrypted)
                numThe = pMsg.count('the')
                if numThe > maxThe:
                    maxThe = numThe
                    key = guess
                    print key, ' ', maxThe
                    msg = pMsg
                decrypted = []
    print sum(map(ord, msg))

#prob59()
import math
import itertools


@memoize
def isPrime(n):
    if n == 1:
        return True
    for i in xrange(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
                
@memoize
def next_prime(n):
    while True:
        if isPrime(n):
            return n
        n += 1
       
def fap(numPrimes, maxVal, depth=1):
    'iterate across all permutations of 5 primes under maxVal'
    if depth == 0:
        yield
    while numPrimes[depth-1] < maxVal:
        np = next_prime(numPrimes[depth-1])
        numPrimes[depth-1] = np
        if depth > 0:
            numPrimes[depth-2] = np
        for i in fap(numPrimes, maxVal, depth - 1):
            yield i

def ig(l, d, maxVal):
    'iterative generator of all permu of val [1,maxVal] for d set'
    for i in xrange(d):
        1
def rg(l, d, maxVal):
    'recursive generator of all permu of 1,maxVal] for d size set'
    if d > 0:
        r = rg(l, d-1, maxVal)
    while l[d] < maxVal:
        l[d] += 1
        if d > 0:
            l[d-1] = l[d]
            r.next()
        yield 
        
def gen():
    for i in xrange(5):
        yield i
    
def prob60():
    'prime pair sets: a set of 5 primes that, when any pair are concatenated in any order, also results in a prime'
    primeSet = [2, 3, 5, 7, 9]
    f = fap(primeSet, 1000, 5)
    for i in xrange(3):
        f.next()
        print primeSet
    
    #iterate across primes for a set of 5
    #check all concatenated pairs are also prime
    
#prob60()
l = [0, 0, 0, 0]
print 'before rg'
r = rg(l, 3, 30)
for i in xrange(5):
    r.next()
    print 'printing: ', l
