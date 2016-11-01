#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re
import os
import sys
reload(sys)  
sys.setdefaultencoding('utf8')

import csv


allletters = sys.argv[1]

file=open(allletters).read()
# splitletters= re.compile("(SWW to )").split(file)
splitletters = re.split('SWW to ', file)
i=1
metadata = [] 
metadatacsv = open('metadata.csv', 'a')
metadatawriter = csv.writer(metadatacsv)
metadata.append(["ID", "Recipient","Date","Location"])

itersplitletters = iter(splitletters)
next(itersplitletters)

for letter in itersplitletters:
	letterfilename =  "letters/" + (os.path.splitext(allletters)[0]) + "_" + str(i).zfill(3) + ".txt"
	print("Now writing Letter #" + str(i) + " to " + letterfilename)
	# Metadata creation

	
	# Grap the receipient of the letter
	firstline = letter.split('\n', 1)[0]
	recipient = firstline.split('：',1)[0].decode().encode('utf-8')
	try:
		date = firstline.split('： ')[1].decode().encode('utf-8')
		try:
			date = date.split('；')[0].decode().encode('utf-8')
		except:
			date = date
	except :
		date = ''
	try: 
		location =  firstline.split('；')[1].decode().encode('utf-8')
	except:
		location = ''
	metadata.append([os.path.splitext(os.path.basename(letterfilename))[0], recipient, date, location])


	# Write the actual file
	target = open(letterfilename, 'w')
	
	target.write(letter)
	target.close()

	
	i=i+1
	
metadatawriter.writerows(metadata)
metadatacsv.close()