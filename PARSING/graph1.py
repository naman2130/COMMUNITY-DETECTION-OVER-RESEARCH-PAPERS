#!/usr/bin/python
import difflib
graph_article={}
with open("incoll_graph.txt") as f:
	content=f.readlines()
f.close()
	#temp=content.replace('\n','')
for row in content:
	id_tuple=()
	temp=row.split(',')
	id_tuple=id_tuple+(int(temp[0]),)
	id_tuple=id_tuple+(int(temp[1]),)
	if id_tuple in graph_article:
		graph_article[id_tuple]+=int(temp[2].replace('\n',''))
	else:
		graph_article[id_tuple]=int(temp[2].replace('\n',''))
	#print graph_article

with open("incoll_graph.txt") as f:
	content=f.readlines()
f.close()

for row in content:
	id_tuple=()
	temp=row.split(',')
	id_tuple=id_tuple+(int(temp[0]),)
	id_tuple=id_tuple+(int(temp[1]),)
	if id_tuple in graph_article:
		graph_article[id_tuple]+=int(temp[2].replace('\n',''))
	else:
		graph_article[id_tuple]=int(temp[2].replace('\n',''))


with open("fphd_new.txt") as f:
	content=f.readlines()
f.close()

for row in content:
	id_tuple=()
	temp=row.split(',')
	id_tuple=id_tuple+(int(temp[0]),)
	id_tuple=id_tuple+(int(temp[1]),)
	if id_tuple in graph_article:
		graph_article[id_tuple]+=int(temp[2].replace('\n',''))
	else:
		graph_article[id_tuple]=int(temp[2].replace('\n',''))
with open("article_journal_author.txt") as f:
	content = f.readlines()
f.close()
for row in content:
	temp = row.split("#")
	author_id = temp[1].split("|")
	length=len(author_id)
	i=0
	j=i+1
	id_tuple=()
#print "list length is " + str(length)
	while i<=(length-2):
		while (j<=length-1):
			id_tuple=()
			small=min(int(author_id[i]),int(author_id[j]))
			large=max(int(author_id[i]),int(author_id[j]))
			id_tuple=id_tuple+(small,)
			id_tuple=id_tuple+(large,)
#print id_tuple
			if id_tuple in graph_article:
				graph_article[id_tuple]+=10
			else:
				graph_article[id_tuple]=10
			j=j+1
		i=i+1	 		

with open("article_author_connection.txt") as f:
	content = f.readlines()
f.close()

#print len(content)
for row in content:
	temp = row.split("#")
	author = temp[0]
	co_list = temp[1].split("?")
	co_list = co_list[1:]
	co_authors = []
	#print co_list	
	for item in co_list:
		dum = item.split("|")
		dum = dum[1:len(dum)-1]
		for au in dum :
			co_authors.append(au)
	#print co_authors
	for auth in co_authors:
		id_tuple  = ()
		small=min(int(author),int(auth))
		large=max(int(author),int(auth))
		id_tuple=id_tuple+(small,)
		id_tuple=id_tuple+(large,)
		#print id_tuple
		if id_tuple in graph_article:
			graph_article[id_tuple]+=10
		else:
			graph_article[id_tuple]=10
	co_auth = []				#[[], [], ]
	for item in co_list:
		temp = item.split("|")
		temp = temp[1:len(dum) - 1]
		co_auth.append(temp)

	for item in co_auth:
		i = 0
		while i < len(item):
			j = i+1
			while j < len(item):
				id_tuple = ()
				main_auth = item[i]
				sec_auth = item[j]
				small=min(main_auth,sec_auth)
				large=max(main_auth,sec_auth)
				id_tuple=id_tuple+(small,)
				id_tuple=id_tuple+(large,)
				if id_tuple in graph_article:
					graph_article[id_tuple]+=10
				else:
					graph_article[id_tuple]=10
				j+= 1
			i+=1
#print len(graph_article)

with open("book_match1.txt") as f:
	content = f.readlines()

f.close()

#graph_article={}

for row in content:
	temp = row.split(">>")
	#print temp[0]
	temp = temp[1]
	if temp.find("|") != -1:
		dum = temp.split("|")
		i = 0
		while i < len(dum):
			#print dum
			j = i+1
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

for row in open("phd_masters.txt"):
	dum = row.split("#")
	dum = dum[:len(dum) - 1]
	i = 0
	while i < len(dum):
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



with open("book_similarity.txt") as f:
	content = f.readlines()
f.close()
for row in content:
	auth1=row.split(',')
	auth2=auth1[1]
	wgt=auth1[2].replace('\n','')
	#print auth1[0],auth2,wgt
	id_tuple = ()
	small=min(int(auth1[0]),int(auth2))
	large=max(int(auth1[0]),int(auth2))
	id_tuple=id_tuple+(small,)
	id_tuple=id_tuple+(large,)
#print id_tuple
	if id_tuple in graph_article:
		graph_article[id_tuple]+=int(float(wgt)*10)
	else:
		graph_article[id_tuple]=int(float(wgt)*10)


for key in graph_article:
	print str(key[0])+","+str(key[1])+","+str(graph_article[key])
