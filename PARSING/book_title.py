#!/usr/bin/python
import difflib

book_author={}
target=open("book_similarity.txt",'w')
with open("book_match1.txt") as f:
	content = f.readlines()
	#print content
l=[]
for row in content:
	#print row
	temp = row.split(">>")
	temp[1] = temp[1].replace("\n", "")
	if '|' in temp[1]:
		temp[1]=temp[1].split("|")
		book_author[temp[0]] = temp[1]
	else:
		l=[temp[1]]
		book_author[temp[0]]=l
		l=[]

length=len(book_author)

titles=book_author.keys()
for i in range(0,len(titles)):
	for j in range(i+1,len(titles)):
		a=titles[i]
		b=titles[j]
		seq=difflib.SequenceMatcher(a=a.lower(),b=b.lower())
		if seq.ratio() > 0.4:
			if seq.ratio() > 0.75:
				if book_author[titles[i]]==book_author[titles[j]]:
					continue

			for auth1 in book_author[titles[i]]:
				for auth2 in book_author[titles[j]]:
					target.write(auth1+','+auth2+','+str(seq.ratio())+'\n')


target.close()

'''
with open("book_similarity.txt") as f:
	content = f.readlines()
f.close()

graph_article={}
for row in content:
	auth1=row.split(',')
	auth2=auth1[1]
	wgt=auth1[2].replace('\n','')
	print auth1[0],auth2,wgt
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

'''

