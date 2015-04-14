import sys

try:
	sys.argv[1]
except:
	print '\n' + 'REMEMBER TO CHOOSE THE FILE TO ANALYSE IN THE TERMINAL!!!' + '\n'

dirty = open(sys.argv[1], "r").readlines()
out=open("CleanHPLC.xls", "w")
samplenum=0


#To obtain the name of all the metabolites in the file
metabolites = [] #create a new list, we will put the metabolites names here
start_reading = False
for line in dirty:
	line = line.rstrip()
	first3 = line[0:3]
	if first3 == "ID#": #This appears every time in the line before the region where we can obtain the concentrations, so it's used as the point to turn the value start_reading True
		start_reading = True 
	elif len(line) == 0: #This detects empty lines and changes the variable start_reading False so you don't check anything from the lines until it becomes True again
		start_reading = False
	elif (start_reading):
		if line.split()[1] not in metabolites: #this is to make a non-redundant and ordered list of metabolites
			metabolites.append(str(line.split()[1]))
#print '\t'.join(metabolites) + '\n'
out.write('Sample name' + '\t' + '\t'.join(metabolites) + '\n') #Write the metabolite names in the right format to have a nice excel sheet. 't'.join(metabolites) makes the elements of the list metabolites appear separated by a tab, you can choose whatever you want instead of tab


start_reading = False
for line in dirty:
	line = line.rstrip()
	first3 = line[0:3]
	first11 = line[0:11]
	if first11 == "Sample Name":
		out.write('\n' + str(line.split()[2]) + '\t') #Writes the name of the sample
	elif first3 == "ID#":
		start_reading = True 
	elif len(line) == 0:
		start_reading = False
	elif (start_reading):
		out.write(str(line.split()[5]) + '\t') #Writes the concentration of the metabolite

# Terminal congratulations
print '\n' 'ANALYSIS COMPLETE! Check CleanHPLC.xls' + '\n'

# Quote submodule
import random
number = random.randrange(1,12+1)
if number == 1:
	quote = 'Data is the new oil! - Clive Humby'
elif number == 2:
	quote = 'Data beats emotions. - Sean Rad'
elif number == 3:
	quote = 'No way I\'m scrolling down 11.000 lines! - Jose Gavalda'
elif number == 4:
	quote = 'Hiding within those mounds of data is knowledge that could change the life of a patient, or change the world. - Atul Butte'
elif number == 5:
	quote = '\"Data! Data! Data\"" he cried impatiently. \"I can\'t make bricks without clay!\" - Sherlock Holmes'
elif number == 6:
	quote = 'I\'ve got 99 problems and HPLC output ain\'t one. - Anonymous-Z'
elif number == 7:
	quote = 'You want weapons? We\'re in a library! Books! The best weapons in the world! - The Doctor'
elif number == 8:
	quote = 'There\'s something that doesn\'t make sense. Let\'s go and poke it with a stick. - The Doctor'
elif number == 9:
	quote = 'You should always waste time when you don\'t have any. Time is not the boss of you. Rule 408 - The Doctor'
elif number == 10:
	quote = 'You can have data without information, but you cannot have information without data. - Daniel Keys Moran'
elif number == 11:
	quote = 'It is a capital mistake to theorize before one has data. - Arthur Conan Doyle'
elif number == 12:
	quote = 'Amy Pond! Get your coat! - The Doctor'
print quote
