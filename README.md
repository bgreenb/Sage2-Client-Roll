# Sage2-Client-Roll
Display Client Roll for Sage2 

##Description  

This roll will install ffmpeg and the Google Chrome browser on display tile nodes. [Sage2](http://sage2.sagecommons.org/) recommends Google Chrome over firefox for display clients. Instead of directly building google chrome from source, this roll uses the script from [Richard Lloyd](http://chrome.richardlloyd.org.uk/) to install the latest version to install chrome isntead. 

##Building and Installing

In the main folder of the roll:

Build the roll using: 
		
	# make roll 2>&1 | tee make.log 
  	
If successful, this will build a .iso file called ''Sage2Client-*.disk1.iso''. 

**Installation**
	
To install on a node, execute: 
	
	# rocks add roll *.iso
	# rocks enable roll Sage2Client
	# (cd /export/rocks/install; rocks create distro)
	# rocks run roll Sage2Client | bash
