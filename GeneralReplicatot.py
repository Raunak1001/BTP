import StringBuilder
import ConnectingData
import AtomCreate

fileName=str(raw_input("Enter File Name: "))
f= open("./"+fileName+".pdb","r")
fileData=f.readlines()
startHydrogen=input("Enter Starting Hydrogen: ")
endHydrogen=input("Enter End Hydrogen: ")
num=input("Total Atoms: ")
connectingAtom=input("Connecting Atom Number: ")

originalData=fileData[1:num+1]
connectionData=fileData[num+1:]
sartMoleculeConnectingData=ConnectingData.createStartConnectingData(connectionData,startHydrogen,endHydrogen,num)

if endHydrogen<connectingAtom:
	sartMoleculeConnectingData[connectingAtom-2].append(num)
else:
	sartMoleculeConnectingData[connectingAtom-1].append(num)	

replicateConnectingData=ConnectingData.createReplicateConnectionData(connectionData,startHydrogen,endHydrogen,num)
counter=StringBuilder.initialiseCounter(originalData)
units=input("Enter the numbher of repeating units: ")
startMolecule=AtomCreate.createStartMolecule(originalData,num,startHydrogen,endHydrogen)
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
		newConnectionData=(ConnectingData.creatConeectionDataMiddle(num-1,replicateConnectingData,num-1))
	else:
		newConnectionData=(ConnectingData.creatConeectionDataMiddle(num-2,replicateConnectingData,(num-2)*i+1))
	counter=AtomCreate.createMainAtom(data,counter,num-1,connectingAtom)	
	counter=AtomCreate.replicate(data,num-2,counter)
	if i==1:
		j=num-1
		if startHydrogen<=connectingAtom:
			j=j-1
	else:
		j=num-2

	newConnectionData[0].append(connectingAtom+counter-num+1-j)
	newConnectionData[connectingAtom-1].append(counter)
	finalConnectionData=finalConnectionData + (newConnectionData)

counter=AtomCreate.createMainAtom(data,counter,num-1,connectingAtom)	
newConnection=ConnectingData.createLastMoleculeConnectingData(connectionData,units,endHydrogen,num,startHydrogen)
if units==2:
	newConnection[0].append(counter-1+connectingAtom-num)
else:
	newConnection[0].append(counter-1+connectingAtom-num+1)	
AtomCreate.createLastMolecule(data,num-1,counter,originalData,startHydrogen)
finalConnectionData = finalConnectionData + (newConnection)

f.close()
f=open(fileName+"_"+str(units)+".pdb",'w')
finalMolecule=startMolecule+data[num-2:]
# finalMolecule.append(data)
f.write("Remark..\n")
for atom in finalMolecule:
	atom=str(atom)
	atom=atom.strip('\n')
	f.write("%s\n" % atom)
for mlist in finalConnectionData:
	connection=StringBuilder.connectionStringBuilder(mlist)
	connection=connection.strip('\n')
	f.write("%s\n"%connection)
end="END"
f.write("%s\n"%end)
f.close()
