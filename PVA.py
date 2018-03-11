def initialiseCounter(data):
	length =len(data)-1
	newAtom=list(data[length].split())
	counter=int(newAtom[1])
	return counter

def createStartConnectingData(connectionData,startHydrogen,endHydrogen,num):
	finalConnection=[]
	for i in range(0,num):
		connection=connectionData[i].split()
		if str(connection[1])==str(endHydrogen):
			continue
		newConnection=[]
		for j in connection:
			if str(j)!=str(endHydrogen):
				if str(j)=='CONECT':
					newConnection.append(j)
				elif int(j)>endHydrogen	:
					newConnection.append(str(int(j)-1))
				else:
					newConnection.append(j)
		finalConnection.append(newConnection)
	return finalConnection


def createReplicateConnectionData(connectionData,startHydrogen,endHydrogen,num):
	finalConnection=[]
	for i in range(0,num):
		connection=connectionData[i].split()
		if str(connection[1])==str(endHydrogen) or str(connection[1])==str(startHydrogen):
			continue
		newConnection=[]
		for j in connection:
			if str(j)!=str(endHydrogen) and str(j)!=str(startHydrogen):
				if str(j)=='CONECT':
					newConnection.append(j)
				else: 
					if int(j)>startHydrogen:
						j=int(j)-1
					if int(j)>=endHydrogen:
						j=int(j)-1
					newConnection.append(str(j))
		finalConnection.append(newConnection)
	return finalConnection

def creatConeectionDataMiddle(num,replicateConnectingData,i):
	newConnection=[]
	for mlist in replicateConnectingData:
		intermediateConnection=[]
		for j in mlist:
			if j=="CONECT":
				intermediateConnection.append(j)
			else:
				# print j
				intermediateConnection.append(str(int(j)+i))
		newConnection.append(intermediateConnection)
	return newConnection


def createLastMoleculeConnectingData(connectionData,units,endHydrogen,num):
	diff=(num-2)*(units-2)+num-1
	finalConnection=[]
	for i in range(0,num):
		connection=connectionData[i].split()
		if str(connection[1])==str(startHydrogen):
			continue
		newConnection=[]
		for j in connection:
			if str(j)!=str(startHydrogen):
				if str(j)=='CONECT':
					newConnection.append(j)
				elif int(j)>startHydrogen	:
					newConnection.append(str(int(j)-1+diff))
				else:
					newConnection.append(str(int(j)+diff))
		finalConnection.append(newConnection)
	return finalConnection


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


def connectionStringBuilder(mlsit):
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

def createMainAtom(data,counter,num,connectingAtom):
	length=len(data)
	newAtom=list(data[length-num+connectingAtom].split())
	# print newAtom[4]
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
fileData=f.readlines()
startHydrogen=6
endHydrogen=12
num=15
connectingAtom=4

originalData=fileData[1:num+1]
connectionData=fileData[num+1:]
sartMoleculeConnectingData=createStartConnectingData(connectionData,startHydrogen,endHydrogen,num)
replicateConnectingData=createReplicateConnectionData(connectionData,startHydrogen,endHydrogen,num)
# print replicateConnectingData
counter=initialiseCounter(originalData)
units=input("Enter the numbher of repeating units: ")
startMolecule=createStartMolecule(originalData,num,startHydrogen,endHydrogen)
data=list(originalData)
del data[startHydrogen-1]

if startHydrogen <endHydrogen:
	endHydrogen=endHydrogen-1

if startHydrogen<connectingAtom:
	connectingAtom=connectingAtom-1

del data[endHydrogen-1]

if endHydrogen<=connectingAtom:
	connectingAtom=connectingAtom-1
	if units>1:
		sartMoleculeConnectingData[connectingAtom-1].append(str(num))
finalConnectionData=sartMoleculeConnectingData

for i in range(1,units-1):
	newConnectionData=[]
	if i==1:
		newConnectionData=(creatConeectionDataMiddle(num-1,replicateConnectingData,num-1))
	else:
		newConnectionData=(creatConeectionDataMiddle(num-2,replicateConnectingData,(num-2)*i+1))
	counter=createMainAtom(data,counter,num-1,connectingAtom)	
	counter=replicate(data,num-2,counter)
	if i==1:
		j=num-1
	else:
		j=num-2
	newConnectionData[0].append(counter-1+connectingAtom-j)
	newConnectionData[connectingAtom-1].append(counter)
	# print newConnectionData
	finalConnectionData=finalConnectionData + (newConnectionData)

counter=createMainAtom(data,counter,num-1,connectingAtom)	
newConnection=createLastMoleculeConnectingData(connectionData,units,endHydrogen,num)
newConnection[0].append(counter-1+connectingAtom-num+2)
createLastMolecule(data,num-1,counter,originalData,startHydrogen)
finalConnectionData = finalConnectionData + (newConnection)
# print(finalConnectionData)

f.close()
f=open("PVA_new.pdb",'w')
finalMolecule=startMolecule+data[num-2:]
# finalMolecule.append(data)
for atom in finalMolecule:
	atom=str(atom)
	atom=atom.strip('\n')
	f.write("%s\n" % atom)
for mlist in finalConnectionData:
	for j in mlist:
		connection=connectionStringBuilder(j)
		connection=connection.strip('\n')
	f.write("%s\n"%connection)
end="END"
f.write("%s\n"%end)
f.close()
