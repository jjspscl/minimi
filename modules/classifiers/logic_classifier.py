from apps.mail.models import Email
class LogicClassifier:
    def __init__(self, emails: list[Email], keywords: list[str] = [], default: str = 'regular') -> None:
        self.keywords = set(keywords)
        self.emails = emails
        self.default = default

    def classify(self) -> list[list[str, str, str]]:
        # return [
        #     (keyword, message)
        #     for message in self.emails
        #     for keyword in (self.keywords if self.keywords else ['regular'])
        #     if keyword in message
        # ]
        return [
            (email.id, keyword, email.content)
            for email in self.emails
            for keyword in (self.keywords if self.keywords else self.default)
            if keyword in email.content
        ]


