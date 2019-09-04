#from os import chdir
##imported for chdir and path.isfile
import os
from shutil import copyfile


#this function will determine an in home identifier to add to the part
#it will be a part number followed by a comma and our identification for the board
def check_if_file_exists(board_number):
	counter=1
	#####
	####
	##
	##
	##### FIX THIS STARTING AT 10 THE COMMA IS GONE
	board_number+=","+str(counter)
	temp=os.path.isfile(board_number)
	print("your board number is "+board_number)
	while(temp==True):
		#wanted to not rewrite the way I wrote it since it is incremented before removed, check if it is divisibile
#by 10 as opposed to break, break may be easier to follow
		if counter%10==0:
			board_number=board_number[:-len(str(counter-1))]
		else:
			board_number=board_number[:-len(str(counter))]
		board_number+=str(counter)
		temp=os.path.isfile(board_number)
		counter= int(counter)+1
	return board_number

text_source="../../logic_board_text_files/"
destination="./saved_boards"

os.chdir(destination)
board_number=raw_input("what is your board number? ")
new_file_name=check_if_file_exists(board_number)

for filename in os.listdir(text_source):
	temp= board_number in filename
	if temp==True:
		print(filename)
		#print(text_source+filename,)
		copyfile(text_source+filename,'./'+new_file_name)
		print("the board you added was "+board_number+" the text file it will copy is "+filename+ " it will be added as "+new_file_name)
