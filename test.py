from tempfile import mkstemp
from shutil import move
from os import remove, close

def replace(file_path, skin_name):
	fh, abs_path = mkstemp()
	new_file = open(abs_path,'w')
	old_file = open(file_path)
	for line in old_file:
		if 'Name: ' in line:
			new_file.write('Name: ' + skin_name + '\n')
		elif 'Version: ' in line:
			new_file.write('Version: 1\n')
		elif 'Author: ' in line:
			new_file.write('Author: OsuElements\n')
		else:
			new_file.write(line)
			
	new_file.close()
	close(fh)
	old_file.close()
	remove(file_path)
	move(abs_path, file_path)

replace('skin.ini', 'new skin') 
