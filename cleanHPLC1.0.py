import sys

dirty = open(sys.argv[1], "r").readlines()

out=open("CleanHPLC.xls", "w")
out.write("Sample 	Ethanol 	Glucose\n")
samplenum=0

for i,line in enumerate(dirty): #Goes through every line, counts it (changes value of i for every line in dirty)
	line = line.rstrip()
	first30 = line[0:30]
	if first30 == "[Compound Results(Detector B)]": #Glucose and Ethanol were in detector B so I used it as a refference line to detect the concentrations
		samplenum = samplenum + 1

		#This this part writtes on the file you have created before in a way that each element is in a clolumn and it starts a new line for each sample
		out.write(str(samplenum) + "\t" )
		out.write(str(dirty[i+3].split()[5]) + "\t") 
		out.write(str(dirty[i+4].split()[5]) + "\n")
		#.split() makes a list out of the words in the line. Then I can select the position in that list, in this case [5], where the concentration is indicated
		#dirty[i+number], since i has a value, if the condition first30 == "[Compound Results(Detector B)]" is true, then he advances that number of lines 
			
		#  This bit prints the result in the screen, comment it if you don't want it to happen
		print "Sample " + str(samplenum)
		print "Ethanol concentration = " + dirty[i+3].split()[5]
		print "Glucose concentration = " + str(dirty[i+4].split()[5])
