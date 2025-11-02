from crewai import Crew, Task
from agents.trip_planner_agent import trip_planner_agent
from agents.hotel_agent import hotel_agent
from agents.budget_agent import budget_agent
from agents.presenter_agent import presenter_agent

def run_travel_planner(user_query: str):
    t1 = Task(
        description=f'Create an itinerary for the user query: {user_query}',
        agent=trip_planner_agent,
        expected_output='Day wise plan with key locations, activities, and timing.'
    )
    t2 = Task(
        description=f'Suggest hotels and food based on the itinerary above and user preferences.',
        agent=hotel_agent,
        expected_output='List of hotels and restaurants with brief details.'
    )
    t3 = Task(
        description=f'Estimate travel, stay,  and food budget based on itinerary and hotel details.',
        agent=budget_agent,
        expected_output='Estimated total budget and cost breakdown.'
    )
    t4 = Task(
        description=f'Combine itinerary, hotels and budget into one well-formatted final summary.',
        agent=presenter_agent,
        expected_output='Readable trip summary in Markdown format'
    )

    crew = Crew(
        agents=[trip_planner_agent, hotel_agent, budget_agent, presenter_agent],
        tasks=[t1, t2, t3, t4],
        llm="ollama/llama3",
        verbose=2
    )

    result = crew.run()
    return result