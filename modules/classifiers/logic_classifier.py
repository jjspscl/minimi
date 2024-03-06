
class LogicClassifier:
    def __init__(self, messages: list[str], keywords: list[str] = []) -> None:
        self.keywords = set(keywords)
        self.messages = messages

    def classify(self) -> list[tuple[str, str]]:
        return [
            (keyword, message) 
            for keyword in self.keywords 
            for message in self.messages 
            if keyword in message
        ]

