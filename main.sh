#!/bin/sh
# 20230810
. /etc/profile
. ~/.bash_profile
####################  vars needed to be edited ############################
pypath='/home/bofan/notebook/AutoDownload/' # absolute path, where programs are
picpath='/data/bofan/NMC_Pictures/' # absolute path, where pictures to be saved
env='eden' # your conda environment name
############################################################################
pymain="${pypath}AutoDownload_main_daily_auto_run.py"
sed -i "24c \    pypath= '$pypath'" $pymain
sed -i "25c \    picpath= '$picpath'" $pymain
conda activate $env  
#python -V
python $pymain
conda deactivate


