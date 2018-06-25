import os
import codecs
from collections import Counter

def make_dict():

	direct = "emails/"
	files = os.listdir(direct)

	emails = [direct + email for email in files]

	#print(emails)
	words = []
	c = len(emails)

	for email in emails:
		#f = open(email)
		with codecs.open(email, "r",encoding='utf-8', errors='ignore') as fdata:
			blob = fdata.read()
			words += blob.split(' ')
			print(c)
			c -= 1

	#print(words)

	for i in range(len(words)):
		if not words[i].isalpha():
			words[i] = ""

	dictionary = Counter(words)
	del dictionary[""]
	return dictionary.most_common(3000)

def make_dataset(dictionary):

	direct = "emails/"
	files = os.listdir(direct)

	emails = [direct + email for email in files]

	#print(emails)
	words = []
	labels = []
	feautre_set = []
	c = len(emails)

	for email in emails:
		#f = open(email)
		data = []
		with codecs.open(email, "r",encoding='utf-8', errors='ignore') as fdata:
			blob = fdata.read()
			words += blob.split(' ')

		for entry in dictionary:
			data.append(words.count(entry[0]))

		feautre_set.append(data)

		if "ham" in email:
			labels.append(0)
		if "spam" in email:
			labels.append(1)
		print(c)
		c -= 1

	return feautre_set, labels
'''
d = make_dict()

feautre_set, labels = make_dataset(d)

print(feautre_set, labels)
'''