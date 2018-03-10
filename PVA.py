def initialiseCounter(data):
	length =len(data)-1
	newAtom=list(data[length].split())
	counter=int(newAtom[1])
	return counter

def createStartMolecule(data,num,startHydrogen,endHydrogen):
	startMolecule=[]
	count=1
	for i in range(0,num):
		if i!=endHydrogen-1:
			newAtom=list(data[i].split())
			newAtom[1]=count
			newAtom[4]=float(newAtom[4])
			newAtom[5]=float(newAtom[5])
			newAtom[6]=float(newAtom[6])
			finString=buildString(newAtom)
			startMolecule.append(finString)
			count=count+1
	return startMolecule


def buildString(newAtom):
	if float(newAtom[4]) <10.0:
		newAtom[4]=format(newAtom[4],'0.3f')
	elif float(newAtom[4]) >=10.0:
		newAtom[4]=format(newAtom[4],'0.2f')

	if float(newAtom[5]) <10.0:
		newAtom[5]=format(newAtom[5],'0.3f')
	elif float(newAtom[5]) >=10.0:
		newAtom[5]=format(newAtom[5],'0.2f')

	if float(newAtom[6]) <10.0:
		newAtom[6]=format(newAtom[6],'0.3f')
	elif float(newAtom[6]) >=10.0:
		newAtom[6]=format(newAtom[6],'0.2f')

	flag=float(newAtom[1])
	spaces=""
	if flag<10:
		spaces="    "
	elif flag>=10:
		spaces="   "
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

def createMainAtom(data,counter,num,connectingAtom):
	length=len(data)
	newAtom=list(data[length-num+connectingAtom].split())
	print newAtom[4]
	newAtom[1]=counter
	sourceAtom=data[0].split()
	mainAtom=data[1].split()
	newAtom[4]=float(newAtom[4])-float(sourceAtom[4])+float(mainAtom[4])
	newAtom[5]=float(newAtom[5])-float(sourceAtom[5])+float(mainAtom[5])
	newAtom[6]=float(newAtom[6])-float(sourceAtom[6])+float(mainAtom[6])
	finString=buildString(newAtom)
	data.append(finString)
	counter=counter+1
	return counter

def  replicate(data,num,counter):
	length=len(data)-1
	sourceAtom=data[length-num].split()
	mainAtom=data[length].split()
	start=length-num+1
	for i in range(1,num):
		newAtom=list(data[start].split())
		newAtom[1]=counter
		newAtom[4]=float(newAtom[4])-float(sourceAtom[4])+float(mainAtom[4])
		newAtom[5]=float(newAtom[5])-float(sourceAtom[5])+float(mainAtom[5])
		newAtom[6]=float(newAtom[6])-float(sourceAtom[6])+float(mainAtom[6])
		finString=buildString(newAtom)
		data.append(finString)
		start=start+1
		counter=counter+1
	return counter

	# print sourceAtom

def  createLastMolecule(data,num,counter,originalMolecule,startHydrogen):
	length=len(data)-1
	sourceAtom=data[0].split()
	mainAtom=data[length].split()
	start=1
	del originalMolecule[startHydrogen-1]
	for i in range(1,num):
		newAtom=list(originalMolecule[start].split())
		newAtom[1]=counter
		newAtom[4]=float(newAtom[4])-float(sourceAtom[4])+float(mainAtom[4])
		newAtom[5]=float(newAtom[5])-float(sourceAtom[5])+float(mainAtom[5])
		newAtom[6]=float(newAtom[6])-float(sourceAtom[6])+float(mainAtom[6])
		finString=buildString(newAtom)
		data.append(finString)
		start=start+1
		counter=counter+1




f= open("./PVA.pdb","r")
originalData=f.readlines()
counter=initialiseCounter(originalData)
print counter
units=input("Enter the numbher of repeating units: ")
startHydrogen=6
endHydrogen=12
num=15
connectingAtom=4
startMolecule=createStartMolecule(originalData,num,startHydrogen,endHydrogen)
data=list(originalData)
del data[startHydrogen-1]

if startHydrogen <endHydrogen:
	endHydrogen=endHydrogen-1

if startHydrogen<connectingAtom:
	connectingAtom=connectingAtom-1

del data[endHydrogen-1]

if endHydrogen<connectingAtom:
	connectingAtom=connectingAtom-1

for i in range(1,units-1):
	counter=createMainAtom(data,counter,num-1,connectingAtom)	
	counter=replicate(data,num-2,counter)

counter=createMainAtom(data,counter,num-1,connectingAtom)	
createLastMolecule(data,num-1,counter,originalData,startHydrogen)
f.close()
f=open("PVA_new.pdb",'w')
finalMolecule=startMolecule+data[num-2:]
# finalMolecule.append(data)
for atom in finalMolecule:
	atom=str(atom)
	atom=atom.strip('\n')
	f.write("%s\n" % atom)
f.close()
