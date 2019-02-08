# Copyright (C) 2019 Oyeniran Adeboye Stephen
import os

def init(out, number):
  if (number == 0):
    out.write(" lui $%d, %d\n" % (1, 0))
    out.write(" ori $%d, $%d, %d\n" % (1, 1, 0))
    out.write(" lui $%d, %d\n" % (2, 65535))
    out.write(" ori $%d, $%d, %d\n" % (2, 2, 65535))
    out.write(" lui $%d, %d\n" % (3, 65535))
    out.write(" ori $%d, $%d, %d\n" % (3, 3, 65535))
    out.write(" lui $%d, %d\n" % (4, 65535))
    out.write(" ori $%d, $%d, %d\n" % (4, 4, 65535))
  elif(number == 1):
    out.write(" lui $%d, %d\n" % (1, 0))
    out.write(" ori $%d, $%d, %d\n" % (1, 1, 0))
    out.write(" lui $%d, %d\n" % (2, 65535))
    out.write(" ori $%d, $%d, %d\n" % (2, 2, 65535))
    out.write(" lui $%d, %d\n" % (3, 65535))
    out.write(" ori $%d, $%d, %d\n" % (3, 3, 65535))
    out.write(" lui $%d, %d\n" % (4, 65535))
    out.write(" ori $%d, $%d, %d\n" % (4, 4, 65535))
  elif(number == 2):
    out.write(" lui $%d, %d\n" % (1, 0))
    out.write(" ori $%d, $%d, %d\n" % (1, 1, 0))
    out.write(" lui $%d, %d\n" % (2, 65535))
    out.write(" ori $%d, $%d, %d\n" % (2, 2, 65535))
    out.write(" lui $%d, %d\n" % (3, 65535))
    out.write(" ori $%d, $%d, %d\n" % (3, 3, 65535))
    out.write(" lui $%d, %d\n" % (4, 0))
    out.write(" ori $%d, $%d, %d\n" % (4, 4, 0))

def pipeline_test(out, result_address):
 for number in range (3):
  out.write("jal reset_offsets\n")
  out.write("pipeline_operation_"+str(number)+":\n")
  offset = 0
  init(out, number)
  out.write(" %s $%d, $%d, $%d\n" % ('and', 1, 1, 2))
  #out.write(" sw $%d, %d($%s)\n" % (1, offset, result_address))
  out.write(" %s $%d, $%d, $%d\n" % ('or', 3, 1, 3))
  #out.write(" sw $%d, %d($%s)\n" % (3, offset, result_address))
  out.write(" %s $%d, $%d, $%d\n" % ('or', 4, 1, 4))
  out.write(" sw $%d, %d($%s)\n" % (4, offset, result_address))
  out.write(" jal increment_offset\n")
  
  init(out, number)
  out.write(" %s $%d, $%d, $%d\n" % ('or', 1, 1, 2))
  #out.write(" sw $%d, %d($%s)\n" % (1, offset, result_address))
  out.write(" %s $%d, $%d, $%d\n" % ('and', 3, 1, 3))
  #out.write(" sw $%d, %d($%s)\n" % (3, offset, result_address))
  out.write(" %s $%d, $%d, $%d\n" % ('and', 4, 1, 4))
  out.write(" sw $%d, %d($%s)\n" % (4, offset, result_address))
  out.write(" jal increment_offset\n")
  
  init(out, number)
  out.write(" %s $%d, $%d, $%d\n" % ('and', 1, 2, 1))
  out.write(" %s $%d, $%d, $%d\n" % ('or', 3, 3, 1))
  out.write(" %s $%d, $%d, $%d\n" % ('or', 4, 4, 1))
  out.write(" sw $%d, %d($%s)\n" % (4, offset, result_address))
  out.write(" jal increment_offset\n")
  
  init(out, number)
  out.write(" %s $%d, $%d, $%d\n" % ('or', 1, 2, 1))
  out.write(" %s $%d, $%d, $%d\n" % ('and', 3, 3, 1))
  out.write(" %s $%d, $%d, $%d\n" % ('and', 4, 4, 1))
  out.write(" sw $%d, %d($%s)\n" % (4, offset, result_address))
  out.write("\n")