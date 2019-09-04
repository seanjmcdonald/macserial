import sys

serial=""
flag=-1
error_file="error_log"
good_input="success_log"
#since it is internall do i need to bother capturing their inputs?
if len(sys.argv)!=2:
	print("wrong number of args")
	exit(1)
raw_serial=sys.argv[1].upper()
if len(raw_serial)==12 or len(raw_serial)==11:
	serial=raw_serial[8:]
else:
	print("A serial needs 11 or 12 characters")
	exit(1)
myfile="database"
file=open (myfile,"r")
#maybe record line_num so if this is popular enough we could reorder so the more popular lookups are near the top
for line_num, line in enumerate(file):
	if(line.find(serial)!=-1):
		good_file=open (good_input,"a+")
		good_file.write("their serial number was "+raw_serial+ " and the last chars were "+serial+" and line number "+str(line_num)+"\n")
		
		good_file.close()
		flag=1
		break
file.close()
if flag!=1:
	bad_file=open(error_file,"a+")
	bad_file.write("their serial number was "+ raw_serial+"\n")
	bad_file.close()
