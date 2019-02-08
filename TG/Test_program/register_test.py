# Copyright (C) 2019 Oyeniran Adeboye Stephen
import os
registerFile_1 = "../input/register_data_1.txt" # Data for testing register decoder
registerFile_0 = "../input/register_data_0.txt" # Data for testing register decoder


def reg_init_upward(out,data, number, pattern_address):
 out.write("init_upward_"+str(number)+":\n")
 register = 0
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 31) or (register == 30)or (register == 0)):
      out.write(" lui $%d, %d\n" % (register, most_sig_bit))
      out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
  
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write(" jr $31\n\n")
 data_f.close


def reg_init_downward(out,data, number, pattern_address):
 data_f = open(data,'r')
 out.write("init_downward_"+str(number)+":\n")
 register = 31
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 31) or (register == 30)or(register == 0)):
      out.write(" lui $%d, %d\n" % (register, most_sig_bit))
      out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
    if (register <= 0):
      register = 31
    else:
      register -= 1
 out.write(" jr $31\n\n")
 data_f.close

 ##################################
def reg_upward_special(out,data, data2, result_address):
 register = 0
 offset = 0
 data_f = open(data,'r')
 line = data_f.readlines()

 data_f2 = open(data2,'r')
 line2 = data_f2.readlines()
 for i in (line2):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 1)or(register == 0)):
      out.write(" addu $%d, $%d, $%d\n" % (register, register, register))
      out.write(" sw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write(" lui $%d, %d\n" % (register, most_sig_bit))
      out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\n")

 for i in (line):
   bit_set1 = i[:16]
   bit_set2 = i[16:32]
   most_sig_bit   = int(bit_set1,2)
   least_sig_bit  = int(bit_set2,2)
   
   if not ((register == 1)or (register == 0)):
     out.write(" nor $%d, $%d, $%d\n" % (register, register, register))
     out.write(" sw $%d, %d($%s)\n" % (register, offset, result_address))
     out.write(" lui $%d, %d\n" % (register, most_sig_bit))
     out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
     offset += 4
     out.write(" addu $%d, $%d, $%d\n" % (register, register, register))
     out.write(" sw $%d, %d($%s)\n" % (register, offset, result_address))
     offset += 4
   if (register <= 0):
     register = 31
   else:
     register -= 1
 out.write("\n")

 data_f.close
 data_f2.close

def reg_upward_special_mirror(out,data, data2, result_address):
 out.write(";.............special register mirror.............;\n")
 register = 0
 offset = 0
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 1)or (register == 0)):
      out.write(" lui $%d, %d\n" % (register, most_sig_bit))
      out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
  
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\n")
 data_f2 = open(data2,'r')
 line2 = data_f2.readlines()
 for i in (line2):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 1)or(register == 0)):
      out.write(" nor $%d, $%d, $%d\n" % (register, register, register))
      out.write(" sw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write(" lui $%d, %d\n" % (register, most_sig_bit))
      out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\n")

 for i in (line):
   bit_set1 = i[:16]
   bit_set2 = i[16:32]
   most_sig_bit   = int(bit_set1,2)
   least_sig_bit  = int(bit_set2,2)
   
   if not ((register == 1)or (register == 0)):
     out.write(" addu $%d, $%d, $%d\n" % (register, register, register))
     out.write(" sw $%d, %d($%s)\n" % (register, offset, result_address))
     out.write(" lui $%d, %d\n" % (register, most_sig_bit))
     out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
     offset += 4
     out.write(" nor $%d, $%d, $%d\n" % (register, register, register))
     out.write(" sw $%d, %d($%s)\n" % (register, offset, result_address))
     offset += 4
   if (register <= 0):
     register = 31
   else:
     register -= 1
 out.write("\n")

 data_f.close
 data_f2.close


def hi_lo_upward_special(out,inst,data, data2, result_address):
 register = 0
 offset = 0
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 1)or (register == 0)):
      out.write(" lui $%d, %d\n" % (register, most_sig_bit))
      out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
  
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\n")

 data_f2 = open(data2,'r')
 line2 = data_f2.readlines()
 for i in (line2):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 1)or(register == 0)):
      instruction = str.strip(inst)[0:5]
      #out.write(" %s $%d\n" % (inst, register))
      out.write(" %s $%d, $%d\n" % (instruction, register, register))
      if ((inst == "mthi") or (inst == "multu1")):
        out.write(" mfhi $%d\n" % (register))
      else:
        out.write(" mflo $%d\n" % (register))
      out.write(" sw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write(" lui $%d, %d\n" % (register, most_sig_bit))
      out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\n")

 for i in (line):
   bit_set1 = i[:16]
   bit_set2 = i[16:32]
   most_sig_bit   = int(bit_set1,2)
   least_sig_bit  = int(bit_set2,2)
   
   if not ((register == 1)or (register == 0)):
     #out.write(" %s $%d\n" % (inst, register))
     out.write(" %s $%d, $%d\n" % (instruction, register, register))
     if ((inst == "mthi")or (inst == "multu1")):
      out.write(" mfhi $%d\n" % (register))
     else:
      out.write(" mflo $%d\n" % (register))
     out.write(" sw $%d, %d($%s)\n" % (register, offset, result_address))
     out.write(" lui $%d, %d\n" % (register, most_sig_bit))
     out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
     offset += 4
     #out.write(" %s $%d\n" % (inst, register))
     out.write(" %s $%d, $%d\n" % (instruction, register, register))
     if ((inst == "mthi")or (inst == "multu1")):
      out.write(" mfhi $%d\n" % (register))
     else:
      out.write(" mflo $%d\n" % (register))
     out.write(" sw $%d, %d($%s)\n" % (register, offset, result_address))
     offset += 4
   if (register <= 0):
     register = 31
   else:
     register -= 1
 out.write("\n")

 data_f.close
 data_f2.close

 #def hi_lo_upward_special_mirror(out,inst,data, data2, result_address):
 #out.write(";.............HILO special register mirror.............;\n")
 #register = 0
 #offset = 0
 #data_f = open(data,'r')
 #line = data_f.readlines()
#
 #for i in (line):
 #   bit_set1 = i[:16]
 #   bit_set2 = i[16:32]
 #   most_sig_bit   = int(bit_set1,2)
 #   least_sig_bit  = int(bit_set2,2)
 #   
 #   if not ((register == 1)or (register == 0)):
 #     out.write(" lui $%d, %d\n" % (register, most_sig_bit))
 #     out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
 # 
 #   if (register >= 31):
 #     register = 0
 #   else:
 #     register += 1
 #out.write("\n")
 #data_f2 = open(data2,'r')
 #line2 = data_f2.readlines()
 #for i in (line2):
 #   bit_set1 = i[:16]
 #   bit_set2 = i[16:32]
 #   most_sig_bit   = int(bit_set1,2)
 #   least_sig_bit  = int(bit_set2,2)
 #   
 #   if not ((register == 1)or(register == 0)):
 #     instruction = str.strip(inst)[0:5]
 #     #out.write(" %s $%d\n" % (inst, register))
 #     out.write(" %s $%d, $%d\n" % (instruction, register, register))
 #     if ((inst == "mthi") or (inst == "multu1")):
 #       out.write(" mfhi $%d\n" % (register))
 #     else:
 #       out.write(" mflo $%d\n" % (register))
 #     out.write(" sw $%d, %d($%s)\n" % (register, offset, result_address))
 #     out.write(" lui $%d, %d\n" % (register, most_sig_bit))
 #     out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
 #     offset += 4
 #   if (register >= 31):
 #     register = 0
 #   else:
 #     register += 1
 #out.write("\n")
#
 #for i in (line):
 #  bit_set1 = i[:16]
 #  bit_set2 = i[16:32]
 #  most_sig_bit   = int(bit_set1,2)
 #  least_sig_bit  = int(bit_set2,2)
 #  
 #  if not ((register == 1)or (register == 0)):
 #    out.write(" %s $%d, $%d\n" % (instruction, register, register))
 #    if ((inst == "mthi")or (inst == "multu1")):
 #     out.write(" mfhi $%d\n" % (register))
 #    else:
 #     out.write(" mflo $%d\n" % (register))
 #    out.write(" sw $%d, %d($%s)\n" % (register, offset, result_address))
 #    out.write(" lui $%d, %d\n" % (register, most_sig_bit))
 #    out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
 #    offset += 4
 #    out.write(" %s $%d, $%d\n" % (instruction, register, register))
 #    if ((inst == "mthi")or (inst == "multu1")):
 #     out.write(" mfhi $%d\n" % (register))
 #    else:
 #     out.write(" mflo $%d\n" % (register))
 #    out.write(" sw $%d, %d($%s)\n" % (register, offset, result_address))
 #    offset += 4
 #  if (register <= 0):
 #    register = 31
 #  else:
 #    register -= 1
 #out.write("\n")
#
 #data_f.close
 #data_f2.close

#####################################

def store_load_upward(out,data, number, pattern_address, result_address):
 out.write("store_load_upward_"+str(number)+":\n")
 register = 0
 offset = 0
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 31) or (register == 30)or(register == 0)):
      #out.write(" sw $%d, %d($%s)\n" % (0, offset, result_address))
      #if (number == 1):
      #  out.write(" nor $%d, $%d, $%d\n" % (register, register, register))
      #else:
      out.write(" addu $%d, $%d, $%d\n" % (register, register, register))
      out.write(" sw $%d, %d($%s)\n" % (register, offset, pattern_address))
      out.write(" lui $%d, %d\n" % (register, most_sig_bit))
      out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write(" jr $31\n\n")
 data_f.close

