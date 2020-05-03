import os
import subprocess

killcmd = r"TASKKILL /F /IM python.exe"
os.system(killcmd)
exit()