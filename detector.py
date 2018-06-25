from preprocessing import make_dict, make_dataset
import pickle as p

def load(clf_file):
	with open(clf_file) as cf:
		clf = p.load(cf)

d = make_dict()

features = []

testCase = input("enter the message for check:")

for word in d:
	feautres.append(testCase.count(word[0]))

res = clf.predict([features])
print(["not spam", "spam"][res[0]])