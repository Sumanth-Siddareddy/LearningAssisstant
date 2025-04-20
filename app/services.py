from .repository import ResearchRepository
from .models import EducationalReport
from .utils import generate_diagrams, generate_citations, recommend_resources
import ollama

from app.models import EducationalReport

class LearningService:
    def __init__(self, ollama_client):
        self.ollama_client = ollama_client
        self.banned_keywords = ["sex", "violence", "fight", "kill", "nude", "hack", "porn"]

    def generate_report(self, user_profile, learning_request):
        # Check for banned content
        if any(banned in learning_request.topic.lower() for banned in self.banned_keywords):
            return EducationalReport(
                topic=learning_request.topic,
                content="🚫 This topic contains restricted or inappropriate keywords. Please try a different educational topic.",
                diagrams=[],
                citations=[],
                resources=[]
            )

        # Query Ollama (Mistral model)
        ollama_response = self.query_ollama_model(
            f"You are an AI learning assistant helping a user understand the topic '{learning_request.topic}' "
            f"for the purpose: '{learning_request.objectives}'. The user has '{user_profile.prior_knowledge}' experience "
            f"and prefers content in a text format.\n\n"
            f"Please provide a clear, structured explanation tailored to their knowledge level, including:\n"
            f"1. Step-by-step breakdown in simple language.\n"
            f"2. Real-world examples or job/work-related use cases.\n"
            f"3. Visual aids or text-based diagram suggestions (if visual format is preferred).\n"
            f"4. References to reliable learning resources.\n"
            f"5. Mention of standard docs or tools (e.g., MDN for JavaScript).\n\n"
            f"Use section titles for clarity."
        )

        content = ollama_response.get("content", "Content not found.")
        diagrams = ollama_response.get("diagrams", [])
        citations = ollama_response.get("citations", [])
        resources = ollama_response.get("resources", [])

        # Remove empty section headers from content
        lines = content.splitlines()
        filtered_lines = []
        skip_section = False
        skip_headers = {"Diagrams:", "Citations:", "Recommended Resources:"}

        for line in lines:
            if line.strip() in skip_headers:
                skip_section = True
                continue
            elif skip_section:
                # Skip lines until next non-empty line that is not a list item
                if line.strip() == "" or line.strip().startswith(("-", "*", "[")):
                    continue
                else:
                    skip_section = False
            filtered_lines.append(line)

        cleaned_content = "\n".join(filtered_lines)

        # Save cleaned content to text file
        filename = f"ResponseData/{user_profile.name}_{learning_request.topic.replace(' ', '_').lower()}_report.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cleaned_content)

        return EducationalReport(
            topic=learning_request.topic,
            content=cleaned_content,
            diagrams=diagrams,
            citations=citations,
            resources=resources
        )


    def query_ollama_model(self, prompt):
        print("Querying model with prompt:\n", prompt)
        response = self.ollama_client.generate(
            model="mistral",  # <- Add this line!
            prompt=prompt
        )
        return {
            "content": response["response"],  # Mistral returns dict with "response" key
            "diagrams": [],
            "citations": [],
            "resources": []
        }



# class LearningService:
#     def generate_report(self, user_profile, learning_request):
#         topic = learning_request.topic.lower()

#         # 1. Block inappropriate topics
#         banned_keywords = ["sex", "violence", "fight", "kill", "nude", "hack","porn"]
#         if any(word in topic for word in banned_keywords):
#             return EducationalReport(
#                 topic="Inappropriate Topic",  # Changed from 'title' to 'topic'
#                 content="⚠️ I'm designed to provide assistance for legal, ethical, and respectful learning topics only.",
#                 diagrams=[],
#                 citations=[],
#                 resources=[]
#             )

#         # 2. Simulate RAG / Knowledge Retrieval (you'll replace this later)
#         search_results = self.simulate_search(topic)  # Simulated for now

#         if not search_results:
#             return EducationalReport(
#                 topic=topic,  # Changed from 'title' to 'topic'
#                 content="❗ I couldn't find enough useful material on this topic. Please try a different one or clarify your objective.",
#                 diagrams=[],
#                 citations=[],
#                 resources=[]
#             )

        # # 3. Query Ollama (Mistral model) for educational content
        # ollama_response = self.query_ollama_model(
        #     f"You are an AI learning assistant helping a user understand the topic '{learning_request.topic}' "
        #     f"for the purpose: '{learning_request.objectives}'. The user has '{user_profile.prior_knowledge}' level experience "
        #     f"and prefers the content in a '{user_profile.preferred_format}' format. "
        #     f"\n\nPlease provide a clear, structured educational explanation tailored to their knowledge level. "
        #     f"Include the following:\n"
        #     f"1. A step-by-step explanation using simple and concise language.\n"
        #     f"2. Real-world use cases or examples relevant to job interviews or work scenarios.\n"
        #     f"3. Visual descriptions or diagram suggestions (text-based if visual format is preferred).\n"
        #     f"4. Citations or references to reliable learning resources.\n"
        #     f"5. Mention any standard documentation websites (e.g., MDN for JavaScript) or tools related to the topic.\n"
        #     f"\nFormat your response clearly with section titles for easier understanding."
        # )


#         diagrams = generate_diagrams(topic)
#         citations = generate_citations(topic)
#         resources = recommend_resources(topic)

#         return EducationalReport(
#             topic=topic,  # Changed from 'title' to 'topic'
#             content=ollama_response,
#             diagrams=diagrams,
#             citations=citations,
#             resources=resources
#         )

#     def simulate_search(self, topic):
#         # This function simulates if useful data exists
#         known_topics = ["python", "javascript", "quantum computing", "machine learning"]
#         return ["dummy data"] if topic.lower() in known_topics else []

#     def query_ollama_model(self, prompt: str) -> str:
#         try:
#             response = ollama.chat(model='mistral', messages=[
#                 {"role": "user", "content": prompt}
#             ])
#             return response['message']['content']
#         except Exception as e:
#             return f"❗ Error communicating with the AI model: {str(e)}"
