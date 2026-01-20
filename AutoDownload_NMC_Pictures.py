# Script: download radar and satellite products of CMA
# Author: Van
# Version: 20230314 alpha, revised from download_CMAmosaic.py, created by Huang
#          20230604 beta, add ANEC, ANCN, ANWC

import os
import shutil
import sys
import optparse
from datetime import datetime, timedelta

def get_rad_pic_url(timebegin, timeend, keys={'ACHN','AECN','ACCN','ASCN','ANEC','ANCN','ANWC'}):
    # function explanation: for radar, calculate the possibly existing URLs of picture products, and return them to a <dict> or a <list>
    # timebegin: <datetime>, begin time of download pictures, BJT
    # timeend: <datetime>, end time of download pictures, BJT
    # keys: <dict>, picture product types
    # output: urls: <dict> or <list>, urls of product pictures, named by UCT time and other info

    # http://www.nmc.cn/
    # http://image.nmc.cn/product/2023/03/03/RDCP/SEVP_AOC_RDCP_SLDAS3_EBREF_ACHN_L88_PI_20230303075400000.PNG 
    # or https://pi.weather.com.cn/i/product/pic/l/z_rada_c_babj_20230303080100_p_dor_achn_qref_20230303_075400.png
    # 1 pic every 6 min, 30 days remaining
    
    url_phrase={}
    url_phrase[0]= 'http://image.nmc.cn/product/'
    url_phrase[2] = '/RDCP/SEVP_AOC_RDCP_SLDAS3_ECREF_' # revised in 20230420
    url_phrase[4] = '_L88_PI_'
    url_phrase[6] = '000.PNG' 
    urls = {}

    for key in keys: # loop for product types
        urls[key]=[]
        url_phrase[3]=key
        for ii in range(12000): # loop for timedelta (6 min)
            time = timebegin+timedelta(hours=6.0/60.0*ii)-timedelta(hours=8.0)  # 6 min delta, BJT -> UTC
            if time > timeend-timedelta(hours=8.0):
                break
            url_phrase[1]=time.strftime('%Y/%m/%d')
            url_phrase[5]=time.strftime('%Y%m%d%H%M%S')
            url_temp=url_phrase[0]+url_phrase[1]+url_phrase[2]+url_phrase[3]+url_phrase[4]+url_phrase[5]+url_phrase[6]
            urls[key].append(url_temp)
    return urls

def get_sat_pic_url(timebegin, timeend, keys={'ETCC','EC012','EC001','EC009'}):
    # function explanation: for satellite, calculate the possibly existing URLs of picture products, and return them to a <dict> or a <list>
    # timebegin: <datetime>, begin time of download pictures, BJT
    # timeend: <datetime>, end time of download pictures, BJT
    # keys: <dict>, picture product types
    # output: urls: <dict> or <list>, urls of product pictures, named by UCT time and other info


    # http://www.nmc.cn/
    # http://image.nmc.cn/product/2023/03/14/WXBL/medium/SEVP_NSMC_WXBL_FY4A_ETCC_ACHN_LNO_PY_20230314113800000.JPG #FY4A true color
    # http://image.nmc.cn/product/2023/03/14/WXBL/medium/SEVP_NSMC_WXBL_FY4A_EC012_ACHN_LNO_PY_20230314113800000.JPG #FY4A near infrared
    # http://image.nmc.cn/product/2023/03/14/WXBL/medium/SEVP_NSMC_WXBL_FY4A_EC001_ACHN_LNO_PY_20230314113800000.JPG #FY4A visible
    # http://image.nmc.cn/product/2023/03/14/WXBL/medium/SEVP_NSMC_WXBL_FY4A_EC009_ACHN_LNO_PY_20230314113800000.JPG #FY4A water vapor
    # 1 pic every 4 min, 30 days remaining

    url_phrase={}
    url_phrase[0]= 'http://image.nmc.cn/product/'
    url_phrase[2] = '/WXBL/medium/SEVP_NSMC_WXBL_FY4A_'
    url_phrase[4] = '_ACHN_LNO_PY_'
    url_phrase[6] = '000.JPG' 
    urls = {}

    for key in keys: # loop for product types
        urls[key]=[]
        url_phrase[3]=key
        for ii in range(12000): # loop for timedelta (15 min)
            time = timebegin+timedelta(hours=15.0/60.0*ii)-timedelta(hours=8.0)  # 15 min delta, BJT -> UTC
            if time > timeend-timedelta(hours=8.0):
                break
            url_phrase[1]=time.strftime('%Y/%m/%d')
            url_phrase[5]=time.strftime('%Y%m%d%H%M%S')
            url_temp=url_phrase[0]+url_phrase[1]+url_phrase[2]+url_phrase[3]+url_phrase[4]+url_phrase[5]+url_phrase[6]
            urls[key].append(url_temp)
    return urls

def download(urls, picpath):
    # function explanation: download the picture products on URLs, and move them to a certain path
    # urls: <dict> or <list>, urls of product pictures, named by UCT time and other info
    # picpath: <str>, target saving path, either relative or absolute 
    # output: none
    
    if isinstance(urls, dict): # if <dict>
        for key in urls.keys():
            os.makedirs(os.path.join(picpath, key),exist_ok=True)
            for url in urls[key]:
                #print(url)
                savepath=os.path.join(picpath, key, os.path.basename(url))
                if ~os.path.exists(savepath):
                    #os.system('curl -m 3 --silent '+url) # silence, however still noisy
                    os.system('curl -m 3 -O -L '+url) # visual 
                    if os.path.exists(os.path.basename(url)): # if successfully downloaded, moved
                        shutil.move(os.path.basename(url),savepath)
    # if isinstance(urls, list): # if <list>
    #     for url in urls:
    #         print(url)
    #         os.system('curl -m 3 -O '+url)
    #         os.rename('./'+url.split('/')[-1],os.path.join(picpath, url.split('/')[-1]))



if __name__ == '__main__':

    # command line options
    p = optparse.OptionParser(usage="usage: %prog [options]", version="%prog 1.0")
    p.add_option('--begintime', '-b', help='the begin of the time, YYYYMMDDHHMM in BJT')
    p.add_option('--endtime', '-e', help='the end of the time, YYYYMMDDHHMM in BJT')
    p.add_option('--savepath', '-p', help='the saving path of pictures')
    p.add_option('--option','-o', help='radar or satellite')
    options, arguments = p.parse_args()

    # specify beginning of the date
    if not options.begintime:
        print ('The beginning of the date must be specified')
        sys.exit()
    begindate = options.begintime

    # specify end of the date
    if not options.endtime:
        print ('The end of the date must be specified')
        sys.exit()
    enddate = options.endtime

    time_format = '%Y%m%d%H%M'
    timebegin = datetime.strptime(begindate, time_format)
    timeend = datetime.strptime(enddate, time_format)

    # specify saving path 
    if not options.savepath:
        picpath = './'
    else:
        picpath = os.path.abspath(options.savepath)

    # specify option
    if not options.option:
        print ('The option(radar or satellite) must be specified')
        sys.exit()
    else:
        if options.option=='radar':
            folder='radar' # set sub folder name of radar pictures
            urls = get_rad_pic_url(timebegin, timeend)  # <dict>
        elif options.option=='satellite':
            folder='satellite' # set sub folder name of satellite pictures
            urls = get_sat_pic_url(timebegin, timeend)  # <dict>
        else:
            print ('The option must be \'radar\' or \'satellite\'')
            sys.exit()

    os.makedirs(os.path.join(picpath, folder),exist_ok=True)
    download(urls, os.path.join(picpath, folder))
