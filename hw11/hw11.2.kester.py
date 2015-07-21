#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #11 WOOT!!!
# November 24, 2014
# Functional programming
# Script 2
#---------------------------------------------------------


#print max(a*b for a in range(100,1000) for b in range(a,1000) if str(a*b) == str(a*b)[::-1])
# my first attempt was very simple, but I guess it doesn't meet the requirement


revNum = [[(x*y),x,y] for x in range(99,1000) for y in range(99,1000)]
revNumFind = lambda num : str(num) == str(num)[::-1]
revNumFindList = [num[0] for num in revNum]
revNum2 = filter(revNumFind, revNumFindList)
maxRev = max(revNum2)
rev = [revNum[x] for x in range(0,len(revNum)) if revNum[x][0]==maxRev][0]
print str(rev[1]),"+",str(rev[2]),"=",str(rev[0])



