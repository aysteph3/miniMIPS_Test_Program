set start [clock clicks]
# run the simulation
vsim -vopt -coverage -simstats -voptargs="+acc" minimips_rtl.sim_minimips(bench)
#vsim -vopt -debugDB -coverage -voptargs="+acc" minimips_rtl.sim_minimips(bench)
#vsim -vopt -coverage -suppress -voptargs="+acc" minimips_rtl.sim_minimips(bench)

#set StdArithNoWarnings 1
#set NumericStdNoWarnings 1

# show waveforms
source wave.do

# START VCD file generation

#vcd dumpports /sim_minimips/u_minimips/* -file dumpports_rtl.vcd
vcd dumpports sim/:sim_minimips:u_minimips:* -file dumpports_rtl.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u1_pf:* -file dumpports_pf.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u2_ei:* -file dumpports_ei.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u3_di:* -file dumpports_di.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u4_ex:* -file dumpports_ex.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u5_mem:* -file dumpports_mem.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u6_renvoi:* -file dumpports_renvoi.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u7_banc:* -file dumpports_banc.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u8_syscop:* -file dumpports_syscop.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u9_bus_ctrl:* -file dumpports_bus_ctrl.vcd
vcd dumpports sim/:sim_minimips:u_minimips:u10_predict:* -file dumpports_predict.vcd

# create an event to stop the simulation
when -label end_of_simulation {end_sim == '1'} {
	echo "End of simulation"
	set finish [clock clicks]
	puts [expr {($finish - $start)/200}]
	vcd dumpportsflush
	quit -f
	#stop
}

# run the simulation
run 800 ms
#quit -f