def store_load_downward(out,data, number, pattern_address, result_address):
 data_f = open(data,'r')
 out.write("store_load_downward_"+str(number)+":\n")
 register = 31
 offset = 0
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 31) or (register == 30)or (register == 0)):
      #out.write(" sw $%d, %d($%s)\n" % (0, offset, result_address))
      #if (number == 1):
      #  out.write(" nor $%d, $%d, $%d\n" % (register, register, register))
      #else:
      out.write(" addu $%d, $%d, $%d\n" % (register, register, register))
      out.write(" sw $%d, %d($%s)\n" % (register, offset, pattern_address))
      out.write(" lui $%d, %d\n" % (register, most_sig_bit))
      out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
      #if (number == 1):
      out.write(" addu $%d, $%d, $%d\n" % (register, register, register))
      #else:
      #    out.write(" nor $%d, $%d, $%d\n" % (register, register, register))
      out.write(" sw $%d, %d($%s)\n" % (register, offset, pattern_address))
      offset += 4
    if (register <= 0):
      register = 31
    else:
      register -= 1
 out.write(" jr $31\n\n")
 data_f.close
 
def reg_test_dat(out, result_address, pattern_address):
  reg_init_upward(out, registerFile_1, 1, pattern_address)
  store_load_upward(out,registerFile_0, 0, pattern_address, result_address)
  store_load_downward(out,registerFile_1, 1, pattern_address, result_address)

  reg_init_upward(out, registerFile_0, 0, pattern_address)
  store_load_upward(out,registerFile_1, 1, pattern_address, result_address)
  store_load_downward(out,registerFile_0, 0, pattern_address, result_address)
 

  #reg_init_upward(out, registerFile_1, 1, pattern_address)
  #store_load_regular(out,registerFile_0, 0, pattern_address, result_address)
  #reg_init_upward(out, registerFile_0, 0, pattern_address)
  #store_load_regular2(out,registerFile_1, 1, pattern_address, result_address)


  #reg_init_downward(out, registerFile_1, 1, pattern_address)
  #reg_store_upward(out, result_address)
  #reg_store_downward(out, result_address)
  #mthi_upward(out)
  #mtlo_upward(out)
  #mfhi_upward(out)
  #mflo_upward(out)
  #mthi_downward(out)
  #mtlo_downward(out)
  #mfhi_downward(out)
  #mflo_downward(out)

