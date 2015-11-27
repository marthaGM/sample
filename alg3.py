def changedp (A,V):
   a=[[0]*(A+1) for x in xrange(len(V))]
   for j in range (1,A+1):
      a[0][j]=j
   for i in range(1,len(V)):
      for j in range (1,A+1):
	if (j>=V[i]):
	   a[i][j]=min(a[i-1][j],1+a[i][j-V[i]])
	else:	
	   a[i][j]=a[i-1][j]
   minChange=a[len(V)-1][A]


   #the following code to trace back and find
   #values of c[i]  
   m=[-1]*len(V)
   x=len(V)-1
   m[x]=0
   y=A
   print a[x][y]
   value=1
   while (value>0):
      if(y<V[x]):
	x=x-1
	m[x]=m[x]+1
      else:
      	if ((a[x-1][y])<(a[x][y-V[x]]+1)):
	   x=x-1
	   m[x]=m[x]+1
	else:
	   y=y-V[x]
	   m[x]=m[x]+1
      value=a[x][y]
   for i in range (len(m)):
      if (m[i]==-1):
	m[i]=0	   
   return (m, minChange)

K=31
value=[1,3,7,12]
c, result = changedp(K, value)
print c[0:len(c)]
print ("Min Result: %d" %result)

