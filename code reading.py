def agent_loop():
    steps = [
        "Observe the environment",
        "Execute the action"
    ]

    for i, step in enumerate(steps, start=1):
        print(f"Step {i}: {step}")

    return {
        "status": "success",
        "steps_completed": 2,
        "message": "Agent completed 2 steps"
    }


# Run the agent
result = agent_loop()

print("\nPredicted Output:")
print(result)