##########################################################################
#                          HILO Register test                            #
##########################################################################
  hi_upward_op(out,registerFile_0, 0, pattern_address, result_address)
  hi_downward_op(out,registerFile_1, 1, pattern_address, result_address)
  lo_upward_op(out,registerFile_0, 0, pattern_address, result_address)
  lo_downward_op(out,registerFile_1, 1, pattern_address, result_address)

  hi_upward_op(out,registerFile_1, 1, pattern_address, result_address)
  hi_downward_op(out,registerFile_0, 0, pattern_address, result_address)
  lo_upward_op(out,registerFile_1, 1, pattern_address, result_address)
  lo_downward_op(out,registerFile_0, 0, pattern_address, result_address)
###########################################################################


##########################################################################
#                  User-defined Special Register test                    #
##########################################################################
def special_register(out):
  out.write(";........initialize all registers..............;\n")
  out.write("reg_special:\n")
  register = 0
  data_f = open(registerFile_1,'r')
  line = data_f.readlines()
  
  for i in (line):
     bit_set1 = i[:16]
     bit_set2 = i[16:32]
     most_sig_bit   = int(bit_set1,2)
     least_sig_bit  = int(bit_set2,2)
     out.write(" lui $%d, %d\n" % (register, most_sig_bit))
     out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
     if (register >= 31):
       register = 0
     else:
       register += 1
  out.write("\n")
  data_f.close

  out.write(";........test special purpose registers........;\n")
  result_address = 1
  res_address = 1
  out.write(" lui $%d, %d\n" % (result_address, 1))
  out.write(" ori $%d, $%d, %d\n\n" % (result_address, result_address, 2000))

  reg_upward_special(out,registerFile_1, registerFile_0, res_address)
  reg_upward_special_mirror(out,registerFile_0, registerFile_1, res_address)

  hi_lo_upward_special(out,"multu1",registerFile_1, registerFile_0, result_address)
  hi_lo_upward_special(out,"multu2", registerFile_1, registerFile_0, result_address)

  #hi_lo_upward_special_mirror(out,"multu1",registerFile_0, registerFile_1, result_address)
  #hi_lo_upward_special_mirror(out,"multu2",registerFile_0, registerFile_1, result_address)

  #out.write(" addu $%d, $%d, $%d\n" % (29, 29, 29))
  #out.write(" sw $%d, %d($%d)\n" % (29, 0, result_address))
  #out.write(" lui $%d, %d\n" % (29, 0))
  #out.write(" ori $%d, $%d, %d\n" % (29, 29, 0))

  ####out.write(" addu $%d, $%d, $%d\n" % (30, 30, 30))
  ####out.write(" sw $%d, %d($%d)\n" % (30, 4, result_address))
  ####out.write(" lui $%d, %d\n" % (30, 0))
  ####out.write(" ori $%d, $%d, %d\n" % (30, 30, 0))
