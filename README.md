# radar_mosaic
Python and shell scripts to autoly download radar mosaic from chinese national meteorology center   (https://www.nmc.cn/publish/radar/chinaall.html)  

Author: bo_fan@qq.com  
20230315 for version 1.0  
20230810 for version 1.1  


Core scripts include:  
main.sh  
AutoDownload_main.py  
AutoDownload_main_daily_auto_run.py  
AutoDownload_NMC_Pictures.py  
AutoDownload_Pictures_Classify.py  
  
Usage:  
1. Run automatically (recommended)   
Edit 'picpath' for saving pictures:  
$ vim AutoDownload_main_daily_auto_run.py  
Using crontab command:  
$ crontab -e  
In vim, insert following words and wq:  
0 12 * * * AutoDownload_main_daily_auto_run.sh  
This means every 12:00 BJT, yesterday's pictures from 00:00 to 24:00 UTC are to be downloaded.  
  
1. Run manually   
$ vim AutoDownload_main.py  
Edit 'begintime', 'endtime', 'picpath' and finally:  
$ python AutoDownload_main.py  
  
Update logs:  
20230810, add Internet Log-in command in school web  

