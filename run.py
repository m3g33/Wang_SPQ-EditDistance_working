#!/usr/bin/python
from __future__ import print_function
import sys, subprocess, os

delim = ";" if os.name == "nt" else ":"

party = {'gen': "java -cp FlexSC/lib/*" + delim + "bin/ util.GenRunnable",
         'eva': "java -cp FlexSC/lib/*" + delim + "bin/ util.EvaRunnable"}
program = {'ptcl1': "Protocol1 ",
           'ptcl2': "Protocol2 "}

cmd = party[sys.argv[1]]+" online."+program[sys.argv[2]]+" ".join(sys.argv[3:])
print("Command to run:", cmd)

subprocess.call(cmd, shell=True)