####
  ####out.write(" addu $%d, $%d, $%d\n" % (31, 31, 31))
  ####out.write(" sw $%d, %d($%d)\n" % (31, 8, result_address))
  ####out.write(" lui $%d, %d\n" % (31, 0))
  ####out.write(" ori $%d, $%d, %d\n\n" % (31, 31, 0))
####
  ####out.write(" addu $%d, $%d, $%d\n" % (31, 31, 31))
  ####out.write(" sw $%d, %d($%d)\n" % (31, 12, result_address))
  ####out.write(" lui $%d, %d\n" % (31, 65535))
  ####out.write(" ori $%d, $%d, %d\n" % (31, 31, 65535))
  ####out.write(" addu $%d, $%d, $%d\n" % (31, 31, 31))
  ####out.write(" sw $%d, %d($%d)\n" % (31, 16, result_address))
####
  ####out.write(" addu $%d, $%d, $%d\n" % (30, 30, 30))
  ####out.write(" sw $%d, %d($%d)\n" % (30, 20, result_address))
  ####out.write(" lui $%d, %d\n" % (30, 65535))
  ####out.write(" ori $%d, $%d, %d\n" % (30, 30, 65535))
  ####out.write(" addu $%d, $%d, $%d\n" % (30, 30, 30))
  ####out.write(" sw $%d, %d($%d)\n" % (30, 24, result_address))
