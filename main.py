from app.controllers import LearningController
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    controller = LearningController()
    controller.run()


# app/models.py
class UserProfile:
    def __init__(self, name, prior_knowledge, learning_format):
        self.name = name
        self.prior_knowledge = prior_knowledge
        self.learning_format = learning_format

class LearningRequest:
    def __init__(self, topic, objectives):
        self.topic = topic
        self.objectives = objectives

class EducationalReport:
    def __init__(self, title, content, diagrams, citations, recommendations):
        self.title = title
        self.content = content
        self.diagrams = diagrams
        self.citations = citations
        self.recommendations = recommendations
