# http://learnpythonthehardway.org/book/ex15.html

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r: " % filename

lines = txt.readlines()
txt.close()

for i in lines:
	print i

print "Here's your line-by-line counts: "
transposed = zip(*lines)
line_number = 1
for i in transposed:
	print "In line number %i" % line_number
	counts = (i.count('G'), i.count('A'))
	print "There are {0} Gs and {1} As".format(*counts)
	#print "There are %s Cs" & i.count('C')
	line_number +=1