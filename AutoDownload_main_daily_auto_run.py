# Script: main function to download pictures from nmc
#         auto run version
# Author: Van
# Version: 20230316
#          20230809, add Internet Log-in function

import os
import sys
from datetime import datetime, timedelta
from time import time
if __name__ == '__main__':
    T1=time()
    ####################################################### auto time obtain ##################################################
    nowtime=datetime.now()
    begintime=nowtime.replace(hour=8,minute=0,second=0)-timedelta(hours=24.0)
    endtime=begintime+timedelta(hours=23.0,minutes=59.0)
    if endtime>nowtime:
        print('Current time must be later than 8:00 BJT!')
        sys.exit()
    #print(begintime.strftime('%Y%m%d-%H:%M'))
    begintime=begintime.strftime('%Y%m%d%H%M')
    endtime=endtime.strftime('%Y%m%d%H%M')
    ###########################################################################################################################
    pypath= '/home/fan/notebook/AutoDownload/'
    picpath= '/data/fan/NMC_Pictures/'
   
    os.system('python %sAutoDownload_NMC_Pictures.py -o radar -b %s -e %s -p %s'%(pypath,begintime,endtime,picpath))
    os.system('python %sAutoDownload_NMC_Pictures.py -o satellite -b %s -e %s -p %s'%(pypath,begintime,endtime,picpath))
    os.system('python %sAutoDownload_Pictures_Classify.py -o radar -p %s'%(pypath,picpath))
    os.system('python %sAutoDownload_Pictures_Classify.py -o satellite -p %s'%(pypath,picpath))
    T2=time()
    print('Mission success! Elapsed time = %.1f h'%((T2-T1)/3600))
