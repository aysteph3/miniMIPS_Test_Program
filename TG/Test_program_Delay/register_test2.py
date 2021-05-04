# Copyright (C) 2019 Oyeniran Adeboye Stephen
import os
registerFile_1 = "../input/register_data_1.txt" # Data for testing register decoder
registerFile_0 = "../input/register_data_0.txt" # Data for testing register decoder
offset = 0

##################################################################################
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

    if not ((register == 31) or (register == 29)):
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))

    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\tjr $31\n\n")
 data_f.close

##################################################################################
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

    if not ((register == 31) or (register == 29)):
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
    if (register <= 0):
      register = 31
    else:
      register -= 1
 out.write("\tjr $31\n\n")
 data_f.close

##################################################################################
def reg_upward_special(out,data, data2, result_address):
 register = 0
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()

 data_f2 = open(data2,'r')
 line2 = data_f2.readlines()
 for i in (line2):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 1)):
      out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
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

   if not((register == 1)):
     out.write("\tnor $%d, $%d, $%d\n" % (register, register, register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
     out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
     out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
     offset += 4
     out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
     offset += 4
   if (register <= 0):
     register = 31
   else:
     register -= 1
 out.write("\n")

 data_f.close
 data_f2.close

def reg_tdf_10(out, result_address):
 out.write("\t;.............tdf test 10 ...............;\n ")
 global offset
 for register in range(0,31):
    out.write("\t;........Register....... %d;\n" % (register))
    if not ((register == int(result_address))):
      out.write("\tlui $%d, %d\n" % (register, 65535))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 65535))
      for j in range(register+1, register+5):
          if (register >=26):
              j -= 5
          out.write("\tlui $%d, %d\n" % (j, 0))
          out.write("\tori $%d, $%d, %d\n" % (j, j, 0))
          out.write("\tnor $%d, $%d, $%d\n" % (register, register, register))
          out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
          offset += 4
          out.write("\tnor $%d, $%d, $%d\n" % (j, j, j))
          out.write("\tsw $%d, %d($%s)\n" % (j, offset, result_address))
          offset += 4
 out.write("\n")

def reg_tdf_01(out, result_address):
 out.write("\t;.............tdf test 10 ...............;\n ")
 global offset
 for register in range(0,31):
    out.write("\t;........Register....... %d;\n" % (register))
    if not ((register == int(result_address))):
      out.write("\tlui $%d, %d\n" % (register, 0))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 0))
      for j in range(register+1, register+5):
          if (register >=26):
              j -= 5
          out.write("\tlui $%d, %d\n" % (j, 65535))
          out.write("\tori $%d, $%d, %d\n" % (j, j, 65535))
          out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
          out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
          offset += 4
          out.write("\tand $%d, $%d, $%d\n" % (j, j, j))
          out.write("\tsw $%d, %d($%s)\n" % (j, offset, result_address))
          offset += 4
 out.write("\n")


def reg_upward_special_basic(out,result_register, result_address, data_list):
 out.write("\t;.............tdf test_basic ...............;\n ")
 register = 0
 global offset
 for list_register in data_list:
    register_j = list_register[0]
    register_i = list_register[1]
    out.write("\t;........Register....... %d;\n" % (register_j))
    if not ((register_j == int(result_address)) or (register_i == int(result_address)) or (register_j == int(result_register)) or (register_i == int(result_register))):
        out.write("\tand $%d, $%d, $%d\n" % (result_register, register_j, register_i))
        out.write("\tand $%d, $%d, $%d\n" % (result_register, register_i, register_j))
        out.write("\tsw $%d, %d($%s)\n" % (result_register, offset, result_address))
        out.write("\tlui $%d, %d\n" % (register_j, 0))
        out.write("\tori $%d, $%d, %d\n" % (register_j, register_j, 0))
        out.write("\tlui $%d, %d\n" % (register_i, 0))
        out.write("\tori $%d, $%d, %d\n" % (register_i, register_i, 0))
        offset += 4
        out.write("\n")

        out.write("\tnor $%d, $%d, $%d\n" % (result_register, register_j, register_i))
        out.write("\tnor $%d, $%d, $%d\n" % (result_register, register_i, register_j))
        out.write("\tsw $%d, %d($%s)\n" % (result_register, offset, result_address))
        out.write("\tlui $%d, %d\n" % (register_j, 65535))
        out.write("\tori $%d, $%d, %d\n" % (register_j, register_j, 65535))
        out.write("\tlui $%d, %d\n" % (register_i, 65535))
        out.write("\tori $%d, $%d, %d\n" % (register_i, register_i, 65535))
        offset += 4
        out.write("\tand $%d, $%d, $%d\n" % (result_register, register_j, register_i))
        out.write("\tand $%d, $%d, $%d\n" % (result_register, register_i, register_j))
        out.write("\tsw $%d, %d($%s)\n" % (result_register, offset, result_address))
        offset += 4
        out.write("\n")


