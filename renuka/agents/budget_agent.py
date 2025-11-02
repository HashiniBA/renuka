from crewai import Agent

budget_agent = Agent(
    role='Budget Estimator',
    goal='Estimate total travel cost including travel, stay, food and sightseeing.',
    backstory='You are a financial planner helping travelers manage their budgets.',
    verbose=True,
    allow_delegation=False,
    llm="ollama/llama3"
)