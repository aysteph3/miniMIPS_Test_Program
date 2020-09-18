# Copyright (C) 2018 Oyeniran Adeboye Stephen, Olusiji
import reset
import load_memory
import op2_template
import op1_template
import pseudo_template
import register_test
import pipeline
import op2_template_optimized
import op1_template_optimized

#test data file
inputFile = "../input/data_tdf.txt"
parameter = "parameter.txt"
data_f = open(inputFile,'r')

l = open(parameter,'r')
out = open('outputme.txt', 'w')
total_pattern = len(open('../input/data_tdf.txt').readlines())

branchFile = "../input/branch.txt"
branch_f = open(branchFile,'r')
branch_total_pattern = len(open('../input/branch.txt').readlines())

#interrupt
reset.interrupt_function(out)

#reset registers
reset.reset_function(out)

iterator = 0
pattern_count = 0
result_address = 0
pattern_address = 0
result_register = 0
shift_amount = 0
jump_address = 0
branch_count = 0
source_register1 = 0
source_register2 = 0
transition_address = 0

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
			elif (check[0] == 'jump_address'):
				jump_address = check[1].rstrip()
			elif (check[0] == 'branch_count'):
				branch_count = check[1].rstrip()
			elif (check[0] == 'source_register1'):
				source_register1 = check[1].rstrip()
			elif (check[0] == 'source_register2'):
				source_register2 = check[1].rstrip()
			elif (check[0] == 'transition_address'):
				transition_address = check[1].rstrip()
			elif (check[0] == 'source_register3'):
				source_register3 = check[1].rstrip()
		except IndexError:
			firstPass = False

print 'iterator =', iterator
print 'pattern_count =', pattern_count
print 'store_result_address =', result_address
print 'test_pattern_address =', pattern_address
print 'result_register =', result_register
print 'jump_address =', jump_address
print 'branch_count =', branch_count
print 'source_register1 =', source_register1
print 'source_register2 =', source_register2
print 'transition_address =', transition_address
print 'source_register3 =', source_register3
print "...................................."

out.write(" main:\n")
#Special registers
register_test.special_register(out)
#register_test.special_register_datapart(out)

#template for pipeline
out.write(";..........pipeline test..........;\n")
out.write(" lui $%s, %d\n" % (result_address, 1))
out.write(" ori $%s, $%s, %d\n\n" % (result_address, result_address, 5000))
pipeline.pipeline_test(out, result_address, result_register)


####template for register testing
###out.write(";..........register test..........;\n")
###register_test.reg_test(out, result_address, pattern_address)

#co_processor register testing
out.write(";........co-co_processor registers........;\n")
out.write(" lui $%s, %d\n" % (result_address, 1))
out.write(" ori $%s, $%s, %d\n\n" % (result_address, result_address, 5500))
register_test.cop_register(out, result_address)
#register_test.cop_register_new(out, result_address)

out.write(";........other test........;\n")
out.write(";........reset $26 back for branch loops........;\n")
out.write(" lui $%s, %d\n" % (branch_count, 0))
out.write(" ori $%s, $%s, %d\n" % (branch_count, branch_count, branch_total_pattern*2))
out.write(";........reset $28 back for other test loops........;\n")
out.write(" lui $%s, %d\n" % (pattern_count, 0))
out.write(" ori $%s, $%s, %d\n" % (pattern_count, pattern_count, total_pattern*2))
out.write(";........set memory location for signature........;\n")
out.write(" lui $%s, %d\n" % (result_address, 1))
out.write(" ori $%s, $%s, %d\n\n" % (result_address, result_address, 6000))

out.write(" jal reset_offsets\n")
out.write(" jal init_patterns\n")
out.write(" jal init_branch\n\n")

#template for op2
###op2_template.op2_template(parameter,out,result_register,result_address,iterator,pattern_count, shift_amount)
op2_template_optimized.op2_template(parameter,out,result_register,result_address,iterator,pattern_count, shift_amount, source_register1, source_register2, transition_address, source_register3)

#template for op1
op1_template_optimized.ops1_template(parameter, out, result_register, result_address, inputFile, iterator, pattern_count, pattern_address, branch_count, source_register1, source_register2, transition_address)
###out.write("jal reset_offsets\n\n") # reset offsets after all immediate operations. Remove if you plan other instructions after this

#syscall
pipeline.syscall(out)

#template for psuedo-exhaustive data
out.write(";..........data-path test..........;\n")
out.write(" lui $%s, %d\n" % (result_address, 1))
out.write(" ori $%s, $%s, %d\n\n" % (result_address, result_address, 10000))
pseudo_template.make_pseudo_template(parameter,out, result_register)

#break
pipeline.breaks(out)

#template for HILO
out.write(";..........hilo test..........;\n")
register_test.hilo(out, result_address, pattern_address)

#pattern loading, reset offset module, increment offset
reset.end_program(out)
reset.load_pattern(out, pattern_address, transition_address)
reset.reset_offsets(out, pattern_address,iterator,result_register)
reset.reset_hi_lo(out)
reset.increment_offset(out, pattern_address,iterator, result_address)
reset.increment(out, pattern_address,iterator, result_address)
reset.store_branch(out,source_register1, result_address)
reset.store(out,result_register, result_address)
reset.init_cp(out)

##Branch templates
out.write(";..........Branch templates..........;\n")
op1_template_optimized.branch_template(parameter, out, jump_address, result_register, result_address, inputFile, iterator, pattern_count, pattern_address, branch_count, source_register1, source_register2)

#register initialization
out.write(";..........register_initialization..........;\n")
register_test.reg_test_dat(out,result_address,pattern_address)


#load data into memory
out.write(";..........memory_initialization..........;\n")
load_memory.init_patterns(out,data_f, pattern_address)

load_memory.load_branch(out, pattern_address)

#load branch data into memory
out.write(";..........branch_memory_initialization..........;\n")
load_memory.init_patterns_branch(out,branch_f, pattern_address)

out.write("end:\n")
out.write("\t j end\n")

data_f.close()
out.close()
l.close()
