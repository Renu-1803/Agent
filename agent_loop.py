# agent_loop.py

def agent_loop():
    state = 0

    for iteration in range(1, 4):  # 3 iterations
        print(f"\n--- Iteration {iteration} ---")

        # 1. Observe
        print("Agent observes state:", state)

        # 2. Decide
        if state < 3:
            action = "Increase state by 1"
        else:
            action = "Keep state unchanged"

        print("Agent decides:", action)

        # 3. Act
        if action == "Increase state by 1":
            state += 1

        print("Agent performs action")
        print("New state:", state)

    print("\nAgent loop completed.")


# Run the agent
agent_loop()