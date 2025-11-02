from crewai import Agent

hotel_agent = Agent(
    role='Hotel and Food Recommender',
    goal='Suggest a good hotels and restaurants within budget near the destination',
    backstory='You are an expert on Hotels, local cuisine and affordable stays',
    verbose=True,
    allow_delegation=False,
    llm="ollama/llama3"
)