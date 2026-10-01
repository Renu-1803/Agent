# goal_based_agent.py

class GoalBasedAgent:

    def __init__(self, goal):
        self.goal = goal

    def choose_action(self, current_location):
        # If the goal is already reached
        if current_location == self.goal:
            return "Goal reached!"

        # Simple route knowledge
        routes = {
            "Home": "Bus Stop",
            "Bus Stop": "Railway Station",
            "Railway Station": "City Center",
            "City Center": "College"
        }

        # Select the next action toward the goal
        if current_location in routes:
            next_location = routes[current_location]
            return f"Go from {current_location} to {next_location}"

        return "No route available."


# Create agent with a goal
agent = GoalBasedAgent("College")

current_location = "Home"

print("Goal:", agent.goal)
print("Starting location:", current_location)

while current_location != agent.goal:

    action = agent.choose_action(current_location)

    print("Agent:", action)

    # Extract next location
    routes = {
        "Home": "Bus Stop",
        "Bus Stop": "Railway Station",
        "Railway Station": "City Center",
        "City Center": "College"
    }

    if current_location in routes:
        current_location = routes[current_location]
    else:
        break

print("Agent:", agent.choose_action(current_location))