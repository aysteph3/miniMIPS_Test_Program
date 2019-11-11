# Copyright (C) 2019 Oyeniran Adeboye Stephen
import os
registerFile_1 = "../input/register_data_1.txt" # Data for testing register decoder
registerFile_0 = "../input/register_data_0.txt" # Data for testing register decoder


def reg_init_upward(out,data, number, pattern_address):
 out.write(" init_upward_"+str(number)+":\n")
 register = 0
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 31) or (register == 30)or (register == 0)):
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
  
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\tjr $31\n\n")
 data_f.close
def reg_init_downward(out,data, number, pattern_address):
 data_f = open(data,'r')
 out.write(" init_downward_"+str(number)+":\n")
 register = 31
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)
    
    if not ((register == 31) or (register == 30)or(register == 0)):
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
    if (register <= 0):
      register = 31
    else:
      register -= 1
 out.write("\tjr $31\n\n")
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
      out.write("\taddu $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
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
   
   if not((register == 1)or (register == 0)):
     out.write("\tnor $%d, $%d, $%d\n" % (register, register, register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
     out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
     out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
     offset += 4
     out.write("\taddu $%d, $%d, $%d\n" % (register, register, register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
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
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
  
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
    
    if  ((register == 31)or(register == 30)):
      out.write("\tnor $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
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
     out.write("\taddu $%d, $%d, $%d\n" % (register, register, register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
     out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
     out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
     offset += 4
     out.write("\tnor $%d, $%d, $%d\n" % (register, register, register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
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
    
    if  not ((register == 1)or (register == 0)):
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
  
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
    
    if  not ((register == 1)or(register == 0)):
      instruction = str.strip(inst)[0:5]
      out.write("\t%s $%d\n" % (inst, register))
      if ((inst == "mthi") or (inst == "multu1")):
        out.write("\tmfhi $%d\n" % (register))
      else:
        out.write("\tmflo $%d\n" % (register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
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
   
   if  not ((register == 1)or (register == 0)):
     out.write("\t%s $%d\n" % (inst, register))
     if ((inst == "mthi")or (inst == "multu1")):
      out.write("\tmfhi $%d\n" % (register))
     else:
      out.write("\tmflo $%d\n" % (register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
     out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
     out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
     offset += 4
     out.write("\t%s $%d\n" % (inst, register))
     #out.write(" %s $%d, $%d\n" % (instruction, register, register))
     if ((inst == "mthi")or (inst == "multu1")):
      out.write("\tmfhi $%d\n" % (register))
     else:
      out.write("\tmflo $%d\n" % (register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
     offset += 4
   if (register <= 0):
     register = 31
   else:
     register -= 1
 out.write("\n")

 data_f.close
 data_f2.close

############################################################################
#def store_load_upward(out,data, number, pattern_address, result_address):
# out.write(" store_load_upward_"+str(number)+":\n")
# register = 0
# offset = 0
# data_f = open(data,'r')
# line = data_f.readlines()
#
# for i in (line):
#    bit_set1 = i[:16]
#    bit_set2 = i[16:32]
#    most_sig_bit   = int(bit_set1,2)
#    least_sig_bit  = int(bit_set2,2)
#    
#    if not ((register == 31) or (register == 30)or(register == 0)):
#      #out.write(" sw $%d, %d($%s)\n" % (0, offset, result_address))
#      #if (number == 1):
#      #  out.write(" nor $%d, $%d, $%d\n" % (register, register, register))
#      #else:
#      out.write("\taddu $%d, $%d, $%d\n" % (register, register, register))
#      out.write("\tsw $%d, %d($%s)\n" % (register, offset, pattern_address))
#      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
#      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
#      offset += 4
#    if (register >= 31):
#      register = 0
#    else:
#      register += 1
# out.write("\tjr $31\n\n")
# data_f.close


#def store_load_downward(out,data, number, pattern_address, result_address):
# data_f = open(data,'r')
# out.write(" store_load_downward_"+str(number)+":\n")
# register = 31
# offset = 0
# line = data_f.readlines()

# for i in (line):
#    bit_set1 = i[:16]
#    bit_set2 = i[16:32]
#    most_sig_bit   = int(bit_set1,2)
#    least_sig_bit  = int(bit_set2,2)
#    
#    if not ((register == 31) or (register == 30)or (register == 0)):
#      #out.write(" sw $%d, %d($%s)\n" % (0, offset, result_address))
#      #if (number == 1):
#      #  out.write(" nor $%d, $%d, $%d\n" % (register, register, register))
#      #else:
#      out.write("\taddu $%d, $%d, $%d\n" % (register, register, register))
#      out.write("\tsw $%d, %d($%s)\n" % (register, offset, pattern_address))
#      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
#      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
#      offset += 4
#      #if (number == 1):
#      out.write("\taddu $%d, $%d, $%d\n" % (register, register, register))
#      #else:
#      #    out.write(" nor $%d, $%d, $%d\n" % (register, register, register))
#      out.write("\tsw $%d, %d($%s)\n" % (register, offset, pattern_address))
#      offset += 4
#    if (register <= 0):
#      register = 31
#    else:
#      register -= 1
# out.write("\tjr $31\n\n")
# data_f.close
 
#def reg_test_dat(out, result_address, pattern_address):
#  reg_init_upward(out, registerFile_1, 1, pattern_address)
##  store_load_upward(out,registerFile_0, 0, pattern_address, result_address)
##  store_load_downward(out,registerFile_1, 1, pattern_address, result_address)
##
#  reg_init_upward(out, registerFile_0, 0, pattern_address)
##  store_load_upward(out,registerFile_1, 1, pattern_address, result_address)
##  store_load_downward(out,registerFile_0, 0, pattern_address, result_address)
# 
###########################################################################
##                          HILO Register test                            #
###########################################################################
#  hi_upward_op(out,registerFile_0, 0, pattern_address, result_address)
#  hi_downward_op(out,registerFile_1, 1, pattern_address, result_address)
#  lo_upward_op(out,registerFile_0, 0, pattern_address, result_address)
#  lo_downward_op(out,registerFile_1, 1, pattern_address, result_address)
#
#  hi_upward_op(out,registerFile_1, 1, pattern_address, result_address)
#  hi_downward_op(out,registerFile_0, 0, pattern_address, result_address)
#  lo_upward_op(out,registerFile_1, 1, pattern_address, result_address)
#  lo_downward_op(out,registerFile_0, 0, pattern_address, result_address)
#
##########################################################################
#                  User-defined Special Register test                    #
##########################################################################
def special_register(out):
  out.write(";........initialize all registers..............;\n")
  out.write(" reg_special:\n")
  register = 0
  data_f = open(registerFile_1,'r')
  line = data_f.readlines()
  
  for i in (line):
     bit_set1 = i[:16]
     bit_set2 = i[16:32]
     most_sig_bit   = int(bit_set1,2)
     least_sig_bit  = int(bit_set2,2)
     out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
     out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
     if (register >= 31):
       register = 0
     else:
       register += 1
  out.write("\n")
  data_f.close

  out.write(";........test special purpose registers........;\n")
  result_address = 1
  res_address = 1
  out.write("\tlui $%d, %d\n" % (result_address, 1))
  out.write("\tori $%d, $%d, %d\n\n" % (result_address, result_address, 2000))

  reg_upward_special(out,registerFile_1, registerFile_0, res_address)
  reg_upward_special_mirror(out,registerFile_0, registerFile_1, res_address)

  out.write(";........test special purpose registers with HILO........;\n")
  hi_lo_upward_special(out,"mthi",registerFile_1, registerFile_0, result_address)
  hi_lo_upward_special(out,"mtlo", registerFile_1, registerFile_0, result_address)

##########################################################################
#                          HILO Register test                            #
##########################################################################
def hi_upward_op(out,data, number, pattern_address, result_address):
 out.write(" hi_upward_"+str(number)+":\n")
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
      out.write("\tmthi $%d\n" % ( register))
      out.write("\tmfhi $%d\n" % (register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, pattern_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\tjr $31\n\n")
 data_f.close


def hi_downward_op(out,data, number, pattern_address, result_address):
 out.write(" hi_downward_"+str(number)+":\n")
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
      out.write("\tmthi $%d\n" % ( register))
      out.write("\tmfhi $%d\n" % (register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, pattern_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      out.write("\tmthi $%d\n" % (register))
      out.write("\tmfhi $%d\n" % (register))
      offset += 4
      out.write(" sw $%d, %d($%s)\n" % (register, offset, pattern_address))
      offset += 4
    if (register <= 0):
      register = 31
    else:
      register -= 1
 out.write("\tjr $31\n\n")
 data_f.close


def lo_upward_op(out,data, number, pattern_address, result_address):
 out.write(" lo_upward_"+str(number)+":\n")
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
      out.write("\tmtlo $%d\n" % (register))
      out.write("\tmflo $%d\n" % (register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, pattern_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\tjr $31\n\n")
 data_f.close


def lo_downward_op(out,data, number, pattern_address, result_address):
 out.write( "lo_downward_"+str(number)+":\n")
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
      out.write("\tmtlo $%d\n" % (register))
      out.write("\tmflo $%d\n" % (register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, pattern_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      out.write("\tmtlo $%d\n" % (register))
      out.write("\tmflo $%d\n" % (register))
      offset += 4
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, pattern_address))
      offset += 4
    if (register <= 0):
      register = 31
    else:
      register -= 1
 out.write("\tjr $31\n\n")
 data_f.close

##########################################################################
#def reg_test(out, result_address, pattern_address):
#  out.write("jal reset_offsets\n")
#  out.write("register_operation:\n")
#  out.write(" jal init_upward_1\n")
#  out.write(" jal store_load_upward_0\n")
#  out.write(" jal store_load_downward_1\n\n")

#  out.write("jal reset_offsets\n")
#  out.write("register_operation_2:\n")
#  out.write(" jal init_upward_0\n")
#  out.write(" jal store_load_upward_1\n")
#  out.write(" jal store_load_downward_0\n")
#  out.write("\n")

#def hilo(out, result_address, pattern_address):
#  ######################################
#  out.write("jal reset_offsets\n")
#  out.write("jal reset_hi_lo\n")
#  out.write("hilo_register_operation:\n")
#  out.write(" jal init_upward_1\n")
#  out.write(" jal hi_upward_0\n")
#  out.write(" jal hi_downward_1\n")
#  out.write(" jal lo_upward_0\n")
#  out.write(" jal lo_downward_1\n")
#
#  out.write(" jal init_upward_0\n")
#  out.write(" jal hi_upward_1\n")
#  out.write(" jal hi_downward_0\n")
#  out.write(" jal lo_upward_1\n")
#  out.write(" jal lo_downward_0\n")
#  out.write("\n")


def cop_register(out,result_address):
  out.write("jal reset_offsets\n")
  out.write("cop0_register:\n")
  offset = 0
  out.write("\tlui $%d, %d\n" % (1, 65535))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  #out.write("\tmtc0 $%d, $%d\n" % (1, 12))
  out.write("\tmtc0 $%d, $%d\n" % (1, 13))
  out.write("\tmtc0 $%d, $%d\n" % (1, 14))
  out.write("\tmtc0 $%d, $%d\n" % (1, 15))

  #out.write("\tmfc0 $%d, $%d\n" % (1, 12))
  #out.write("\tmtc0 $%d, $%d\n" % (0, 12))
  out.write("\tmfc0 $%d, $%d\n" % (2, 13))
  out.write("\tswc0 $%d, %d($%s)\n" % (13, offset, result_address))
  offset +=4
  out.write("\tsw $%d, %d($%s)\n" % (2, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 13))
  out.write("\tmfc0 $%d, $%d\n" % (3, 14))
  out.write("\tswc0 $%d, %d($%s)\n" % (14, offset, result_address))
  offset +=4
  out.write("\tsw $%d, %d($%s)\n" % (3, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 14))
  out.write("\tmfc0 $%d, $%d\n" % (4, 15))
  out.write("\tswc0 $%d, %d($%s)\n" % (15, offset, result_address))
  offset +=4
  out.write("\tsw $%d, %d($%s)\n" % (4, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 15))

  #out.write("\tmfc0 $%d, $%d\n" % (1, 12))
  #out.write("\tlui $%d, %d\n" % (1, 65535))
  #out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  #out.write("\tmtc0 $%d, $%d\n" % (1, 12))
  #out.write("\tmfc0 $%d, $%d\n" % (1, 12))

  out.write("\tmfc0 $%d, $%d\n" % (5, 13))
  out.write("\tswc0 $%d, %d($%s)\n" % (13, offset, result_address))
  offset +=4
  out.write("\tsw $%d, %d($%s)\n" % (5, offset, result_address))
  offset +=4
  #out.write("\tlui $%d, %d\n" % (1, 65535))
  #out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  out.write("\tmtc0 $%d, $%d\n" % (1, 13))
  out.write("\tmfc0 $%d, $%d\n" % (6, 13))
  out.write("\tswc0 $%d, %d($%s)\n" % (13, offset, result_address))
  offset +=4
  out.write("\tsw $%d, %d($%s)\n" % (6, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (7, 14))
  out.write("\tswc0 $%d, %d($%s)\n" % (14, offset, result_address))
  offset +=4
  out.write("\tsw $%d, %d($%s)\n" % (7, offset, result_address))
  offset +=4
  #out.write("\tlui $%d, %d\n" % (1, 65535))
  #out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  out.write("\tmtc0 $%d, $%d\n" % (1, 14))
  out.write("\tmfc0 $%d, $%d\n" % (8, 14))
  out.write("\tswc0 $%d, %d($%s)\n" % (14, offset, result_address))
  offset +=4
  out.write("\tsw $%d, %d($%s)\n" % (8, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (9, 15))
  out.write("\tswc0 $%d, %d($%s)\n" % (15, offset, result_address))
  offset +=4
  out.write("\tsw $%d, %d($%s)\n" % (9, offset, result_address))
  offset +=4
  #out.write("\tlui $%d, %d\n" % (1, 65535))
  #out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  out.write("\tmtc0 $%d, $%d\n" % (1, 15))
  out.write("\tmfc0 $%d, $%d\n" % (10, 15))
  out.write("\tswc0 $%d, %d($%s)\n" % (15, offset, result_address))
  offset +=4
  out.write("\tsw $%d, %d($%s)\n\n" % (10, offset, result_address))
  offset +=4

  out.write(";........coprocessor mirror........;\n")
  out.write("\tlui $%d, %d\n" % (1, 65535))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535)) # can set this to 1 and remove register 17
  #out.write("\tlui $%d, %d\n" % (17, 65535))
  #out.write("\tori $%d, $%d, %d\n" % (17, 17, 65535))
 
  out.write("\tmtc0 $%d, $%d\n" % (0, 13)) 
  out.write("\tmtc0 $%d, $%d\n" % (0, 14))
  out.write("\tmtc0 $%d, $%d\n" % (0, 15))

  out.write("\tmfc0 $%d, $%d\n" % (11, 13))
  out.write("\tsw $%d, %d($%s)\n" % (11, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 13))
  out.write("\tmfc0 $%d, $%d\n" % (12, 14))
  out.write("\tsw $%d, %d($%s)\n" % (12, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 14))
  out.write("\tmfc0 $%d, $%d\n" % (13, 15))
  out.write("\tsw $%d, %d($%s)\n" % (13, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 15))

  out.write("\tmfc0 $%d, $%d\n" % (14, 13))
  out.write("\tsw $%d, %d($%s)\n" % (14, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 13))
  out.write("\tmfc0 $%d, $%d\n" % (15, 13))
  out.write("\tsw $%d, %d($%s)\n" % (15, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (16, 14))
  out.write("\tsw $%d, %d($%s)\n" % (16, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 14))
  out.write("\tmfc0 $%d, $%d\n" % (17, 14))
  out.write("\tsw $%d, %d($%s)\n" % (17, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (18, 15))
  out.write("\tsw $%d, %d($%s)\n" % (18, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 15))
  out.write("\tmfc0 $%d, $%d\n" % (19, 15))
  out.write("\tsw $%d, %d($%s)\n\n" % (19, offset, result_address))
