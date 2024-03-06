from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


class MLClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.clf = LogisticRegression()

    def train(self, data: list[str]):
        X_train, X_test, y_train, y_test = train_test_split(
            data, [0]*len(data), test_size=0.2, random_state=42)

        X_train_vec = self.vectorizer.fit_transform(X_train)

        self.clf.fit(X_train_vec, y_train)

    def predict(self, data: list[str]):
        X_test_vec = self.vectorizer.transform(data)
        return self.clf.predict(X_test_vec)
