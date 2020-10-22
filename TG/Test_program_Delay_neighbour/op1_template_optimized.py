# Copyright (C) 2018 Oyeniran Adeboye Stephen, Olusiji
import reset
import instruction_decoder

print ".....Decoder for TDF OP1 neighbours....."
op1_decoder = instruction_decoder.decode("op1")
for dec, opcode in op1_decoder.items():
    if dec == '000000':
    	initialval = "{0:b}".format(int(dec,2)+1).zfill(6)
        nextval = "{0:b}".format(int(dec,2)+2).zfill(6)
    else:
        nextval = "{0:b}".format(int(dec,2)+1).zfill(6)
        initialval = "{0:b}".format(int(dec,2)-1).zfill(6)
    if nextval not in op1_decoder:
        nextval = "{0:b}".format(int(initialval,2)-1).zfill(6)
        if nextval not in op1_decoder:
            nextval = "{0:b}".format(int(initialval,2)).zfill(6)
    if initialval not in op1_decoder:
        initialval = "{0:b}".format(int(nextval,2)+1).zfill(6)
        if initialval not in op1_decoder:
            initialval = "{0:b}".format(int(nextval,2)).zfill(6)
    print dec, initialval, nextval, opcode.rstrip(), op1_decoder.get(initialval).rstrip(), op1_decoder.get(nextval).rstrip()
    opcode = opcode.rstrip().lower()
    neighbour1 = op1_decoder.get(initialval).rstrip().lower()
    neighbour2 = op1_decoder.get(nextval).rstrip().lower()

def generate_immediate(instruct, out, result_register, result_address, inputFile, src1, src2, transition_instruction):
	data_lines = []
	total_pattern = len(open(inputFile).readlines())
 	f = open(inputFile,'r')
	k = 0
	n = 0
 	for line in f:
	 n = n + 1
 	 bit_set1 = line[48:64]
 	 immediate = str(int(bit_set1,2))
	 immediate_fun_2(instruct, out, result_register,result_address, immediate, src1, src2, transition_instruction)
	 if (total_pattern == n):
	 	out.write("\n")
	 	#print total_pattern
	f.close()

def immediate_fun(instruction, file, result_register, result_address, immediate,k, src1, src2):
    #file.write("\tjal load_patterns\n")
    file.write("\t%s $%s, $%s, %s\n" % (instruction, result_register, src1, immediate))
    file.write("\tsw $%s, %s($%s)\n" % (result_register, k, result_address))
    #file.write("\tjal increment_offset\n")

def immediate_fun_2(instruction, file, result_register, result_address, immediate, src1, src2, transition_instruction):
   file.write("\tjal load_patterns\n")
   file.write("\t%s $%s, $%s, %s\n" % (instruction, result_register, src1, immediate))
   file.write("\t%s $%s, $%s, %s\n" % (transition_instruction, result_register, src1, immediate))
   file.write("\t%s $%s, $%s, %s\n" % (transition_instruction, str(int(result_register)+1), src1, immediate))
   file.write("\t%s $%s, $%s, %s\n" % (instruction, str(int(result_register)+1), src1, immediate))
   file.write("\tjal store\n")
   file.write("\tjal increment_offset\n")

def branch_1(instruction, file, jump_address,result_address,iterator,branch_count, instr, src1, src2):
    file.write("\t%s $%s, $%d, %d\n" % ('addi', jump_address, 31, 0))
    file.write("\t%s $%s, $%s, store_branch\n" % (instruction, src1, src2))
    file.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
    file.write("\tsw $%s, %s($%s)\n" % (src2, 0, result_address))
    file.write("\tjr $%s\n\n" % (jump_address))

def branch_2(instruction, file, jump_address,result_address,iterator,branch_count, instr, src1, src2):
 	file.write("\t%s $%s, $%d, %d\n" % ('addi', jump_address, 31, 0))
 	file.write("\t%s $%s, store_branch\n" % (instruction, src1))
 	file.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
 	file.write("\tsw $%s, %s($%s)\n" % (src2, 0, result_address))
 	file.write("\tjr $%s\n\n" % (jump_address))

