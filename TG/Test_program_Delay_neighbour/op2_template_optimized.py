# Copyright (C) 2020 Oyeniran Adeboye Stephen
#This template generates OP2 instructions. The functionality is described as follow
#op2_func and variants generate test for OP2 instructions while hi_lo and variants generate
#test for HILO. The parameter file helps organize the test with the help of the HLDD
import instruction_decoder

def op2_func(instruction, file, result_register,result_address,iterator,pattern_count, instr, src1, src2, transition_address):
    file.write("jal reset_offsets\n")
    #file.write("jal init_cp\n")
    file.write("operation_op2:\n")
    file.write("\tjal load_patterns\n")


def op2_func2(instruction, file, result_register,result_address,iterator,pattern_count, instr, src1, src2, transition_instruction, shift_amount):
    file.write("jal reset_offsets\n")
    file.write("jal init_cp\n")
    file.write("operation_"+instr+":\n")
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%s, $%s, $%s\n" % (instruction, result_register, src1, src2))
    if ((transition_instruction == 'sll') or (transition_instruction == 'sra') or (transition_instruction == 'srl')):
        file.write("\t%s $%s ,$%s, %s\n" % (transition_instruction, result_register, src1, shift_amount ))
    else:
        file.write("\t%s $%s, $%s, $%s\n" % (transition_instruction, result_register, src1, src2))
    if ((transition_instruction == 'sll') or (transition_instruction == 'sra') or (transition_instruction == 'srl')):
        file.write("\t%s $%s, $%s, %s\n" % (transition_instruction, str(int(result_register)+1), src1, shift_amount))
    else:
        file.write("\t%s $%s, $%s, $%s\n" % (transition_instruction, str(int(result_register)+1), src1, src2))
    file.write("\t%s $%s, $%s, $%s\n" % (instruction, str(int(result_register)+1), src1, src2))
    file.write("\tjal store\n")
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def op2_mult_u_func(instruction, file, result_register,result_address,iterator,pattern_count, instr, src1, src2, transition_instruction, shift_amount):
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%s, $%s\n" % (instruction, src1, src2))
    if ((transition_instruction == 'sll') or (transition_instruction == 'sra') or (transition_instruction == 'srl')):
        file.write("\t%s $%s ,$%s, %s\n" % (transition_instruction, result_register, src1, shift_amount ))
    elif ((transition_instruction == 'mfhi') or (transition_instruction == 'mflo') or (transition_instruction == 'mthi') or (transition_instruction == 'mtlo')):
        file.write("\t%s $%s\n" % (transition_instruction, result_register))
    elif((transition_instruction == 'mult') or (transition_instruction == 'multu')):
        file.write("\t%s $%s, $%s\n" % (transition_instruction, src1, src2))
    else:
        file.write("\t%s $%s, $%s, $%s\n" % (transition_instruction, result_register, src1, src2))
    if ((transition_instruction == 'sll') or (transition_instruction == 'sra') or (transition_instruction == 'srl')):
        file.write("\t%s $%s, $%s, %s\n" % (transition_instruction, str(int(result_register)+1), src1, shift_amount))
    elif ((transition_instruction == 'mfhi') or (transition_instruction == 'mflo') or (transition_instruction == 'mthi') or (transition_instruction == 'mtlo')):
        file.write("\t%s $%s\n" % (transition_instruction, str(int(result_register)+1)))
    elif((transition_instruction == 'mult') or (transition_instruction == 'multu')):
        file.write("\t%s $%s, $%s\n" % (transition_instruction, src1, src2))
    else:
        file.write("\t%s $%s, $%s, $%s\n" % (transition_instruction, str(int(result_register)+1), src1, src2))
    file.write("\t%s $%s, $%s\n" % (instruction, src1, src2))
    file.write("\t%s $%s\n" % ("mfhi", result_register))
    file.write("\t%s $%s\n" % ("mflo", str(int(result_register)+1)))
    file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
    file.write("\tsw $%s, %d($%s)\n" % (str(int(result_register)+1), 4, result_address))
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def op2_mthi_lo_func(instruction, file, result_register,result_address,iterator,pattern_count, instr, src1, src2, transition_instruction, shift_amount):
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%s\n" % (instruction, src1))
    if ((transition_instruction == 'sll') or (transition_instruction == 'sra') or (transition_instruction == 'srl')):
        file.write("\t%s $%s ,$%s, %s\n" % (transition_instruction, result_register, src1, shift_amount ))
    elif ((transition_instruction == 'mfhi') or (transition_instruction == 'mflo') or (transition_instruction == 'mthi') or (transition_instruction == 'mtlo')):
        file.write("\t%s $%s\n" % (transition_instruction, src1))
    else:
        file.write("\t%s $%s, $%s, $%s\n" % (transition_instruction, result_register, src1, src2))
    if ((transition_instruction == 'sll') or (transition_instruction == 'sra') or (transition_instruction == 'srl')):
        file.write("\t%s $%s ,$%s, %s\n" % (transition_instruction, str(int(result_register)+1), src1, shift_amount ))
    elif ((transition_instruction == 'mfhi') or (transition_instruction == 'mflo') or (transition_instruction == 'mthi') or (transition_instruction == 'mtlo')):
        file.write("\t%s $%s\n" % (transition_instruction, src2))
    else:
        file.write("\t%s $%s, $%s, $%s\n" % (transition_instruction, str(int(result_register)+1), src1, src2))
    file.write("\t%s $%s\n" % (instruction, src2))
    file.write("\t%s $%s\n" % ("mfhi", result_register))
    file.write("\t%s $%s\n" % ("mflo", str(int(result_register)+1)))
    file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
    file.write("\tsw $%s, %d($%s)\n" % (str(int(result_register)+1), 4, result_address))
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def op2_mfhi_lo_func(instruction, file, result_register,result_address,iterator,pattern_count, instr, src1, src2, transition_instruction,shift_amount):
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%s\n" % ("mtlo", src1))
    file.write("\t%s $%s\n" % ("mthi", src1))
    file.write("\t%s $%s\n" % (instruction, result_register))
    if ((transition_instruction == 'sll') or (transition_instruction == 'sra') or (transition_instruction == 'srl')):
        file.write("\t%s $%s ,$%s, %s\n" % (transition_instruction, result_register, src1, shift_amount ))
    elif ((transition_instruction == 'mfhi') or (transition_instruction == 'mflo') or (transition_instruction == 'mthi') or (transition_instruction == 'mtlo')):
        file.write("\t%s $%s\n" % (transition_instruction, result_register))
    else:
        file.write("\t%s $%s, $%s, $%s\n" % (transition_instruction, result_register, src1, src2))
    if ((transition_instruction == 'sll') or (transition_instruction == 'sra') or (transition_instruction == 'srl')):
        file.write("\t%s $%s ,$%s, %s\n" % (transition_instruction, str(int(result_register)+1), src1, shift_amount ))
    elif ((transition_instruction == 'mfhi') or (transition_instruction == 'mflo') or (transition_instruction == 'mthi') or (transition_instruction == 'mtlo')):
        file.write("\t%s $%s\n" % (transition_instruction, str(int(result_register)+1)))
    else:
        file.write("\t%s $%s, $%s, $%s\n" % (transition_instruction, str(int(result_register)+1), src1, src2))
    file.write("\t%s $%s\n" % (instruction, str(int(result_register)+1)))
    file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
    file.write("\tsw $%s, %d($%s)\n" % (str(int(result_register)+1), 4, result_address))
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr)) # check this later

