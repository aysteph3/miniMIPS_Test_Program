# Copyright (C) 2020 Oyeniran Adeboye Stephen

from collections import OrderedDict
###############################################################
# Decoding instruction for TDF Test generation				  # 
###############################################################
def decode(op):
	decoder="decoder.txt"
	decode = open(decoder,'r')
	decoder_op1 = OrderedDict()
	decoder_op2 = OrderedDict()
	firstPass = True
	for line in decode:
		if "=" in line:
			try:
				check = line.split("=")
				if check[1][0] == "i":
					decoder_op1[check[0]]=check[1][2:]
				else:
					decoder_op2[check[0]]=check[1]
			except IndexError:
				firstPass = False
	if op=='op1':
		return decoder_op1
	else:
		return decoder_op2