def branch_test(instruction, file, result_register,result_address,iterator,branch_count, instr):
    file.write("\tjal load_branch\n")
    file.write("\tjal branch_"+instruction+"\n")
    #file.write("\t%s $%s, $%d, $%d\n" % ('and', result_register, 15, 16))
    #file.write("\t%s $%d, $%d, store_branch\n" % (instruction, 15, 16))
    #file.write("\tsw $%d, %d($%s)\n" % (0, 0, result_address))
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, branch_count, instr))

def branc_location(instruction, file, result_address):
    file.write(" store_"+instruction+":\n")
    file.write("\tsw $%d, %d($%s)\n" % (18, 0, result_address))
    file.write("\tjal increment_offset\n\n")

def co_processor_fun(instruction, file, result_register, result_address, iterator, pattern_count, instr, cp_register, src1, src2):
	file.write("\tjal load_patterns\n")
	file.write("\t%s $%s, $%d\n" % (instruction, src1, cp_register-1))
	file.write("\t%s $%s, $%d\n" % (instruction, src2, cp_register))
	file.write("\tswc0 $%s, %d($%s)\n" % (cp_register-1, 0, result_address))
	file.write("\tswc0 $%s, %d($%s)\n" % (cp_register, 4, result_address))
	file.write("\tjal increment_offset\n")
	file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def co_processor_fun_2(instruction, file, result_register, result_address, iterator, pattern_count, instr, cp_register, src1, src2):
	file.write("\tjal load_patterns\n")
	file.write("\t%s $%s, $%d\n" % ('mtc0', src1, cp_register-1))
	file.write("\t%s $%s, $%d\n" % (instruction, result_register, cp_register-1))
	file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
	file.write("\t%s $%s, $%d\n" % ('mtc0', src2, cp_register))
	file.write("\t%s $%s, $%d\n" % (instruction, result_register, cp_register))
	file.write("\tsw $%s, %d($%s)\n" % (result_register, 4, result_address))
	file.write("\tjal increment_offset\n")
	file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def lw0_sw0_fun(instruction, file, cp_register, result_address, iterator, pattern_count, instr, pattern_address):
	file.write("\tlwc0 $%s, %d($%s)\n" % (cp_register-1, 0, pattern_address))
	file.write("\tlwc0 $%s, %d($%s)\n" % (cp_register, 4, pattern_address))
	file.write("\tswc0 $%s, %d($%s)\n" % (cp_register-1, 0, result_address))
	file.write("\tswc0 $%s, %d($%s)\n" % (cp_register, 4, result_address))
	file.write("\tjal increment_offset\n")
	file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def lw_sw_fun(instruction, file, result_register, result_address, iterator, pattern_count, instr, pattern_address):
	file.write("\tlw $%s, %d($%s)\n" % (result_register, 0, pattern_address))
	file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
	file.write("\tjal increment_offset\n")
	file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def print_tags(file, instr):
	file.write("jal reset_offsets\n")
	file.write("operation_"+instr+":\n")

def print_tags_branch(file, instr):
	file.write("branch_"+instr+":\n")

def print_tags_cp(file, instr):
	file.write("jal reset_offsets\n")
	file.write("jal init_cp\n")
	file.write("operation_"+instr+":\n")

