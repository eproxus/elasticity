class Sequence(object):
	"""
	Implements a circular sequence with a max value. I the value of the counter is
	incremented over maxval it starts over at 0 + the amount that overlapped.
	A comparisson such as 2 > 9 with a max value of 10 would yield True as 2 is the
	"latest" value. 7 > 9 would in that case give False as a result. 7 > 12 would
	give Ture as 12 wrapped to 10 is 1.
	
	Note that the value of a Sequence class must be set by setting seq.val = 10 due
	to limits in the Python language. If one would write seq = 10 it woul assign an
	integer to seq.
	
	Usage:
	
	>>> s = Sequence(10)
	>>> print s
	0
	
	>>> s += 23
	>>> print s, s > 5
	3 True
	"""

	def __init__(self, maxval, initval=0):
		self.maxval = maxval
		self.val = initval

	def __iter__(self):
		return self

	def next(self):
		ret = self.val
		self.__add__(1)
		return ret

	def __add__(self, increment):
		self.val = (self.val + increment) % self.maxval
		return self

	def __sub__(self, decrement):
		self.val = (self.val - decrement) % self.maxval
		return self
	
	def __lt__(self, other):
		otherClamped = other % self.maxval
		return ((self.val < otherClamped) and ((self.val - otherClamped) <= (self.maxval / 2))) or \
			   ((otherClamped < self.val) and ((otherClamped - self.val) > (self.maxval / 2)))
	
	def __le__(self, other):
		otherClamped = other % self.maxval
		return ((self.val < otherClamped) and ((self.val - otherClamped) <= (self.maxval / 2))) or \
			   ((otherClamped < self.val) and ((otherClamped - self.val) > (self.maxval / 2))) or \
			   self.val == otherClamped
	
	def __eq__(self, other):
		return self.val == (other % self.maxval)
	
	def __ne__(self, other):
		return self.val != (other % self.maxval)
	
	def __gt__(self, other):
		otherClamped = other % self.maxval
		return ((self.val > otherClamped) and ((self.val - otherClamped) <= (self.maxval / 2))) or \
			   ((otherClamped > self.val) and ((otherClamped - self.val) > (self.maxval / 2)))
	
	def __ge__(self, other):
		otherClamped = other % self.maxval
		return ((self.val > otherClamped) and ((self.val - otherClamped) <= (self.maxval / 2))) or \
			   ((otherClamped > self.val) and ((otherClamped - self.val) > (self.maxval / 2))) or \
			   self.val == otherClamped

	def __repr__(self):
		return str(self.val)

	def __str__(self):
		return str(self.val)

