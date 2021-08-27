'''
	You will more than likely need to run the script with administrator privileges
		to avoid anauthorized actions

	Requirements:
		- Python 3.x version installed
		- Latest pip version for the specified python version installed
'''

import os
import subprocess


# generate package list
#ret = os.system( 'pip3 list > packages.txt' )
#if ( ret != 0 ):
#	print( "Command failed with exit code " + ret )
#	exit( -1 )

# print package list
with open( 'packages.txt', 'r' ) as f:
	lines = f.readlines()
	for line in lines:
		print( line, end='' )

# install packages
results = []
if ( os.path.exists( "packages.txt" ) ):
	with open( "packages.txt", 'r' ) as f:
		lines = f.readlines()
		i = 0
		for line in lines:
			i += 1
			if i > 2:
				module = line.split()[0]
				#print( module )
				try:
					result = subprocess.check_output( "python -m pip install " + module )
					print( result )
					results.append( result )
				except Exception as e:
					print( e )

# write output from each command to a file
with open( 'results.txt', 'w' ) as f:
	for line in results:
		f.write( "{}\n".format( line ) )
