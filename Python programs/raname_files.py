import os
def rename_files():
	file_names =  os.listdir(r"/home/hemant/MyDrive/Programming/Scripts")
	path = os.getcwd()
	os.chdir(r"/home/hemant/MyDrive/Programming/Scripts")
	for file_name in file_names:
		os.rename(file_name,file_name.translate(None,".h"))
	os.chdir(path)	
rename_files()	