def branch_template(para, out, jump_address, result_register, result_address, inputFile,iterator, pattern_count, pattern_address,branch_count, src1, src2):
 Ins = open(para,'r')
 data_lines = []
 opcode = []
 firstPass = True
 for line in Ins:
 	if "=" not in line:
 		try:
 		 line = line.replace(" ", "")
 		 catergory = line[1:3]
		 line = line.rstrip()
		 instru = line[3:]
		 instr = str.strip(instru)
		 instruction = instr[0:]
		 if(catergory == 'd_'):
			print_tags_branch(out, instr)
			branch_1(instruction, out,jump_address,result_address,iterator,branch_count, instr, src1, src2)
		 elif(catergory == 'e_'):
			print_tags_branch(out, instr)
			if ((instr == 'bgezal') or (instr == 'bltzal')):
				branch_2(instruction, out,jump_address,result_address,iterator,branch_count, instr, src1, src2)
			else:
				branch_2(instruction, out,jump_address,result_address,iterator,branch_count, instr, src1, src2)
		except IndexError:
 				firstPass = False
	else:
		do='nothing'

def ops1_template(para, out, result_register, result_address,iterator, pattern_count, pattern_address, branch_count, src1, src2):
 Ins = open(para,'r')
 data_lines = []
 opcode = []
 firstPass = True
 cp_register = 13 # use to control register 12 and 13
 cp_register2 = 15  # use to control register 14 and 15

 for line in Ins:
 	if "=" not in line:
 		try:
 		 line = line.replace(" ", "")
 		 catergory = line[1:3]
		 line = line.rstrip()
		 instru = line[3:]
		 instr = str.strip(instru)
		 instruction = instr[0:]
		 if (catergory == 'i_'):
		 	if (instr == 'addi' or instr == 'addui'):
		 		inputFile = '../input/dedicated_control/add.txt'
		 	elif instr == 'slti':
		 		inputFile = '../input/dedicated_control/slt.txt'
		 	elif instr == 'sltiu':
		 		inputFile = '../input/dedicated_control/sltu.txt'
		 	elif instr == 'andi':
		 		inputFile = '../input/dedicated_control/and.txt'
		 	elif instr == 'ori':
		 		inputFile = '../input/dedicated_control/or.txt'
		 	elif instr == 'xori':
		 		inputFile = '../input/dedicated_control/xor.txt'

		 	for x in range(2):
		 		if (x == 0):
		 			if instr!=neighbour1:
		 		 		inst= instr+"_"+neighbour1
		 				print_tags_cp(out, inst)
						generate_immediate(instruction, out, result_register, result_address, inputFile, src1, src2, neighbour1)
				else:
					if instr!=neighbour2:
						if neighbour1 != neighbour2:
							inst= instr+"_"+neighbour2
							print_tags_cp(out, inst)
							generate_immediate(instruction, out, result_register, result_address, inputFile, src1, src2, neighbour2)
		 elif(catergory == '1_'):
			 print_tags(out, instr)
			 if (instruction == 'mtc0'):
			 	co_processor_fun(instruction, out,result_register,result_address, iterator,pattern_count, instr, cp_register, src1, src2)
			 elif(instruction == 'mfc0'):
			 	co_processor_fun_2(instruction, out,result_register,result_address, iterator,pattern_count, instr, cp_register, src1, src2)
		 elif(catergory == '2_'):
			 print_tags(out, instr)
			 lw_sw_fun(instruction, out,result_register,result_address, iterator,pattern_count, instr, pattern_address)
		 elif(catergory == '3_'):
			 print_tags(out, instr)
			 lw0_sw0_fun(instruction, out,cp_register2,result_address, iterator,pattern_count, instr, pattern_address)
		 elif(catergory == 'd_'):
			print_tags(out, instr)
			branch_test(instruction, out,result_register,result_address,iterator,branch_count, instr)
		 elif(catergory == 'e_'):
			print_tags(out, instr)
			if ((instr == 'bgezal') or (instr == 'bltzal')):
				branch_test(instruction, out,result_register,result_address,iterator,branch_count, instr)
			else:
				branch_test(instruction, out,result_register,result_address,iterator,branch_count, instr)
				#branc_location(instruction, out, result_address)
		except IndexError:
 				firstPass = False
	else:
		do='nothing'

 Ins.close()
