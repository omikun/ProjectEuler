import math

def reciprocal():
    for i in range(1,10):
        pass #print 1/float(i)
        
def fibonacci(i):
    if i == 1:
        return 1
    elif i == 2:
        return 2
    else:
        return fibonacci(i-1) + fibonacci(i-2)
        
def fibs(f):
    fibs = [0,1]
    for i in range(2, f+2):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
        
def fib():
    m = list(map(fibonacci, range(1,10)))
    #print 'sum fib(1-10) ', sum(m)
    n = fibs(50)
    #print 'more ', sum(n[i] for i in range(1, 40) if n[i] % 2 == 0 and n[i] < 4000000)
    #print 'done'
    
def findPrimes(n):
    #do it
    primes = [2]
    def isPrime(i):
        for p in primes:
            if i % p == 0:
                return False
        else:
            return True
            
    #for i in xrange(2, n):
    numPrime = 1
    i = 2
    while numPrime < n:
        i += 1
        if isPrime(i):
            primes.append(i)
            numPrime += 1
            
    return primes
    
#primes = findPrimes(10001)
#print primes[-1]

def sumSqDiff(n):
    sumSq = sum([i*i for i in range(n+1)])
    s = sum(range(n+1))
    print('sum: ', s)
    sqSum = s * s
    return sqSum - sumSq
    
#print sumSqDiff(100)

def largestPrimeFactor(n):
    pass#print max(getPrimeFactors(n))
    
def getPrimeFactors(n):
    primes = findPrimesN(n)
    l = [i for i in primes if n % i == 0]
    return l
        
    
def findPrimesN(n):
    #do it
    primes = [2]
    def isPrime(i):
        for p in primes:
            if i % p == 0:
                return False
        else:
            return True
            
    for i in range(2, n):
        if isPrime(i):
            primes.append(i)
    return primes
    
#print getPrimeFactors(13195)
#print largestPrimeFactor(600851475143)

def pyth(n):
    for i in range(1, n):
        for j in range(i+1, n-i):
            if i+j > n-i or i+j > n-j:
                break
            if i**2 + j**2 == (n-i-j)**2:
                #print "found!: ", i, j, n-i-j
                #print "abc = ", i * j * (n-i-j)
                return
            else:
                pass #print "nuh uh: ", i, j, n-i-j
    #print "nothing found"
    return
            
#pyth(1000)

def getFactors(n):
    count = 2
    for i in range(1, int(math.sqrt(float(n)))+1):
        if n % i == 0:
            count += 1
    return count
    
import itertools

def find_hdt(n):
    tn = 0
    for i in itertools.count():
        tn += i
        if getFactors(tn) >= n:
            return tn
        
#problem 14
from operator import itemgetter
#print find_hdt(500)


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper
    
@memoize
def collatz(n):
    count = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + collatz(n / 2)
    else:
        return 1 + collatz(3 * n + 1)

#collatz = memoize(collatz)    

def maxLenC(n):
    #print max(collatz(i) for i in range(n))
    m = [(i, collatz(i)) for i in range(n)]
    print(max(m, key=itemgetter(1))[0])
        
    
#problem 15
def latticePaths(n):
    #n is sqr matrix dimension
    #diag mat is like a binary tree,
    #count branches?, count paths
    pass
#problem 16
def powerdigitsum(n):
    return sum(int(i) for i in str(n)) 
#problem 17
def numLetterCount(n):
    # 1 2 3 4 5 6 7 8 9
    ones = "one two three four five six seven eight nine".split(' ')
    ones = [len(i) for i in ones]
    ones.insert(0, 0)
    # 10 20 30 40 50 60 70 80 90 
    tens = "ten twenty thirty forty fifty sixty seventy eighty ninty".split(' ')
    tens = [len(i) for i in tens]
    tens.insert(0,0)
    thousand = len('thousand')
    # 100 200 300 400 500 600 700 800 900 100
    hundred = len("hundred")
    count = 0
    for i in range(1000):
        count += ones[i % 10] + tens[int((i % 100) / 10)] + ones[int((i % 1000) / 100)]
        count += hundred if i > 99 else 0
    count += 3 + thousand
    return count
           
#print(numLetterCount(101))
    
#problem 18 max path sum from top of triangle down to bottom
triangle = [  # Mutable
	[75],
	[95,64],
	[17,47,82],
	[18,35,87,10],
	[20, 4,82,47,65],
	[19, 1,23,75, 3,34],
	[88, 2,77,73, 7,63,67],
	[99,65, 4,28, 6,16,70,92],
	[41,41,26,56,83,40,80,70,33],
	[41,48,72,33,47,32,37,16,94,29],
	[53,71,44,65,25,43,91,52,97,51,14],
	[70,11,33,28,77,73,17,78,39,68,17,57],
	[91,71,52,38,17,14,91,43,58,50,27,29,48],
	[63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
	[ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23],
]
def maxPathSum(t):
    for i in reversed(range(len(triangle) - 1)):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return str(triangle[0][0])

#print (mps(triangle))

def countSundays():
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    nly = sum(months)
    #count num days from 1900 to 2000
    firstSundays = 0
    days = 1
    for year in range(1900, 2001):
        for i, m in enumerate(months):
            if days % 7 == 0:
                firstSundays += 1
            days += m 
            if i == 1 and year % 4 == 0 and year % 400 != 0:
                days += 1
    return firstSundays
        
#print(countSundays())
    
#problem 20
import math
def facDigitSum(n):
    nfac = math.factorial(n)
    return sum(int(i) for i in str(nfac))
    
print "prob 20: ", facDigitSum(100)


import timeit

s = timeit.default_timer()
#maxLenC(1000000)
#print (powerdigitsum(32768))
e = timeit.default_timer()
print(( "timed: ", e - s))       
    
    
    
    

