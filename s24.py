import os # import the os module
#select the directory whose content you want to list
directory_path = 'Program Files (x86)/'
#use the os module to list the directory content
contents = os.listdir(directory_path)
print(contents)
