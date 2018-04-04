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
				intermediateConnection.append(str(int(j)+i))
		newConnection.append(intermediateConnection)
	return newConnection

def createLastMoleculeConnectingData(connectionData,units,endHydrogen,num,startHydrogen):
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

