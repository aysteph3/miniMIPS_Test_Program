# Copyright (C) 2018 Oyeniran Adeboye Stephen, Olusiji
def reset_function(file):
    file.write(" ;CODE MEMORY: (0x00000000-0x0000FFFF) \n")
    file.write(" ;DATA MEMORY: (0x00010000-0x0001FFFF) \n\n")
    file.write(" org 0000 \n\n")
    file.write(" _reset: \n\n")
    for x in range(32):
        file.write("\txor $%d, $%d, $%d\n" % (x, x, x))
    file.write("\n")

def reset_offsets(file, pattern_address, iterator, result_register):
    file.write("reset_offsets:\n")
    file.write("\tlui $%s, %d\n" % (pattern_address, 1))
    file.write("\tori $%s, $%s, %d\n" % (pattern_address, pattern_address, 8))
    file.write("\txor $%s, $%s, $%s\n" % (iterator, iterator, iterator))
    file.write("\txor $%s, $%s, $%s\n" % (result_register, result_register, result_register))
    file.write("\tjr $31\n\n")

def load_pattern(file, pattern_address):
    file.write("load_patterns:\n")
    file.write("\tlw $%d, %d($%s)\n" % (2, 0, pattern_address))
    file.write("\tlw $%d, %d($%s)\n" % (3, 4, pattern_address))
    file.write("\tjr $31\n\n")

def increment_offset(file, pattern_address, iterator, result_address):
    file.write("increment_offset:\n")
    file.write("\taddi $%s, $%s, %d\n" % (pattern_address, pattern_address, 8))
    file.write("\taddi $%s, $%s, %d\n" % (iterator, iterator, 2))
    file.write("\taddi $%s, $%s, %d\n" % (result_address, result_address, 4))
    file.write("\tjr $31\n\n")

def reset_hi_lo(file):
    file.write("reset_hi_lo:\n")
    file.write("\tlui $%d, %d\n" % (1, 0))
    file.write("\tori $%d, $%d, %d\n" % (1, 1, 0))
    file.write("\tmthi $%d\n" % (1))
    file.write("\tmtlo $%d\n" % (1))
    file.write("\tjr $31\n\n")
