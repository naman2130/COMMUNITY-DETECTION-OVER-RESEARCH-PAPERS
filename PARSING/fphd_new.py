with open('fphd.txt','r') as f:
	content=f.readlines()

f.close()
target=open('fphd_new.txt','w')
for row in content:
	temp=row.split(',')
	temp[2]=int(float(temp[2].replace('\n',''))*10)
	target.write(temp[0]+","+temp[1]+","+str(temp[2])+'\n')


target.close()