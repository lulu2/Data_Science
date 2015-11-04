from sys import argv
import sys

reload(sys)  
sys.setdefaultencoding('utf8')
script, filename= argv

readFile = (open(filename)).read()
paras = readFile.split('\n')
parasCopy = []
paraIndex = 0
inCollecting = 0
collection = []
tempCollection = []
for paragraph in paras:
	paragraph = paragraph.strip()
	if paragraph == '':
		inCollecting = 0
		collection.append(tempCollection)
		tempCollection = []
	if inCollecting:
		element = paragraph.split(' ')
		while element.count('') > 0:
			element.remove('')
		tempCollection.append([element[0], element[4], element[6], element[8]])
	if paragraph[0:7] == "reviews":
		inCollecting = 1
while collection.count([]) > 0:
	collection.remove([])
print collection

# Write File
loadFile = open('amazon.txt', 'w')
loadFile.write("item date rating votes helpful\n")
productCount = 0
for productInfo in collection:
	productCount += 1
	for productTuple in productInfo:
		productTuple.insert(0, str(productCount))
		loadFile.write(' '.join(productTuple))
		loadFile.write("\n")
loadFile.close()

