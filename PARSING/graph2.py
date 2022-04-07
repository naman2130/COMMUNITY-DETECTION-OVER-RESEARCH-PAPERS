

#with open("inproceedings.txt") as f:
	#content = f.readlines()

#f.close()
import sys
graph_article={}

for row in open("incollection.txt"):
	temp = row.split(">>")
	#print temp[0]
	temp = temp[1]
	if temp.find("|") != -1:
		dum = temp.split("|")
		i = 0
		while i < len(dum):
			#print dum[i]
			j = i+1
			while j < len(dum):
				id_tuple = ()
				small=min(int(dum[i]),int(dum[j]))
				large=max(int(dum[i]),int(dum[j]))
				id_tuple=id_tuple+(small,)
				id_tuple=id_tuple+(large,)
				#print id_tuple ,  " " ,  str(sys.getsizeof(graph_article))
				if id_tuple in graph_article:
					graph_article[id_tuple]+=2
				else:
					graph_article[id_tuple]=2
				j=j+1
			i=i+1	 

for key in graph_article:
	print str(key[0])+","+str(key[1])+","+str(graph_article[key])
