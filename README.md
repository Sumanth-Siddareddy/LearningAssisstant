# AI Learning Assistant – Personalized Educational Report Generator using Ollama (Mistral)

## Project Description
This is a Python-based CLI application that generates structured educational content using LLMs. It asks users for:
- Their name
- Prior knowledge level
- Preferred learning format
- Desired topic
- Learning goals

It uses this information to generate a report using the **Mistral model via Ollama**.

## Features
- Query personalization based on user input
- Calls Ollama model (e.g., `mistral`)
- Generates structured educational reports
- Saves output to a text file with a dynamic filename

## Installation Guide

### Prerequisites
Ensure you have the following installed:
- Python 3.10 or above
- `pip` (Python package installer)
- Ollama ([Download from here](https://ollama.com/))

### Steps to Install

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ai-learning-assistant.git
   cd ai-learning-assistant
   ```

2. **Create a Virtual Environment (optional but recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate       # macOS/Linux
    .\venv\Scripts\activate        # Windows
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    Or 
    ```bash
    pip install llama-index llama-index-llms-ollama llama-index-readers-file llama-index-vector-stores-faiss
    ```

4. **Install and Run Ollama**
    - Download and install Ollama from : https://ollama.com/download
    - Click the “Download for Windows” button to get the .exe installer.
    - After it's done, it should add Ollama to your system PATH automatically.
    - Please check the PATH in environment variables. Both User and System PATH.
    - for verification run cmd : ollama --version
    - Open a terminal and run cmd : ( Run the ollama so that the application will work properly)
    ```bash
    ollama run mistral
    ``` 
    - Use crtl+d to stop the ollama

5. **Project Structure**
    ```bash
        LearningAssitant
        ├── app/
        │   ├── __init__.py
        │   ├── controllers.py         # Handles input and application logic
        │   ├── rag_engine.py
        │   ├── repository.py          # Try to search research references
        │   ├── models.py              # UserProfile, LearningRequest, etc.
        │   ├── services.py            # Querying Ollama and report generation
        │   └── utils.py               # Optional: file operations, helpers
        ├── main.py                    # Entry point
        ├── requirements.txt           # Required packages
        ├── README.md                  # Project documentation
        ├── .gitignore                 # Git ignore rules
        └── ResponseData/         # (Optional) Folder to store output text files
    ```

6. **How to Run the Program**
    1. Run the program using:
    ```bash
    python main.py
    ```
    2. Follow the prompts: (example)
    ```bash
    Enter your name: sumanth
    Describe your prior knowledge (none/basic/advanced): basic
    Preferred learning format (text/visual/audio): text
    Enter the topic you want to learn: Object Oriented Programming in JAVA
    What are your learning objectives? Learn and practice
    ```
    3. Your educational report will be saved as:
    ```bash
    sumanth_object_oriented_programming_in_java_report.txt
    ```


