# Import necessary libraries
from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource
from dotenv import load_dotenv
from langchain_groq import ChatGroq

import os

# Load environment variables from a .env file
load_dotenv()

# Retrieve API keys from environment variables
GEMINI_API_KEY = os.environ.get("GOOGLE_API_KEY")  # GEMINI API key
groq_api_key = os.environ.get('GROQ_API_KEY')      # Groq API key
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY') 
# Create a CSV knowledge source to enable CSV file parsing and understanding
csv_source = CSVKnowledgeSource(
    file_paths=["Employees.csv"]  # Path to the CSV file (Add your Data)
)

# Configure ChatGroq, specifying the Groq provider and model details
# llm = ChatGroq(
#     api_key=groq_api_key,
#     model="groq/llama3-70b-8192",  # Use the specified Groq LLM model
#     temperature=0.5,               # Control response randomness
# )



llm = LLM(
    model="openrouter/qwen/qwen3-30b-a3b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)



# Create an agent responsible for interacting with the CSV data
agent = Agent(
    role="CSV Data Expert",          # Role of the agent
    goal="Answer questions and provide insights about the uploaded CSV file.",
    backstory="""You are a master at understanding and analyzing CSV files. 
                  You excel at parsing data, providing summaries, and answering detailed queries based on the file's contents.""",
    verbose=True,                    # Enable detailed output
    allow_delegation=False,          # Disallow task delegation
    llm=llm,                         # Use the configured LLM
    embedder={                       # Embedder configuration for enhanced data processing
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
    }
)

# Define a task template to answer questions about the CSV file
task_template = Task(
    description="Answer the following questions about the uploaded CSV file: {question}",
    expected_output="A detailed answer to the question about the CSV file.",
    agent=agent,
)

# Create a Crew object to manage agents, tasks, and data sources
crew = Crew(
    agents=[agent],                 # List of agents in the crew
    tasks=[],                       # Initialize with an empty task list
    verbose=True,                   # Enable detailed output
    process=Process.sequential,     # Sequential task execution
    knowledge_sources=[csv_source], # Knowledge source: the CSV file
    embedder={                      # Embedder configuration
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
    }
)

# Interactive loop to allow user input for multiple questions
while True:
    user_question = input("Enter your question (or type 'exit' to quit): ")
    if user_question.lower() == "exit":  # Exit condition
        break

    # Create a new task for the user-provided question
    task = Task(
        description=f"Answer the following question about the uploaded CSV file: {user_question}",
        expected_output="A detailed answer to the question.",
        agent=agent,
    )
    crew.tasks.append(task)  # Add the task to the crew's task list

    # Execute the task and get the result
    result = crew.kickoff(inputs={"question": user_question})
    print(f"Answer: {result}")  # Display the answer to the user

# Print a closing message after the user exits
print("Thank you for using the CSV Data Expert!")
