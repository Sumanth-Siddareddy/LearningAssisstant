from .services import LearningService
from .models import UserProfile, LearningRequest
import ollama

class LearningController:
    def __init__(self):
        self.ollama_client = ollama  # or a custom wrapper if you use one
        self.service = LearningService(self.ollama_client)

    def ask_user_preferences(self):
        name = input("Enter your name: ")
        prior_knowledge = input("Describe your prior knowledge (none/basic/advanced): ")
        learning_format = input("Preferred learning format (text/visual/audio): ")
        return UserProfile(name, prior_knowledge, learning_format)

    def ask_learning_topic(self):
        topic = input("Enter the topic you want to learn: ")
        objectives = input("What are your learning objectives? ")
        return LearningRequest(topic, objectives)

    def run(self):
        user_profile = self.ask_user_preferences()
        learning_request = self.ask_learning_topic()
        # report = self.service.create_report(learning_request.topic, learning_request.objectives)
        report = self.service.generate_report(user_profile, learning_request)
        # print(report)
        self.present_report(report)

    def present_report(self, report):
        print("\n===== EDUCATIONAL REPORT =====")
        print(f"Title: {report.topic}\n")
        print(f"Content:\n{report.content}\n")
