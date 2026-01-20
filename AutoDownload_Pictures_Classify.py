# sort downloaded pictures(PNG/JPG) by date
# Van
# 20230306
# v2 add optparse option in 20230314

import os
import shutil
import sys
from glob import glob
import optparse

def classify(picpath):
    # function explanation: catagory pictures by date
    # picpath: <str>, target saving path, either relative or absolute 
    # folder: <str>, 'nmc_satellite' or 'nmc_radar_mosaic' 
    # output: none

    # list downloaded PNGs/JPGs catagoried by keys
    filelist=glob(os.path.join(picpath,'*','*.PNG'),recursive=True)
    filelist.extend(glob(os.path.join(picpath,'*','*.JPG'),recursive=True))

    # move pictures into a new path named by date
    for file in filelist:
        filename=os.path.basename(file);date=filename.split('_')[-1][0:8] # YYYYMMDD
        datepath=os.path.join(picpath,date,file.split('/')[-2]) # picpath/date/key/
        os.makedirs(datepath,exist_ok=True)
        try:
            shutil.move(file,os.path.join(datepath,filename))
        except Exception as e:
            print(e)
            # os.remove(file)

if __name__ == '__main__':

    # command line options
    p = optparse.OptionParser(usage="usage: %prog [options]", version="%prog 1.0")
    p.add_option('--savepath', '-p', help='the saving path of pictures')
    p.add_option('--option','-o', help='radar or satellite')
    options, arguments = p.parse_args()

    # specify option
    if not options.option:
        print ('The option(radar or satellite) must be specified')
        sys.exit()
    else:
        if options.option=='radar':
            folder='radar' # set sub folder name of radar pictures
        elif options.option=='satellite':
            folder='satellite' # set sub folder name of satellite pictures
        else:
            print ('The option must be \'radar\' or \'satellite\'')
            sys.exit()

    # specify saving path 
    if not options.savepath:
        print ('The savepath must be specified')
        sys.exit()
    else:
        picpath = os.path.join(os.path.abspath(options.savepath),folder)
    
    classify(picpath)
            

