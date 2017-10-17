from nltk.corpus import names
import nltk, random


def gender_features(word):
    features = dict()
    word = word.lower()
    features['first_letter'] = word[0]
    features['last_letter'] = word[-1]
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features['count({})'.format(letter)] = word.count(letter)
        features['has({})'.format(letter)] = letter in word
    return features
labeled_names = [(name.lower(), 'male') for name in names.words('male.txt')] + [(name.lower(), 'female')
                                                                    for name in names.words('female.txt')]
random.shuffle(labeled_names)
feature_set = [(gender_features(name.lower()), gender) for name, gender in labeled_names]

train_names = labeled_names[1500:]
devtest_names = labeled_names[500:1500]
test_names = labeled_names[:500]

train_set = [(gender_features(name), gender) for name, gender in train_names]
devtest_set = [(gender_features(name), gender) for name, gender in devtest_names]
test_set = [(gender_features(name), gender) for name, gender in test_names]

classifier = nltk.NaiveBayesClassifier.train(train_set)
print('Accuracy is :', nltk.classify.accuracy(classifier, devtest_set))


errors = [(gender, classifier.classify(gender_features(name)), name) for name, gender in devtest_names
          if classifier.classify(gender_features(name)) != gender]

for error in errors:
    print(error)