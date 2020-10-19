import glob
import os

folder_path = '/Patterns/'
for filename in glob.glob(os.path.join(folder_path, '*.txt')):
    with open(filename, 'r') as f:
        text = f.read()
        print (filename)
        print (len(text))
#print (folder_path)

folder_path = 'Patterns'
for filename in os.listdir(folder_path):
	print (filename)

for filename in os.listdir(os.getcwd()):
	print (filename)
