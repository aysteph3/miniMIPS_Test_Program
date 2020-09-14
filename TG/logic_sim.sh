#!/bin/sh

./compile_tst.sh || { echo "COMPILE ERROR." ; exit 1; }
# Start the timer
start_time="`date +%s`"
#vsim -batch -do vsim_gui.tcl || { echo "LOGIC SIMULATION ERROR." ; exit 1; }
vsim -do vsim_gui.tcl || { echo "LOGIC SIMULATION ERROR." ; exit 1; }


# Stop the time and calculate time spent
stop_time="`date +%s`"
time_spent=`python3 -c "print ($stop_time - $start_time)"`

echo
echo "--------------------"
echo "All simulations finished!"
echo "Total time spent on simulation: `date -d@$time_spent -u +%H:%M:%S`"
echo
