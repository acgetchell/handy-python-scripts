# http://learnpythonthehardway.org/book/ex15.html

from __future__ import division
# This allows integer division to convert to floating point division automatically
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r: " % filename

lines = txt.readlines()
txt.close()

for i in lines:
	print i

print "Here's your position-in-line counts: "
transposed = map(None, *lines)
line_number = 1
for i in transposed:
	length = i.count('A')+i.count('C')+i.count('G')+i.count('T')
	if length != 0:
		A_percent = (i.count('A')/length)*100
		C_percent = (i.count('C')/length)*100
		G_percent = (i.count('G')/length)*100
		T_percent = (i.count('T')/length)*100
		print "Position %i:A(%i)%%,C:(%i)%%, G:(%i)%%, T:(%i)%%" % (line_number, A_percent, C_percent, G_percent, T_percent)
		line_number +=1