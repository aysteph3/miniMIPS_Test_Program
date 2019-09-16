read_netlist gate_level/pdt2002_fsim.v -format verilog -sensitive -library
read_netlist gate_level/minimips_synth.v -format verilog -sensitive
run_build_model minimips
set_contention nobus
run_drc
#set_patterns -external dumpports_rtl.vcd -sensitive -strobe_period { 200 ns } -strobe_offset { 80 ns }
set_patterns -external dumpports_rtl.vcd -sensitive -strobe_period { 200 ns } -strobe_offset { 101 ns }
run_simulation -sequential
remove_faults -all
#add_faults -all
add_faults -module alu_DW01_add_0
#add_faults -module alu_DW01_add_10
#add_faults -module alu_DW01_add_11
#add_faults -module alu_DW02_mult_1
#add_faults -module alu_DW02_mult_0
#add_faults -module alu
#add_faults -module pps_ex_DW01_add_1
#add_faults -module pps_ex_DW01_add_0
#add_faults -module pps_ex

run_fault_sim -sequential
set_faults -summary verbose -fault_coverage
report_faults -summary
report_faults -level 4 64
quit
