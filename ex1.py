import os
import codecs
import re
from nltk.stem.porter import *

stemmer = PorterStemmer()
path = "dataset/"
lst_name = []
data = []

for fpath ,dirs , fs in os.walk(path):
	for f in fs:
		filename = os.path.join(fpath, f)
		if not filename.endswith('.DS_Store'):
			lst_name.append(filename)


for ele in lst_name:
	file = codecs.open(ele,'r',encoding = 'Latin1')
	content = file.read()
	# content = re.sub("[^a-zA-Z]+", " ", content)
	content = re.sub(r'[^a-z]', ' ', content.lower() ).strip()
	#content_list = content.split(" ")
	# content = content.lower()
	tmp = content.split()
	data = data + tmp
	#data_tmp.append(content.split(" "))


stop_word = set(line.strip() for line in open('stopwords.txt', encoding="utf8"))

data[:] = [x for x in data if x not in stop_word]
data = [stemmer.stem(plural) for plural in data]


# for ele in lst_name:
# 	print(ele)
#
# for ele in data:
# 	print(ele)


filename = "result_file.txt"
with open(filename,'w') as file_object:
	for ele in data:
		file_object.write(ele+"\n")
