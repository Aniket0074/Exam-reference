"""
Aim: Data Aquision:
perform data aquation using usb write blocker and ftk imager
objective:
from this experiment we will able to perform data aquation using usb write blocker and ftk imager
steps:
1 press the key+R to open the run box
2 type regedit and press enter
3 navigate to hkey_local_machines\system\current controlset\control
4 right click on the control key in the left pane, select new key
5 name it as storagedevicepolicies.
6 select the storagedevicepolicies key in the left pane then right click 
on any empty space in the right pane and select new- DWORD(32 bit) name it write project
7 double click on writeproduct and then change the value data form 0 to 1
8 now create image of the usb drive using ftk imager
9 select the usb drive folder by browsing and click next and finish
"""