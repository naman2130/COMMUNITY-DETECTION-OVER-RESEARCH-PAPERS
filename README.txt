Community Detection in DBLP:


We need to find the communities of the authors in the dblp(digital bibliography and library project) corpus.((It can be downloaded from http://dblp.uni-trier.de/xml/) 
(Download dblp.xml.tar.gz as well as dblp.dts and keep it in the same folder).

It consists of the following tags:
article – An article from a journal or magazine
inproceedings – A paper in a conference or workshop proceedings.
proceedings – The proceedings volume of a conference or workshop.
book – An authored monograph or an edited collection of articles.
incollection – A part or chapter in a monograph.
phdthesis – A PhD thesis.
mastersthesis – A Master's thesis. There are only very few Master's theses in dblp.
www – A web page. It also contains all the aliasing of the authors within the tag

Output of the program after execution:
www.py: To remove aliasing we executed this. It assigns a single ID to the author and their aliases. After that everywhere an author will be referenced with their ID.(ouput generated is www_parse)

article.py: It outputs two files. the first one contains an author and their respective couthors (article_author_connection1.txt)
The second file generated is article_journal_author.txt that contains different authors in the journal.

Book.py: It outputs two files - book_match1.txt that gives the list of authors who contributed to the same book and auth_co.txt that contains author and coauthors.

book_similarity.py: We found connection between different titles using difflib and assigned some weight to the two authors who have similarity > 0.4
Output file generated is book_similarity.txt

inproceedings.py: We found all the authors or editors who worked on the same book title. (output file is inproceedings.txt)

proceedings.py: We found all the authors or editors who worked on the same book title. (output file is proceedings.txt)

incollection.py: We found all the authors or editors who worked on the same book title. (output file is incollection.txt)

phd_thesis.py: It collects all the authors who have done their phd in the same school. (output is phd_masters.txt)

phd_graph.py: It gives weight to the authors who have very less difference in their title using difflib.

graph1.py: It assigns weight to the edges that have some relationship. For instance, the edge joining the authors belonging to same journal tag is given a weight of 10. In the same way, the edge joining the authors working together on the same book is given a weight of 5. The edge joining the authors working on different titles are given weight according to the similarity calculated using the python difflib library.

Now we have our output graph.txt (in the form of u,v,w).

Now we run our community detection algorithm to find the communities in the graph.

Firstly we ran Newman-Girvan algorithm on our graph but complexity of newman-girvan is very large i.e O(mn)(where m is no of nodes and n is no of vertices)

Then we ran Louvain's algorithm on our graph that is suitable for a very large dataset. 

Then we ran CPM algorithm for community detection (refer cpm_guide.txt to run the code )

Using the above methods, we generated communities in the dblp corpus.