def reg_upward_special_basic_2(out,result_register, result_address, data_list):
 out.write("\t;.............tdf test_basic ...............;\n ")
 register = 0
 global offset
 for list_register in data_list:
    register_j = list_register[0]
    register_i = list_register[1]
    out.write("\t;........Register....... %d;\n" % (register_j))
    if not ((register_j == int(result_address)) or (register_i == int(result_address)) or (register_j == int(result_register)) or (register_i == int(result_register))):
        out.write("\tlui $%d, %d\n" % (register_j, 0)) #
        out.write("\tori $%d, $%d, %d\n" % (register_j, register_j, 0))#
        out.write("\tlui $%d, %d\n" % (register_i, 65535))#
        out.write("\tori $%d, $%d, %d\n" % (register_i, register_i, 65535))#
        #out.write("\tor $%d, $%d, $%d\n" % (result_register, register_j, register_i))
        #out.write("\tor $%d, $%d, $%d\n" % (result_register, register_i, register_j))
        #out.write("\tsw $%d, %d($%s)\n" % (result_register, offset, result_address))

        out.write("\tor $%d, $%d, $%d\n" % (register_j, register_j, register_j))
        out.write("\tor $%d, $%d, $%d\n" % (register_j, register_i, register_j))
        out.write("\tsw $%d, %d($%s)\n" % (register_j, offset, result_address))
        offset += 4#
        out.write("\tlui $%d, %d\n" % (register_j, 0))
        out.write("\tori $%d, $%d, %d\n" % (register_j, register_j, 0))
        #out.write("\tlui $%d, %d\n" % (register_i, 0))
        #out.write("\tori $%d, $%d, %d\n" % (register_i, register_i, 0))
        out.write("\tor $%d, $%d, $%d\n" % (register_j, register_j, register_j))
        out.write("\tor $%d, $%d, $%d\n" % (register_j, register_j, register_i))
        out.write("\tsw $%d, %d($%s)\n" % (register_j, offset, result_address))#
        offset += 4
        out.write("\n")

        #out.write("\tnor $%d, $%d, $%d\n" % (result_register, register_j, register_i))
        #out.write("\tnor $%d, $%d, $%d\n" % (result_register, register_i, register_j))
        #out.write("\tsw $%d, %d($%s)\n" % (result_register, offset, result_address))
        #out.write("\tlui $%d, %d\n" % (register_j, 65535))
        #out.write("\tori $%d, $%d, %d\n" % (register_j, register_j, 65535))
        #out.write("\tlui $%d, %d\n" % (register_i, 65535))
        #out.write("\tori $%d, $%d, %d\n" % (register_i, register_i, 65535))
        #offset += 4
        #out.write("\tand $%d, $%d, $%d\n" % (result_register, register_j, register_i))
        #out.write("\tand $%d, $%d, $%d\n" % (result_register, register_i, register_j))
        #out.write("\tsw $%d, %d($%s)\n" % (result_register, offset, result_address))
        offset += 4
        out.write("\n")