def op2_shift_amount_func(instruction, file, result_register,result_address,iterator,pattern_count, instr, shift_amount, src1, src2, transition_instruction):
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%s ,$%s, %s\n" % (instruction, result_register, src1, shift_amount ))
    if ((transition_instruction == 'sll') or (transition_instruction == 'sra') or (transition_instruction == 'srl')):
        file.write("\t%s $%s ,$%s, %s\n" % (transition_instruction, result_register, src1, shift_amount ))
    else:
        file.write("\t%s $%s, $%s, $%s\n" % (transition_instruction, result_register, src1, src2))
    if ((transition_instruction == 'sll') or (transition_instruction == 'sra') or (transition_instruction == 'srl')):
        file.write("\t%s $%s, $%s, %s\n" % (transition_instruction, str(int(result_register)+1), src1, shift_amount))
    else:
        file.write("\t%s $%s, $%s, $%s\n" % (transition_instruction, str(int(result_register)+1), src1, src2))
    file.write("\t%s $%s ,$%s, %s\n" % (instruction, str(int(result_register)+1), src1, shift_amount ))
    file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
    file.write("\tsw $%s, %d($%s)\n" % (str(int(result_register)+1), 4, result_address))
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def hi_lo_mt_func(instruction, file, result_register,result_address,iterator,pattern_count, instr, src1, src2, transition_instruction, shift_amount):
    if (instruction == 'mthi'):
        subInstruct = 'mfhi'
    else:
        subInstruct = 'mflo'
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%s\n" % (instruction, src2))
    file.write("\t%s $%s\n" % (subInstruct ,result_register))
    if ((transition_instruction == 'sll') or (transition_instruction == 'sra') or (transition_instruction == 'srl')):
        file.write("\t%s $%s ,$%s, %s\n" % (transition_instruction, result_register, src1, shift_amount ))
    elif ((transition_instruction == 'mfhi') or (transition_instruction == 'mflo') or (transition_instruction == 'mthi') or (transition_instruction == 'mtlo')):
        file.write("\t%s $%s ,$%s, %s\n" % (transition_instruction, src2))
    else:
        file.write("\t%s $%s, $%s, $%s\n" % (transition_instruction, str(int(result_register)+1), src1, src2))
    file.write("\t%s $%s\n" % (instruction, src2))
    file.write("\t%s $%s\n" % (subInstruct ,result_register))
    file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
    file.write("\tsw $%s, %d($%s)\n" % (str(int(result_register)+1), 4, result_address))
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s_hi_lo\n\n" % (iterator, pattern_count, instr))

