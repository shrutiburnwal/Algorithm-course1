import math

class karatsuba:

	def _init__(self):
		print "Karatsuba!"

	def karatmul(self, x, y):
		strx = str(x)
		stry = str(y)
		mx = len(strx)
		my = len(stry)
		if mx==1 or my==1:
			res = int(x)*int(y)
			return res
		n1 = mx
		if mx>my:
			stry = stry.rjust(mx, '0')
			n1 = mx
		elif my>mx:
			strx = strx.rjust(my, '0')
			n1 = my
		m = n1 % 2
		setval = 0
		even = n1
		if m!=0:
			n1 +=1
			setval = 1
		
		lower = int(math.ceil((n1)/2))-setval
    upper = int(math.floor((n1)/2))-setval
		a = strx[0:upper]
		b = strx[lower:n1]
		c = stry[0:upper]
		d = stry[lower:n1]
		res = ((10**n1)*self.karatmul(a,c)) + ((10**((n1)/2))*(self.karatmul(a,d) + self.karatmul(b,c))) + self.karatmul(b,d)
		return res 


calling = karatsuba();

print calling.karatmul(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)
