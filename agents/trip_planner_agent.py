from crewai import Agent

trip_planner_agent = Agent(
    role='Trip Planner',
    goal='Create an itinerary based on destination, duration and interests.',
    backstory='You are a travel guide specializing in planning trips across India.',
    verbose=True,
    allow_delegation=False,
    llm="ollama/llama3"
)