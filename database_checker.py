import sys

serial=""
if len(sys.argv)!=2:
	print("wrong number of args")
	exit(1)
raw_serial=sys.argv[1].upper()
if len(raw_serial)==12 or 11:
	serial=raw_serial[8:]
else:
	print("A serial needs 11 or 12 characters")
myfile="database"
file=open (myfile,"r")
for line_num, line in enumerate(file):
	if(line.find(serial)!=-1):
		print(serial)
file.close()
