# Copyright (C) 2018 Adeboye Stephen Oyeniran

#inputFile = "input/data.txt"
#outputFile ="testfiles/output1.txt"
def load_data(transition_address, result_register, src3, out):
    out.write("\tlui $%s, %d\n" % (transition_address, 65533))
    out.write("\tori $%s, $%s, %d\n" % (transition_address, transition_address, 65533))
    out.write("\tlui $%s, %d\n" % (src3, 0))
    out.write("\tori $%s, $%s, %d\n" % (src3, src3, 0))
    out.write("\t%s $%s, $%s, $%s\n" % ('or', result_register, transition_address, transition_address))


def transition_template(out, instruct, result_register, transition_address, src3):
  #f = open(inputFile,'r')         #input file
  #out = open(outputFile, 'w')     #output file

  #instruction = 'mtlo'
  instruction = instruct

  out.write("jal reset_offsets\n")
  if(instruction[0:2] =="mf" or instruction[0:2] =="mt"):
      out.write("jal reset_hi_lo\n")
  if(instruction[0:] =="add" or instruction[0:] =="sub"):
      out.write("jal init_cp\n")
  #out.write("operation_"+instruction+":\n")
  out.write("operation_"+instruction+"_trans:\n")
  offset = 0
  register = 2
  outline = []

  #line=f.readlines()


  def alu_shifts(offset, opcode):
      #for i in (line):
          #load_data_shift(i, register, opcode)
          out.write("\tsw $%s, %d($29)\n" % (result_register, offset))
          out.write("\tjal increment\n")

  def alu_immediate(offset, opcode):
      #for i in (line):
          #load_data_immediate(i, register, opcode)
          out.write("\tsw $%s, %d($29)\n" % (result_register, offset))
          out.write("\tjal increment\n")

  def alu_op(offset, src3, transition_address):
          load_data(transition_address,register,src3,out)
          out.write("\t%s $%s, $%s, $%s\n" % (instruction, result_register, src3, src3))
          out.write("\tsw $%s, %d($29)\n" % (result_register, offset))
          out.write("\tjal increment\n")

  def mult_op(offset, src3, transition_address):
          load_data(transition_address,register, src3,out)
          out.write("\t%s $%s, $%s\n" % (instruction, src3, src3))
          out.write("\tmflo $%s\n" % (result_register))
          out.write("\tsw $%s, %d($29)\n" % (result_register, offset))
          out.write("\tmfhi $%s\n" % (result_register))
          out.write("\tsw $%s, %d($29)\n" % (result_register, offset))
          out.write("\tjal increment\n")

  def hi_lo(src3, transition_address,opcode):
      #for i in (line):
          load_data(transition_address,register,src3,out)
          if(opcode[2:4]=="hi"):
              out.write("\tmfhi $%d\n" % (register+2))
          else:
              out.write("\tmflo $%d\n" % (register+2))
          out.write("\tsw $%d, %d($29)\n" % (register+2, offset))
          out.write("\tjal increment\n")

  if ((instruction =="mult") or (instruction =="multu")):
      mult_op(offset,src3,transition_address)
  elif((instruction =="addiu") or (instruction =="andi")or (instruction =="ori")or (instruction =="xori") or (instruction =="sltiu")or (instruction =="slti")):
      alu_immediate(offset, instruction)
  elif((instruction =="sll") or (instruction =="sra") or (instruction =="srl") or (instruction =="lui")):
      alu_shifts(offset,instruction)
  elif((instruction == "mtlo") or (instruction =="mthi")):
      hi_lo(src3,transition_address,instruction)
  else:
      alu_op(offset,src3,transition_address)

  #out.close()
  #f.close()
def make_transition10_template(para, outputFile, result_register, transition_address, src3):
  Ins = open(para,'r')
  data_lines = []
  firstPass = True

  for line in Ins:
    if "=" not in line:
      try:
        catergory = line[0:2]
        line = line.rstrip()
        instru = line[2:]
        instr = str.strip(instru)
        instruction = instr[0:]
        if (catergory == 'p_'):
          if (instruction == 'addu' or instruction == 'add'):
            #inputFile = '../input/pseudo_input/add.txt'
            transition_template(outputFile, instruction, result_register,transition_address,src3)
            outputFile.write("\n")
          elif(instruction == 'subu'or instruction == 'sub'):
            #inputFile = '../input/pseudo_input/sub.txt'
            transition_template(outputFile, instruction, result_register,transition_address,src3)
            outputFile.write("\n")
          elif(instruction == 'or' or instruction == 'xor' or instruction == 'nor' or instruction == 'and'):
            #inputFile = '../input/pseudo_input/logic.txt'
            transition_template(outputFile, instruction, result_register,transition_address,src3)
            outputFile.write("\n")
          elif(instruction == 'sll' or instruction == 'srl' or instruction == 'sra' or instruction == 'sllv' or instruction == 'srlv' or instruction == 'srav' or instruction == 'slt' or instruction == 'sltu' or instruction == 'lui'):
            #inputFile = '../input/pseudo_input/shift.txt'
            transition_template(outputFile, instruction, result_register, transition_address,src3)
            outputFile.write("\n")
          elif(instruction == 'mult' or instruction == 'multu'):
            #inputFile = '../input/pseudo_input/mult.txt'
            transition_template(outputFile, instruction, result_register, transition_address,src3)
            outputFile.write("\n")
      except IndexError:
        firstPass = False

    else:
      do='nothing'

  Ins.close()
