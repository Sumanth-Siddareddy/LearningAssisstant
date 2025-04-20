from dataclasses import dataclass
from typing import List

@dataclass
class UserProfile:
    name: str
    prior_knowledge: str
    preferred_format: str

@dataclass
class LearningRequest:
    topic: str
    objectives: str

@dataclass
class EducationalReport:
    topic: str
    content: str
    diagrams: List[str]
    citations: List[str]
    resources: List[str]

    def __repr__(self):
        return (f"EducationalReport(topic={self.topic}, "
                f"content={self.content}, "
                f"diagrams={self.diagrams}, "
                f"citations={self.citations}, "
                f"resources={self.resources})")
