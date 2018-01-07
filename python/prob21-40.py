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
