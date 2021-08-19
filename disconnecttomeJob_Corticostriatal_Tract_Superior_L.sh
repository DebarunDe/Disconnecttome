#!/bin/bash
#BSUB -J disconnecttomeJob
#BSUB -o disconnecttomeJob.%J.out
#BSUB -e disconnecttomeJob.%J.error

module unload gcc
module load gcc/10.2.0
module load dsi-studio/2021-08
module load python/3.6.1
echo "modules loaded, beginning script."
echo "___________________________________________________________________________"
echo " "
python3 /project/detre/debarun/disconnecttome/run_Corticostriatal_Tract_Superior_L.py
echo "___________________________________________________________________________"
echo " "
echo "done!"
