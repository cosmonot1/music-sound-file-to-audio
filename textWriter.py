inf = open('test.txt', 'w')
for i in range(0,2500):
	inf.write('a')
inf.close()
print "closed"