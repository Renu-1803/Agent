def agent_loop(max_iterations=5):
    iteration = 0

    while iteration < max_iterations:
        print(f"Iteration: {iteration + 1}")

        # Agent work
        print("Agent is working...")

        # FIX: increment iteration
        iteration += 1

    return {
        "status": "success",
        "iterations": iteration
    }


result = agent_loop()

print("\nFinal Result:")
print(result)