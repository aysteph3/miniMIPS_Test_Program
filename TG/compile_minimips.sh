#!/bin/sh


## Create & Map Libraries
v.7

## Compile modules
vcom -work minimips_rtl src/pack_mips.vhd
vcom -work minimips_rtl src/my_package.vhd
vcom -work minimips_rtl src/alu.vhd
vcom -work minimips_rtl src/bus_ctrl.vhd
vcom -work minimips_rtl src/pps_di.vhd
vcom -work minimips_rtl src/pps_ex.vhd
vcom -work minimips_rtl src/pps_pf.vhd
vcom -work minimips_rtl src/renvoi.vhd
vcom -work minimips_rtl src/banc.vhd
vcom -work minimips_rtl src/pps_ei.vhd
vcom -work minimips_rtl src/pps_mem.vhd
vcom -work minimips_rtl src/predict.vhd
vcom -work minimips_rtl src/syscop.vhd
vcom -work minimips_rtl src/minimips.vhd
vcom -work minimips_rtl src/ram.vhd
vcom -work minimips_rtl src/rom.vhd
vcom -work minimips_rtl src/bench_minimips.vhd