def reg_tdf_hi_10(out, result_address):
 out.write("\t;.............tdf test_hi register 10 ...............;\n ")
 global offset
 for register in range(0,31):
    out.write("\t;........Register.......; %d\n" % (register))
    if not ((register == result_address)):
      out.write("\tlui $%d, %d\n" % (register, 65535))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 65535))
      out.write("\tmthi $%d\n" % (register))
      for j in range(register+1, register+5):
          if (register >=26):
              j -= 5
          out.write("\tlui $%d, %d\n" % (j, 0))
          out.write("\tori $%d, $%d, %d\n" % (j, j, 0))
          out.write("\tmthi $%d\n" % (j))
          out.write("\tmthi $%d\n" % (register))
          out.write("\tmfhi $%d\n" % (register))
          out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
          #offset += 4
          #out.write("\tmflo $%d\n" % (j))
          #out.write("\tsw $%d, %d($%s)\n" % (j, offset, result_address))
          offset += 4
 out.write("\n")

def reg_tdf_hi_01(out, result_address):
 out.write("\t;.............tdf test_hi register 01 ...............;\n ")
 global offset
 for register in range(0,31):
    out.write("\t;........Register.......; %d\n" % (register))
    if not ((register == result_address)):
      out.write("\tlui $%d, %d\n" % (register, 0))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 0))
      out.write("\tmthi $%d\n" % (register))
      for j in range(register+1, register+5):
          if (register >=26):
              j -= 5
          out.write("\tlui $%d, %d\n" % (j, 65535))
          out.write("\tori $%d, $%d, %d\n" % (j, j, 65535))
          out.write("\tmthi $%d\n" % (j))
          out.write("\tmthi $%d\n" % (register))
          out.write("\tmfhi $%d\n" % (register))
          out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
          #offset += 4
          #out.write("\tmflo $%d\n" % (j))
          #out.write("\tsw $%d, %d($%s)\n" % (j, offset, result_address))
          offset += 4
 out.write("\n")

def reg_tdf_datapath(out, result_address):
 out.write("\t;........register tdf datapth.......; \n")
 global offset
 for register in range(0,31):
    out.write("\t;........Register.......; %d\n" % (register))
    if not ((register == int(result_address))):
      out.write("\tlui $%d, %d\n" % (register, 65535))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 65535))
      out.write("\tlui $%d, %d\n" % (register, 0))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 0))
      out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, 65535))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 65535))
      offset += 4
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      offset += 4
 out.write("\n")

def reg_tdf_load(out, result_address):
 out.write("\t;.............tdf test load ...............;\n ")
 global offset
 for register in range(0,31):
    out.write("\t;........Register....... %d;\n" % (register))
    if not ((register == int(result_address))):
      for j in range(register+1, register+5):
          if (register >=26):
              j -= 5
          out.write("\tlui $%d, %d\n" % (register, 0))
          out.write("\tori $%d, $%d, %d\n" % (register, register, 0))
          #out.write("\tnor $%d, $%d, $%d\n" % (register, register, register)) #
          out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
          out.write("\tlui $%d, %d\n" % (j, 0))
          out.write("\tori $%d, $%d, %d\n" % (j, j, 0))
          out.write("\tlui $%d, %d\n" % (register, 65535))
          out.write("\tori $%d, $%d, %d\n" % (register, register, 65535))
          #out.write("\tand $%d, $%d, $%d\n" % (register, register, register)) #
          #out.write("\tand $%d, $%d, $%d\n" % (j, j, j)) #
          out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
          offset += 4
          out.write("\tsw $%d, %d($%s)\n" % (j, offset, result_address))
          out.write("\tlui $%d, %d\n" % (register, 0))
          out.write("\tori $%d, $%d, %d\n" % (register, register, 0))
          out.write("\tlui $%d, %d\n" % (j, 65535))
          out.write("\tori $%d, $%d, %d\n" % (j, j, 65535))
          #out.write("\tand $%d, $%d, $%d\n" % (j, j, j)) #
          out.write("\tsw $%d, %d($%s)\n" % (j, offset, result_address))
          offset += 4
 out.write("\n")


