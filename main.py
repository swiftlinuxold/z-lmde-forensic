#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/home/mint')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'
	dir_user = '/home/mint'
else:
	dir_develop='/home/' + uname + '/develop'
	dir_user = '/home/' + uname

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================


# THIS IS THE SCRIPT FOR ADDING FORENSIC PACKAGES.

print '=============================='
print 'BEGIN ADDING FORENSIC PACKAGES'

def package_add (name):
    os.system ('echo ADDING ' + name)
    os.system ('apt-get install -y ' + name)

# Carried over from antiX Linux
package_add ('partimage testdisk')

# Rescue (Search Synaptic for "rescue")
package_add ('scrounge-ntfs dares ddrescue gddrescue magicrescue myrescue')

# Recover (Search Synaptic for "recover")
package_add ('chntpw')
package_add ('e2undel ext3grep ')
package_add ('foremost ngorca ophcrack ophcrack-cli')
package_add ('recover safecopy recoverjpeg vdmfec')
package_add ('extundelete gzrt nasty par2 pdfcrack')
package_add ('recoverdm rephrase scalpel')
package_add ('dcfldd unhide dc3dd')
package_add ('rdd rifiuti2')







print 'FINISHED ADDING FORENSIC PACKAGES'
print '================================='
