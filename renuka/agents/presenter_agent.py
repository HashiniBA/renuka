from crewai import Agent

presenter_agent = Agent(
    role='Presenter',
    goal='Combine and present the final travel plan in a clean, formatted summary',
    backstory='You are a presentation expert creating beautiful, easy-to-read itineraries.',
    verbose=True,
    allow_delegation=False,
    llm="ollama/llama3"
)