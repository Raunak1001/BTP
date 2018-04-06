import StringBuilder

fileName1=str(raw_input("Enter First File Name: "))
fileName2=str(raw_input("Enter Second File Name: "))

f1= open("./"+fileName1+".pdb","r")
f2= open("./"+fileName2+".pdb","r")
fileData1=f1.readlines()
fileData2=f2.readlines()
Hydrogen1=input("Enter First Hydrogen Number: ")
Hydrogen2=input("Enter Second Hydrogen Number: ")
ConnectinAtom1=input("Enter First Molecule Connecting atom Number: ")
ConnectinAtom2=input("Enter Second Molecule Connecting atom Number: ")
num1=input("No. of atoms in first molecule: ")
num2=input("No. of atoms in second molecule: ")


originalData1=fileData1[1:num1+1]
connectionData1=fileData1[num1+1:]
originalData2=fileData2[1:num2+1]
connectionData2=fileData2[num2+1:]

counter=1
finalMolecule=[]
for i in range(0,num1):
	if i!=Hydrogen1-1:
		newAtom=list(originalData1[i].split())
		newAtom[1]=counter
		newAtom[4]=float(newAtom[4])
		newAtom[5]=float(newAtom[5])
		newAtom[6]=float(newAtom[6])
		finString=StringBuilder.buildString(newAtom)
		finalMolecule.append(finString)
		counter=counter+1
print counter
for i in range(0,num2):
	if i!=Hydrogen2-1:
		newAtom=list(originalData2[i].split())
		newAtom[1]=counter
		newAtom[4]=float(newAtom[4])
		newAtom[5]=float(newAtom[5])
		newAtom[6]=float(newAtom[6])
		finString=StringBuilder.buildString(newAtom)
		finalMolecule.append(finString)
		counter=counter+1

finalConnection=[]
for i in range(0,num1):
	connection=connectionData1[i].split()
	if str(connection[1])==str(Hydrogen1):
		continue
	newConnection=[]
	for j in connection:
		if str(j)!=str(Hydrogen1):
			if str(j)=='CONECT':
				newConnection.append(j)
			elif int(j)>Hydrogen1	:
				newConnection.append(str(int(j)-1))
			else:
				newConnection.append(j)
	finalConnection.append(newConnection)

for i in range(0,num2):
	connection=connectionData2[i].split()
	if str(connection[1])==str(Hydrogen2):
		continue
	newConnection=[]
	for j in connection:
		if str(j)!=str(Hydrogen2):
			if str(j)=='CONECT':
				newConnection.append(j)
			elif int(j)>Hydrogen1	:
				newConnection.append(str(int(j)-1+int(num1)-1))
			else:
				newConnection.append(int(j)+int(num1)-1)
	finalConnection.append(newConnection)

if Hydrogen1<ConnectinAtom1:
	ConnectinAtom1=ConnectinAtom1-1
if Hydrogen2<ConnectinAtom2:
	ConnectinAtom2=ConnectinAtom2-1

ConnectinAtom2=ConnectinAtom2+num1-1

finalConnection[ConnectinAtom1-1].append(ConnectinAtom2)
finalConnection[ConnectinAtom2-1].append(ConnectinAtom1)


f1.close()
f2.close()
fileName=fileName1+"_"+fileName2
f=open(fileName+".pdb",'w')
f.write("Remark..\n")
for atom in finalMolecule:
	atom=str(atom)
	atom=atom.strip('\n')
	f.write("%s\n" % atom)
for mlist in finalConnection:
	connection=StringBuilder.connectionStringBuilder(mlist)
	connection=connection.strip('\n')
	f.write("%s\n"%connection)
end="END"
f.write("%s\n"%end)
f.close()





