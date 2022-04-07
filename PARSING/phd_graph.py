import difflib
graph_article={}
ids=[]
title=[]
for row in open("phd_masters1.txt"):
	dum = row.split("#")
#	print dum
#print str(len(dum)) + " "
#	dum = dum[:len(dum) - 1]
	dum = dum[1:len(dum)]
#print dum
	id_title=dum[0].split('|')
	if len(ids)==0:
		ids=[id_title[0].strip()]
	else:
		ids.append(id_title[0].strip())
	if len(title)==0:
		title=[id_title[1].strip()]
	else:	
		title.append(id_title[1].strip())
#print ids
#print title
#print len(ids), len(title)
i = 0
print "len of ids = ",
print len(ids)
while i<len(ids):
	j=i+1
	while j<len(ids):
		id_tuple=()
		small=min(int(ids[i]),int(ids[j]))
		large=max(int(ids[i]),int(ids[j]))
		id_tuple=id_tuple+(small,)
		id_tuple=id_tuple+(large,)
		a=title[i]
		b=title[j]
		seq=difflib.SequenceMatcher(a=a.lower(), b=b.lower())
		if seq.ratio() > 0.4:
			if id_tuple in graph_article:
				graph_article[id_tuple]+=seq.ratio()
			else:
				graph_article[id_tuple]=seq.ratio()
		j=j+1
		print "j =",j," i =",i  
	i=i+1
	   
for key in graph_article:
	print str(key[0])+","+str(key[1])+","+str(graph_article[key])
'''	while i < len(dum):
		j = i + 1
		while j < len(dum):
			id_tuple = ()
			small=min(int(dum[i]),int(dum[j]))
			large=max(int(dum[i]),int(dum[j]))
			id_tuple=id_tuple+(small,)
			id_tuple=id_tuple+(large,)
#print id_tuple
			if id_tuple in graph_article:
				graph_article[id_tuple]+=5
			else:
				graph_article[id_tuple]=5
			j=j+1
		i=i+1

for key in graph_article:
	print str(key[0])+","+str(key[1])+","+str(graph_article[key])	 '''