####
  #out.write(" addu $%d, $%d, $%d\n" % (29, 29, 29))
  #out.write(" sw $%d, %d($%d)\n" % (29, 20, result_address))
  #out.write(" lui $%d, %d\n" % (29, 65535))
  #out.write(" ori $%d, $%d, %d\n" % (29, 29, 65535))
  #out.write(" addu $%d, $%d, $%d\n" % (29, 29, 29))
  #out.write(" sw $%d, %d($%d)\n" % (29, 28, result_address))

##########################################################################
#                          HILO Register test                            #
##########################################################################
def hi_upward_op(out,data, number, pattern_address, result_address):
 out.write("hi_upward_"+str(number)+":\n")
 register = 0
 offset = 0
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 31) or (register == 30)or (register == 0)):
      out.write(" multu $%d, $%d\n" % (register, register))
      out.write(" mfhi $%d\n" % (register))
      out.write(" sw $%d, %d($%s)\n" % (register, offset, pattern_address))
      out.write(" lui $%d, %d\n" % (register, most_sig_bit))
      out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write(" jr $31\n\n")
 data_f.close


def hi_downward_op(out,data, number, pattern_address, result_address):
 out.write("hi_downward_"+str(number)+":\n")
 register = 0
 offset = 0
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 31) or (register == 30)or (register == 0)):
      out.write(" multu $%d, $%d\n" % (register, register))
      out.write(" mfhi $%d\n" % (register))
      out.write(" sw $%d, %d($%s)\n" % (register, offset, pattern_address))
      out.write(" lui $%d, %d\n" % (register, most_sig_bit))
      out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      out.write(" multu $%d, $%d\n" % (register, register))
      out.write(" mfhi $%d\n" % (register))
      offset += 4
      out.write(" sw $%d, %d($%s)\n" % (register, offset, pattern_address))
      offset += 4
    if (register <= 0):
      register = 31
    else:
      register -= 1
 out.write(" jr $31\n\n")
 data_f.close


def lo_upward_op(out,data, number, pattern_address, result_address):
 out.write("lo_upward_"+str(number)+":\n")
 register = 0
 offset = 0
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 31) or (register == 30)or (register == 0)):
      out.write(" multu $%d, $%d\n" % (register, register))
      out.write(" mflo $%d\n" % (register))
      out.write(" sw $%d, %d($%s)\n" % (register, offset, pattern_address))
      out.write(" lui $%d, %d\n" % (register, most_sig_bit))
      out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write(" jr $31\n\n")
 data_f.close


def lo_downward_op(out,data, number, pattern_address, result_address):
 out.write("lo_downward_"+str(number)+":\n")
 register = 0
 offset = 0
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 31) or (register == 30)or (register == 0)):
      out.write(" multu $%d, $%d\n" % (register, register))
      out.write(" mflo $%d\n" % (register))
      out.write(" sw $%d, %d($%s)\n" % (register, offset, pattern_address))
      out.write(" lui $%d, %d\n" % (register, most_sig_bit))
      out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      out.write(" multu $%d, $%d\n" % (register, register))
      out.write(" mflo $%d\n" % (register))
      offset += 4
      out.write(" sw $%d, %d($%s)\n" % (register, offset, pattern_address))
      offset += 4
    if (register <= 0):
      register = 31
    else:
      register -= 1
 out.write(" jr $31\n\n")
 data_f.close

##########################################################################


