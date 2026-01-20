# Script: main function to download pictures from nmc
# Author: Van
# Version: 20230314
#          20230809, add Internet Log-in part

import os
from time import time
if __name__ == '__main__':
    T1=time()
    
    begintime='202308020800' ################## BJT: YYYYMMDDHHMM ############################
    endtime='202308090800' #################### BJT: YYYYMMDDHHMM ############################
    picpath='./test/' ######## saving path  ############################    

    
    os.system('python AutoDownload_NMC_Pictures.py -o radar -b %s -e %s -p %s'%(begintime, endtime,picpath))
    os.system('python AutoDownload_NMC_Pictures.py -o satellite -b %s -e %s -p %s'%(begintime, endtime, picpath))
    os.system('python AutoDownload_Pictures_Classify.py -o radar -p %s'%picpath)
    os.system('python AutoDownload_Pictures_Classify.py -o satellite -p %s'%picpath)
    T2=time()
    print('Mission success! Elapsed time = %.1f h'%((T2-T1)/3600))

