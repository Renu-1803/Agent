# agent_loop.py

def agent_loop(max_iterations=3):

    state = 0

    for iteration in range(1, max_iterations + 1):

        print(f"\n--- Iteration {iteration} ---")

        # 1. Observe
        print("Current state:", state)

        # 2. Check success condition
        if state >= 3:
            return {
                "status": "success",
                "state": state,
                "iteration": iteration
            }

        # 3. Decide action
        action = "increase"

        print("Action:", action)

        # 4. Perform action
        if action == "increase":
            state += 1

        print("Updated state:", state)

        # 5. Check success after action
        if state >= 3:
            return {
                "status": "success",
                "state": state,
                "iteration": iteration
            }

    # 6. Maximum iterations reached
    return {
        "status": "failure",
        "state": state,
        "iteration": max_iterations
    }


# Run the agent
result = agent_loop(max_iterations=3)

print("\n--- Final Result ---")
print("Status:", result["status"])
print("State:", result["state"])
print("Iterations:", result["iteration"])