def reg_tdf_datapath_master(out, result_address):
 out.write("\t;........register tdf datapth master.......; \n")
 global offset
 for register in range(0,31):
    out.write("\t;........Register.......; %d\n" % (register))
    if not ((register == int(result_address))):
      result_address = int(result_address)
      out.write("\tsw $%d, %d($%s)\n" % (0, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, 65535))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 65535))
      out.write("\tnor $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, 0))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 0))
      out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      offset += 4
 out.write("\n")

def reg_tdf_hilo_datapath(out, result_address):
  out.write("\t;........register tdf hi_lo datapth .......; \n")
  global offset
  for register in range(0,31):
     out.write("\t;........Register.......; %d\n" % (register))
     if not ((register == int(result_address))):
       result_address = int(result_address)
       out.write("\tsw $%d, %d($%s)\n" % (0, offset, result_address))
       out.write("\tlui $%d, %d\n" % (register, 65535))
       out.write("\tori $%d, $%d, %d\n" % (register, register, 65535))
       out.write("\tmthi $%d\n" % (register))
       out.write("\tmfhi $%d\n" % (register))
       out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
       out.write("\tlui $%d, %d\n" % (register, 0))
       out.write("\tori $%d, $%d, %d\n" % (register, register, 0))
       out.write("\tmthi $%d\n" % (register))
       out.write("\tmfhi $%d\n" % (register))
       out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
       offset += 4
  out.write("\n")


def reg_tdf_EX4(out,result_register,result_address):
 out.write("\t;.............tdf test 2 decoders ...............;\n ")
 global offset
 for register in range(0,31):
    out.write("\t;........Register....... %d;\n" % (register))
    if not ((register == int(result_address)) or (register == int(result_register))):
      out.write("\tlui $%d, %d\n" % (register, 65535))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 65535))
      for j in range(register+1, register+5):
          if (register >=26):
              j -= 5
          out.write("\tlui $%d, %d\n" % (j, 0))
          out.write("\tori $%d, $%d, %d\n" % (j, j, 0))
          out.write("\tnor $%d, $%d, $%d\n" % (result_register, j, register))
          out.write("\tand $%d, $%d, $%d\n" % (result_register, register, j))
          out.write("\tsw $%d, %d($%s)\n" % (result_register, offset, result_address))
          offset += 4
 out.write("\n")

def reg_tdf_EX4b(out,result_register,result_address):
 out.write("\t;.............tdf test 2 decoders ...............;\n ")
 global offset
 for register in range(0,31):
    out.write("\t;........Register....... %d;\n" % (register))
    if not ((register == int(result_address)) or (register == int(result_register))):
      out.write("\tlui $%d, %d\n" % (register, 65535))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 65535))
      for j in range(register+1, register+5):
          if (register >=26):
              j -= 5
          out.write("\tlui $%d, %d\n" % (j, 0))
          out.write("\tori $%d, $%d, %d\n" % (j, j, 0))
          out.write("\tand $%d, $%d, $%d\n" % (result_register, register, j))
          out.write("\tnor $%d, $%d, $%d\n" % (result_register, j, register))
          out.write("\tsw $%d, %d($%s)\n" % (result_register, offset, result_address))
          offset += 4
 out.write("\n")

##################################################################################

def reg_upward_special_mirror(out,data, data2, result_address):
 out.write(";.............general register mirror.............;\n")
 register = 0
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()
 data_f2 = open(data2,'r')
 line2 = data_f2.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 1)):
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))

    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\n")

 for i in (line2):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if  not ((register == 1)):
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

   if not ((register == 1)):
     out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
     out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
     out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
     offset += 4
     out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
     offset += 4
   if (register <= 0):
     register = 31
   else:
     register -= 1
 out.write("\n")

 data_f.close
 data_f2.close

##################################################################################

def hi_lo_upward_special(out,inst,data, data2, result_address):
 register = 0
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if  not ((register == 1)):
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

    if  not ((register == 1)):
      instruction = str.strip(inst)[0:5]
      out.write("\t%s $%d\n" % (inst, register))
      #out.write(" %s $%d, $%d\n" % (instruction, register, register))
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

   if  not ((register == 1)):
     out.write("\t%s $%d\n" % (inst, register))
     #out.write(" %s $%d, $%d\n" % (instruction, register, register))
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

##################################################################################

