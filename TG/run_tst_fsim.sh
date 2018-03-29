#!/bin/sh

./compile_tst.sh || { echo "COMPILE ERROR." ; exit 1; }

vsim -c -do vsim.tcl || { echo "LOGIC SIMULATION ERROR." ; exit 1; }

#tmax -shell tmax.tcl || { echo "FAULT SIMULATION ERROR." ; exit 1; }