def print_tags(file, instr):
    file.write("jal reset_offsets\n")
    file.write("jal init_cp\n")
    file.write("operation_"+instr+":\n")


#########################################################################################
#                           Decode and create OP2 test                                  #
#########################################################################################

def op2_template(para, out, result_register,result_address,iterator,pattern_count, shift_amount, src1, src2):
    print ".....Decoder for TDF OP2 neighbours....."

    op2_decoder = instruction_decoder.decode("op2")
    for dec, opcode in op2_decoder.items():
        if dec == '000000':
            initialval = "{0:b}".format(int(dec,2)+1).zfill(6)
            nextval = "{0:b}".format(int(dec,2)+2).zfill(6)
        else:
            nextval = "{0:b}".format(int(dec,2)+1).zfill(6)
            initialval = "{0:b}".format(int(dec,2)-1).zfill(6)
        if nextval not in op2_decoder:
            nextval = "{0:b}".format(int(initialval,2)-1).zfill(6)
            if nextval not in op2_decoder:
                nextval = "{0:b}".format(int(initialval,2)).zfill(6)
        if initialval not in op2_decoder:
            initialval = "{0:b}".format(int(nextval,2)+1).zfill(6)
            if initialval not in op2_decoder:
                initialval = "{0:b}".format(int(nextval,2)).zfill(6)
        print dec, initialval, nextval, opcode.rstrip(), op2_decoder.get(initialval).rstrip(), op2_decoder.get(nextval).rstrip()
        opcode = opcode.rstrip().lower()
        neighbour1 = op2_decoder.get(initialval).rstrip().lower()
        neighbour2 = op2_decoder.get(nextval).rstrip().lower()

        if ((opcode == 'mult') or (opcode == 'multu')):
            for x in range(2):
                if (x == 0):
                    inst= opcode+"_"+neighbour1
                    print_tags(out, inst)
                    op2_mult_u_func(opcode, out, result_register,result_address,iterator,pattern_count, inst, src1, src2, neighbour1, shift_amount)
                else:
                    if neighbour1 != neighbour2:
                        inst= opcode+"_"+neighbour2
                        print_tags(out, inst)
                        op2_mult_u_func(opcode, out, result_register,result_address,iterator,pattern_count, inst, src1, src2, neighbour2, shift_amount)
        elif((opcode == 'mthi') or (opcode == 'mtlo')):
            for x in range(2):
                if (x == 0):
                    inst= opcode+"_"+neighbour1
                    print_tags(out, inst)
                    op2_mthi_lo_func(opcode, out, result_register,result_address,iterator,pattern_count, inst, src1, src2, neighbour1,shift_amount)
                else:
                    if neighbour1 != neighbour2:
                        inst= opcode+"_"+neighbour2
                        print_tags(out, inst)
                        op2_mthi_lo_func(opcode, out, result_register,result_address,iterator,pattern_count, inst, src1, src2, neighbour2,shift_amount)
        elif((opcode == 'mfhi') or (opcode == 'mflo')):
            for x in range(2):
                if (x == 0):
                    inst= opcode+"_"+neighbour1
                    out.write("jal reset_offsets\n")
                    out.write("jal reset_hi_lo\n")
                    out.write("operation_"+inst+":\n")
                    op2_mfhi_lo_func(opcode, out, result_register,result_address,iterator,pattern_count, inst, src1, src2, neighbour1, shift_amount)
                else:
                    if neighbour1 != neighbour2:
                        inst= opcode+"_"+neighbour2
                        out.write("jal reset_offsets\n")
                        out.write("jal reset_hi_lo\n")
                        out.write("operation_"+inst+":\n")
                        op2_mfhi_lo_func(opcode, out, result_register,result_address,iterator,pattern_count, inst, src1, src2, neighbour2, shift_amount)
        elif((opcode == 'sll') or (opcode == 'sra') or (opcode == 'srl')):
            for x in range(2):
                if (x == 0):
                    inst= opcode+"_"+neighbour1
                    print_tags(out, inst)
                    op2_shift_amount_func(opcode, out, result_register,result_address,iterator,pattern_count, inst, shift_amount, src1, src2, neighbour1)
                else:
                    if neighbour1 != neighbour2:
                        inst= opcode+"_"+neighbour2
                        print_tags(out, inst)
                        op2_shift_amount_func(opcode, out, result_register,result_address,iterator,pattern_count, inst, shift_amount, src1, src2, neighbour2)
        else:
            for x in range(2):
                if (x == 0):
                    inst= opcode+"_"+neighbour1
                    #if not (instruction==x):
                    op2_func2(opcode, out, result_register,result_address,iterator,pattern_count, inst, src1, src2, neighbour1, shift_amount)
                else:
                    if neighbour1 != neighbour2:
                        inst= opcode+"_"+neighbour2
                        op2_func2(opcode, out, result_register,result_address,iterator,pattern_count, inst, src1, src2, neighbour2, shift_amount)

    print "...................................."

 #f.close()
 #f2.close()