#def mthi_upward(out):
#  out.write("mthi_upward:\n")
#  for x in range(31):
#    if not ((x == 31) or (x == 30)or (x == 29)or (x == 0)):
#      out.write(" mthi $%d\n" % (x))
#  out.write(" jr $31\n\n")
#
#def mtlo_upward(out):
#  out.write("mtlo_upward:\n")
#  for x in range(31):
#    if not ((x == 31) or (x == 30)or (x == 29)or (x == 0)):
#      out.write(" mtlo $%d\n" % (x))
#  out.write(" jr $31\n\n")
#
#def mfhi_upward(out):
#  out.write("mfhi_upward:\n")
#  for x in range(31):
#    if not ((x == 31) or (x == 30)or (x == 29)or (x == 0)):
#      out.write(" mfhi $%d\n" % (x))
#  out.write(" jr $31\n\n")
#
#def mflo_upward(out):
#  out.write("mflo_upward:\n")
#  offset = 0
#  for x in range(31):
#    if not ((x == 31) or (x == 30)or (x == 29)or (x == 0)):
#      out.write(" mflo $%d\n" % (x))
#  out.write(" jr $31\n\n")
#
#def mthi_downward(out):
#  out.write("mthi_downward:\n")
#  for x in range(31, -1 , -1):
#    if not ((x == 31) or (x == 30)or (x == 29)or (x == 0)):
#      out.write(" mthi $%d\n" % (x))
#  out.write(" jr $31\n\n")
#
#def mtlo_downward(out):
#  out.write("mtlo_downward:\n")
#  for x in range(31, -1 , -1):
#    if not ((x == 31) or (x == 30)or (x == 29)or (x == 0)):
#      out.write(" mtlo $%d\n" % (x))
#  out.write(" jr $31\n\n")
#
#def mfhi_downward(out):
#  out.write("mfhi_downward:\n")
#  for x in range(31, -1 , -1):
#    if not ((x == 31) or (x == 30)or (x == 29)or (x == 0)):
#      out.write(" mfhi $%d\n" % (x))
#  out.write(" jr $31\n\n")
#
#def mflo_downward(out):
#  out.write("mflo_downward:\n")
#  for x in range(31, -1 , -1):
#    if not ((x == 31) or (x == 30)or (x == 29)or (x == 0)):
#      out.write(" mflo $%d\n" % (x))
#  out.write(" jr $31\n\n")


def reg_test(out, result_address, pattern_address):
  out.write("jal reset_offsets\n")
  out.write("register_operation:\n")
  out.write(" jal init_upward_1\n")
  out.write(" jal store_load_upward_0\n")
  out.write(" jal store_load_downward_1\n\n")

  out.write("jal reset_offsets\n")
  out.write("register_operation_2:\n")
  out.write(" jal init_upward_0\n")
  out.write(" jal store_load_upward_1\n")
  out.write(" jal store_load_downward_0\n")
  out.write("\n")

def hilo(out, result_address, pattern_address):
  #out.write("jal reset_offsets\n")
  #out.write("hilo_register_operation:\n")
  #out.write(" jal init_upward_1\n")
  #out.write(" jal mthi_upward\n")
  #out.write(" jal mfhi_upward\n")
  #out.write(" jal store_upward\n")
  #out.write(" jal mtlo_upward\n")
  #out.write(" jal mflo_upward\n")
  #out.write(" jal store_upward\n\n")
#
  #out.write(" jal init_upward_0\n")
  #out.write(" jal mthi_downward\n")
  #out.write(" jal mfhi_downward\n")
  #out.write(" jal store_downward\n")
  #out.write(" jal mtlo_downward\n")
  #out.write(" jal mflo_downward\n")
  #out.write(" jal store_downward\n\n")
#
  #out.write(" jal init_downward_1\n")
  #out.write(" jal mthi_downward\n")
  #out.write(" jal mfhi_downward\n")
  #out.write(" jal store_downward\n")
  #out.write(" jal mtlo_downward\n")
  #out.write(" jal mflo_downward\n")
  #out.write(" jal store_downward\n")
  ######################################
  out.write("jal reset_offsets\n")
  out.write("hilo_register_operation:\n")
  out.write(" jal init_upward_1\n")
  out.write(" jal hi_upward_0\n")
  out.write(" jal hi_downward_1\n")
  out.write(" jal lo_upward_0\n")
  out.write(" jal lo_downward_1\n")

  out.write(" jal init_upward_0\n")
  out.write(" jal hi_upward_1\n")
  out.write(" jal hi_downward_0\n")
  out.write(" jal lo_upward_1\n")
  out.write(" jal lo_downward_0\n")
  out.write("\n")