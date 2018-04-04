def initialiseCounter(data):
	length =len(data)-1
	newAtom=list(data[length].split())
	counter=int(newAtom[1])
	return counter

def connectionStringBuilder(mlist):
	connection=""
	for j in mlist:
		connection=connection+str(j)
		connection=connection+"    "
	return connection

def buildString(newAtom):
	if float(newAtom[4]) <10.0:
		newAtom[4]=format(newAtom[4],'0.3f')
	elif float(newAtom[4]) <100.0:
		newAtom[4]=format(newAtom[4],'0.2f')
	elif float(newAtom[4]) >=100.0:
		newAtom[4]=format(newAtom[4],'0.1f')

	if float(newAtom[5]) <10.0:
		newAtom[5]=format(newAtom[5],'0.3f')
	elif float(newAtom[5]) <100.0:
		newAtom[5]=format(newAtom[5],'0.2f')
	elif float(newAtom[5]) >=100.0:
		newAtom[5]=format(newAtom[5],'0.1f')



	if float(newAtom[6]) <10.0:
		newAtom[6]=format(newAtom[6],'0.3f')
	elif float(newAtom[6]) <100.0:
		newAtom[6]=format(newAtom[6],'0.2f')
	elif float(newAtom[6]) >=100.0:
		newAtom[6]=format(newAtom[6],'0.1f')


	flag=float(newAtom[1])
	spaces=""
	if flag<10:
		spaces="    "
	elif flag<100:
		spaces="   "
	elif flag<1000:
		spaces="  "
	else:
		spaces=" "
	
	spaceX="      "
	if float(newAtom[4])>=0:
		spaceX="       "
	spaceY="  "
	if float(newAtom[5])>=0:
		spaceY="   "
	spaceZ="  "
	if float(newAtom[6])>=0:
		spaceZ="   "
		
	finString=str(newAtom[0])+spaces+str(newAtom[1])+ "  " +str(newAtom[2]) +"           "+str(newAtom[3])+spaceX+str(newAtom[4])+spaceY+str(newAtom[5])+spaceZ+str(newAtom[6])+"                       "+str(newAtom[7])	
	# print finString
	return finString