def reg_test_dat(out, result_address, pattern_address):

  reg_init_upward(out, registerFile_1, 1, pattern_address)
  reg_init_upward(out, registerFile_0, 0, pattern_address)
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

  out.write(";........test general purpose registers........;\n")
  result_address = 1
  res_address = 1
  out.write("\tlui $%d, %d\n" % (result_address, 1))
  out.write("\tori $%d, $%d, %d\n\n" % (result_address, result_address, 2000))

  out.write(";........SAF test for registers..............;\n")
  reg_upward_special(out,registerFile_1, registerFile_0, res_address)
  reg_upward_special_mirror(out,registerFile_0, registerFile_1, res_address)

  out.write(";........tdf test for registers..............;\n")
  reg_tdf_10(out, res_address)   #res_address
  reg_tdf_01(out, res_address)   #res_address

  reg_tdf_load(out, res_address)
  #reg_tdf_EX4(out,1,result_address)
  #reg_tdf_EX4b(out,1,result_address)
  #

  data_list = [[0,0],[1,1],[2,3],[3,2],[4,6],[5,7],[6,5],[7,4],[8,12],
               [9,13],[10,15],[11,14],[12,10],[13,11],[14,9],[15,8],[16,24],
               [17,25],[18,27],[19,26],[20,30],[22,29],[23,28],
               [24,20],[25,21],[26,23],[27,22],[28,18],[29,19],[30,17]]
  #,[31,16],[21,31]
  data_list_down = [[30,17],[29,19],[28,18],[27,22],[26,23],[25,21],[24,20],
                   [23,28],[22,29],[20,30],[19,26],[18,27],[17,25],[16,24],
                    [15,8],[14,9],[13,11],[12,10],[11,14],[10,15],[9,13],[8,12],
                    [7,4],[6,5],[5,7],[4,6],[3,2],[2,3],[1,1],[0,0]]
  #reg_upward_special_basic(out,29, result_address, data_list)
  reg_upward_special_basic_2(out,29, result_address, data_list)
  #reg_upward_special_basic_2(out,29, result_address, data_list_down)


##########################################################################
#                          HILO Register test                            #
##########################################################################
def hi_upward_op(out,data, number, pattern_address, result_address):
 out.write(" hi_upward_"+str(number)+":\n")
 register = 0
 #offset = 0
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 31) or (register == 29)):
      out.write("\tmthi $%d\n" % ( register))
      out.write("\tmfhi $%d\n" % (register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
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
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 31) or (register == 29)):
      out.write("\tmthi $%d\n" % ( register))
      out.write("\tmfhi $%d\n" % (register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      out.write("\tmthi $%d\n" % (register))
      out.write("\tmfhi $%d\n" % (register))
      offset += 4
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
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
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 31) or (register == 29)):
      out.write("\tmtlo $%d\n" % (register))
      out.write("\tmflo $%d\n" % (register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
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
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 31) or (register == 29)):
      out.write("\tmtlo $%d\n" % (register))
      out.write("\tmflo $%d\n" % (register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      out.write("\tmtlo $%d\n" % (register))
      out.write("\tmflo $%d\n" % (register))
      offset += 4
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      offset += 4
    if (register <= 0):
      register = 31
    else:
      register -= 1
 out.write("\tjr $31\n\n")
 data_f.close

 ############################################################################

def hilo(out, result_address, pattern_address):
  out.write("jal reset_offsets\n")
  out.write("jal reset_hi_lo\n")
  out.write("hilo_register_operation:\n")
  out.write("\tjal init_upward_1\n")
  out.write("\tjal hi_upward_0\n")
  out.write("\tjal hi_downward_1\n")
  out.write("\tjal lo_upward_0\n")
  out.write("\tjal lo_downward_1\n")

  out.write("\tjal init_upward_0\n")
  out.write("\tjal hi_upward_1\n")
  out.write("\tjal hi_downward_0\n")
  out.write("\tjal lo_upward_1\n")
  out.write("\tjal lo_downward_0\n")
  out.write("\n")

  reg_tdf_hi_10(out, result_address)
  reg_tdf_hi_01(out, result_address)

  reg_tdf_datapath_master(out, result_address)
  #reg_tdf_hilo_datapath(out, result_address)
  #coreg_tdf(out, result_address)

def coreg_tdf(out, result_address):
 out.write("\t;.............coreg tdf test ...............;\n ")
 global offset
 for register in range(12,15):
    out.write("\t;........Register....... %d;\n" % (register))
    if not ((register == int(result_address))):
      out.write("\tlui $%d, %d\n" % (register, 65535))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 65535))
      out.write("\tmtc0 $%d, $%d\n" % (register, register))
      for j in range(register+1, register+3):
       out.write("\tlui $%d, %d\n" % (j, 0))
       out.write("\tori $%d, $%d, %d\n" % (j, j, 0))
       out.write("\tmfc0 $%d, $%d\n" % (register, register))
       out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
       offset += 4
       out.write("\tmfc0 $%d, $%d\n" % (j, j))
       out.write("\tsw $%d, %d($%s)\n" % (j, offset, result_address))
       offset += 4
 out.write("\n")

