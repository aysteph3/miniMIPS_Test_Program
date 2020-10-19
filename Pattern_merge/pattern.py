#!/usr/bin/ python
# Copyright (C) 2020 Stephen Oyeniran

import glob
import os, sys, getopt

def main(argv):
	inputfile =''
	outputfile=''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  	except getopt.GetoptError:
  		print 'pattern.py -i <inputfile> -o <outputfile>'
  		sys.exit(2)

  	if len(argv[1:]) == 0:
  		print 'pattern.py -i <inputfile> -o <outputfile>'
  		sys.exit()
  	else:
  		for opt, arg in opts:
  			if opt == '-h':
  				print 'pattern.py -i <inputfile> -o <outputfile>'
  				sys.exit()
			elif opt in ("-i", "--ifile"):
				inputfile = arg
			elif opt in ("-o", "--ofile"):
				outputfile = arg


	if os.path.exists("outputfiles_folder"):
		files = [file for file in os.listdir("outputfiles_folder")]
		#for file in files:
			#os.remove("outputfiles_folder"+"/"+file)
	else:
		os.mkdir("outputfiles_folder")

	out = inputfile.split('/',1)[1][:-1] 
	if not outputfile:
		outputfile="outputfiles_folder/"+out+".txt"
	else:
		outputfile="outputfiles_folder/"+outputfile+'_combined.txt'

	lst =[]
	no_duplicate=[]
	count = 0
	folder_path = inputfile
	out_f = open(outputfile, "w")
	for filename in glob.glob(os.path.join(folder_path, '*.txt')):
		with open(filename, 'r') as f:
			for line in f:
				line = line.strip()
				#out_f.write(line)
				#out_f.write("\n")
				lst.append(line)
				count = count+1

	no_duplicate= list(dict.fromkeys(lst))
	for item in no_duplicate:
		out_f.write(item)
		out_f.write("\n")
	print count
	print len(no_duplicate)
	print '!!!file created successfully!!!'
	out_f.close

if __name__ == "__main__":
   main(sys.argv[1:])
