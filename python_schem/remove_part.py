import os

where_text_is_saved="./"

#maybe make identifiers unique instead of like 820-****,1
part_to_look_for=raw_input("what part are you looking for? ")
#os.chdir(where_text_is_saved)
file_to_remove_from='aaaaa'
string_to_remove='AAAAAAAAA'
os.system('bash %s %s %s' % ('./save_to_here/remove_from_file.bash' ,'./save_to_here/'+file_to_remove_from, string_to_remove))
