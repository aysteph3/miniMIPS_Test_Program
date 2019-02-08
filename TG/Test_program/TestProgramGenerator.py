# Copyright (C) 2018 Oyeniran Adeboye Stephen, Olusiji
import reset
import load_memory
import op2_template
import op1_template
import pseudo_template
import register_test
import pipeline

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
register_test.special_register(out)
out.write(";........continue test........;\n")
out.write(" lui $%s, %d\n" % (pattern_count, 0))
out.write(" ori $%s, $%s, %d\n" % (pattern_count, pattern_count, total_pattern*2))
out.write(" lui $%s, %d\n" % (result_address, 1))
out.write(" ori $%s, $%s, %d\n\n" % (result_address, result_address, 2000))

out.write(" jal reset_offsets\n")
out.write(" jal init_patterns\n\n")

#template for register testing
out.write(";..........register test..........;\n")
register_test.reg_test(out, result_address, pattern_address)

out.write(";........other test........;\n")
out.write(";........reset $28 back for loops........;\n")
out.write(" lui $%s, %d\n" % (pattern_count, 0))
out.write(" ori $%s, $%s, %d\n\n" % (pattern_count, pattern_count, total_pattern*2))
out.write(" lui $%s, %d\n" % (result_address, 1))
out.write(" ori $%s, $%s, %d\n\n" % (result_address, result_address, 2000))

#template for op2
op2_template.op2_template(parameter,out,result_register,result_address,iterator,pattern_count, shift_amount)

#template for psuedo-exhaustive data
out.write(";..........data-path test..........;\n")
pseudo_template.make_pseudo_template(parameter,out, result_register)

#template for op1
op1_template.ops1_template(parameter, out, result_register, result_address, inputFile, iterator, pattern_count, pattern_address)
#out.write("jal reset_offsets\n\n") # reset offsets after all immediate operations. Remove if you plan other instructions after this

#template for HILO
out.write(";..........hilo test..........;\n")
register_test.hilo(out, result_address, pattern_address)

#template for pipeline
out.write(";..........pipeline test..........;\n")
pipeline.pipeline_test(out, result_address)

#pattern loading, reset offset module, increment offset
reset.load_pattern(out, pattern_address)
reset.reset_offsets(out, pattern_address,iterator,result_register)
reset.reset_hi_lo(out)
reset.increment_offset(out, pattern_address,iterator, result_address)
reset.store_branch(out, result_address)

#register initialization
out.write(";..........register_initialization..........;\n")
register_test.reg_test_dat(out,result_address,pattern_address)

#load data into memory
out.write(";..........memory_initialization..........;\n")
load_memory.init_patterns(out,data_f, pattern_address)

out.write("end:\n")
out.write("\t j end\n")
data_f.close
out.close()
l.close()
