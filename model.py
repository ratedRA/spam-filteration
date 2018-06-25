from preprocessing import make_dict, make_dataset
from sklearm.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score

d = make_dict()
feautres, labels = make_dataset(d)

x_train, x_test, y_train, y_test = tts(features, labels, test_size = 0.2)

clf = MultinomialNB()
clf.fit(x_train, y_train)

pred = clf.predict(x_test)
print(accuracy_score(y_test, pred))
save(clf, "text-classifier.mdl")