#!/usr/bin/env python3

import os
import shutil
from pathlib import PosixPath
directory = os.getcwd()
print(directory)
#directory = r'/project/detre/debarun/disconnecttome'

for WMH in os.listdir(directory):
	if WMH.endswith(".nii.gz"):
		f1 = os.path.join(directory,WMH)
		base_f1=os.path.basename(f1)
		o_WMH = os.path.splitext(base_f1)[0]
		for FIB in os.listdir(directory):
			if FIB.endswith(".src.gz.gqi.1.7.fib.gz"):
				f2 = os.path.join(directory,FIB)
				base_f2 = os.path.basename(f2)
				o_FIB = os.path.splitext(base_f2)[0]
				o = ""+o_FIB+".Cingulum_Frontal_Parahippocampal_L_"+o_WMH+".tt.gz"
				output = os.path.join(directory,o)
				cmd = "dsi_studio --action=trk --track_id=Cingulum_Frontal_Parahippocampal_L --source="+f2+" --seed_count=100000 --tip_iteration=0 --roa="+f1+" --output="+output+" --export=stat"
				os.system(cmd)
