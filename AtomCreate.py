import StringBuilder
import ConnectingData

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
			finString=StringBuilder.buildString(newAtom)
			startMolecule.append(finString)
			count=count+1
	return startMolecule

def createMainAtom(data,counter,num,connectingAtom):
	length=len(data)
	newAtom=list(data[length-num+connectingAtom].split())
	newAtom[2]='C'
	# print newAtom[4]
	newAtom[1]=counter
	sourceAtom=data[0].split()
	mainAtom=data[1].split()
	newAtom[4]=float(newAtom[4])-float(sourceAtom[4])+float(mainAtom[4])
	newAtom[5]=float(newAtom[5])-float(sourceAtom[5])+float(mainAtom[5])
	newAtom[6]=float(newAtom[6])-float(sourceAtom[6])+float(mainAtom[6])
	finString=StringBuilder.buildString(newAtom)
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
		finString=StringBuilder.buildString(newAtom)
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
		finString=StringBuilder.buildString(newAtom)
		data.append(finString)
		start=start+1
		counter=counter+1


