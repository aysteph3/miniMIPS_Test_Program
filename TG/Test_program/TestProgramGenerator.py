# Copyright (C) 2018 Oyeniran Adeboye Stephen, Olusiji
import reset
import load_memory
import op2_template
import op1_template

#test data file
inputFile = "../input/data.txt"
parameter = "parameter.txt"
data_f = open(inputFile,'r')

l = open(parameter,'r')
out = open('outputme.txt', 'w')

total_pattern = len(open('../input/data.txt').readlines())

#reset registers
reset.reset_function(out)

iterator = 0
pattern_count = 0
result_address = 0
pattern_address = 0
result_register = 0
shift_amount = 0

# fixes the parameter used for the program
print "............parameters............."
firstPass = True
for line in l:
	if "=" in line:
		try:
		 	check = line.split("=")
			if (check[0] == 'iterator'):
				iterator = check[1].rstrip()
			elif (check[0] == 'pattern_count'):
				pattern_count = check[1].rstrip()
			elif (check[0] == 'result_address'):
				result_address = check[1].rstrip()
			elif (check[0] == 'pattern_address'):
				pattern_address = check[1].rstrip()
			elif (check[0] == 'result_register'):
				result_register = check[1].rstrip()
			elif (check[0] == 'shift_amount'):
				shift_amount = check[1].rstrip()
		except IndexError:
			firstPass = False

print 'iterator =', iterator
print 'pattern_count =', pattern_count
print 'store_result_address =', result_address
print 'test_pattern_address =', pattern_address
print 'result_register =', result_register
print "...................................."

out.write("main:\n")
out.write("\tlui $%s, %d\n" % (pattern_count, 0))
out.write("\tori $%s, $%s, %d\n" % (pattern_count, pattern_count, total_pattern*2))
out.write("\tlui $%s, %d\n" % (result_address, 1))
out.write("\tori $%s, $%s, %d\n\n" % (result_address, result_address, 2000))

out.write("\tjal reset_offsets\n\n")
out.write("\tjal init_patterns\n\n")

#template for op2
op2_template.op2_template(parameter,out,result_register,result_address,iterator,pattern_count, shift_amount)
op1_template.ops1_template(parameter, out, result_register, result_address, inputFile, iterator, pattern_count, pattern_address)
#out.write("jal reset_offsets\n\n") # reset offsets after all immediate operations. Remove if you plan other instructions after this

#pattern loading, reset offset module, increment offset
reset.load_pattern(out, pattern_address)
reset.reset_offsets(out, pattern_address,iterator,result_register)
reset.reset_hi_lo(out)
reset.increment_offset(out, pattern_address,iterator, result_address)

#load data into memory
load_memory.init_patterns(out,data_f)

out.write("end:\n")
out.write("\t j end\n")
data_f.close
out.close()
l.close()
