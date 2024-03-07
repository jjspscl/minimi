from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from apps.mail.models import Email
from apps.classifier.models import MLModel
from apps.classifier import services 

class MLClassifier:
    def __init__(self, emails: list[Email] = []):
        self.vectorizer = TfidfVectorizer()
        self.clf = RandomForestClassifier()
        self.emails = emails
        self.trained_model = None

    def train(self):
        emails = self.emails
        email_texts = [email.content for email in emails]

        X_train, X_test, y_train, y_test = train_test_split(
            email_texts, [0]*len(email_texts), test_size=0.2, random_state=42)

        unique_classes = set(y_train)
        if len(unique_classes) < 2:
            raise ValueError(
                "Training data must contain samples from at least two classes.")

        X_train_vec = self.vectorizer.fit_transform(X_train)

        self.clf.fit(X_train_vec, y_train)
        self.trained_model = self.clf

        self.save_model()

    def predict(self, email_content: str):
        if not self.trained_model:
            raise Exception('Model not trained')

        X_test_vec = self.vectorizer.transform([email_content])
        return self.trained_model.predict(X_test_vec)

    def load_model(self):
        ml_model, created = services.get_or_create_ml_model(name=self.clf.__class__.__name__)
        model_file_path = ml_model.model_file.path
        self.trained_model = joblib.load(model_file_path)

    def save_model(self):
        ml_model, created = services.get_or_create_ml_model(
            name=self.clf.__class__.__name__)
        model_file_path = ml_model.model_file.path
        joblib.dump(self.trained_model, model_file_path)