def cop_register(out,result_address):
  out.write("jal reset_offsets\n")
  out.write("jal init_cp\n")
  out.write("cop0_register:\n")
  offset = 0
  out.write("\tlui $%d, %d\n" % (1, 65535))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  out.write("\tmtc0 $%d, $%d\n" % (1, 8))
  out.write("\tmtc0 $%d, $%d\n" % (1, 12))
  out.write("\tmtc0 $%d, $%d\n" % (1, 13))
  out.write("\tmtc0 $%d, $%d\n" % (1, 14))
  out.write("\tmtc0 $%d, $%d\n" % (1, 15))

  out.write("\tmfc0 $%d, $%d\n" % (2, 8))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (2, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 8))

  out.write("\tmfc0 $%d, $%d\n" % (2, 12))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (2, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 12))
  out.write("\tmfc0 $%d, $%d\n" % (3, 13))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (3, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 13))
  out.write("\tmfc0 $%d, $%d\n" % (4, 14))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (4, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 14))
  out.write("\tmfc0 $%d, $%d\n" % (5, 15))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (5, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 15))

  out.write("\tmfc0 $%d, $%d\n" % (6, 8))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (6, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 8))
  out.write("\tmfc0 $%d, $%d\n" % (7, 8))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (7, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (6, 12))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (6, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 12))
  out.write("\tmfc0 $%d, $%d\n" % (7, 12))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (7, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (8, 13))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (8, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 13))
  out.write("\tmfc0 $%d, $%d\n" % (9, 13))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (9, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (10, 14))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (10, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 14))
  out.write("\tmfc0 $%d, $%d\n" % (11, 14))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (11, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (16, 15))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (16, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 15))
  out.write("\tmfc0 $%d, $%d\n" % (17, 15))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n\n" % (17, offset, result_address))
  offset +=4

  out.write(";........coprocessor mirror........;\n")
  out.write("\tlui $%d, %d\n" % (1, 65535))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))

  out.write("\tmtc0 $%d, $%d\n" % (0, 8))
  out.write("\tmtc0 $%d, $%d\n" % (0, 12))
  out.write("\tmtc0 $%d, $%d\n" % (0, 13))
  out.write("\tmtc0 $%d, $%d\n" % (0, 14))
  out.write("\tmtc0 $%d, $%d\n" % (0, 15))

  out.write("\tmfc0 $%d, $%d\n" % (2, 8))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (2, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 8))

  out.write("\tmfc0 $%d, $%d\n" % (2, 12))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (2, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 12))
  out.write("\tmfc0 $%d, $%d\n" % (3, 13))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (3, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 13))
  out.write("\tmfc0 $%d, $%d\n" % (4, 14))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (4, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 14))
  out.write("\tmfc0 $%d, $%d\n" % (5, 15))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (5, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 15))

  out.write("\tmfc0 $%d, $%d\n" % (6, 8))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (6, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 8))
  out.write("\tmfc0 $%d, $%d\n" % (7, 8))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (7, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (6, 12))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (6, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 12))
  out.write("\tmfc0 $%d, $%d\n" % (7, 12))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (7, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (8, 13))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (8, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 13))
  out.write("\tmfc0 $%d, $%d\n" % (9, 13))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (9, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (10, 14))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (10, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 14))
  out.write("\tmfc0 $%d, $%d\n" % (11, 14))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (11, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (16, 15))
  out.write("\tsw $%d, %d($%s)\n" % (16, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 15))
  out.write("\tmfc0 $%d, $%d\n" % (17, 15))
  out.write("\tsw $%d, %d($%s)\n\n" % (17, offset, result_address))
