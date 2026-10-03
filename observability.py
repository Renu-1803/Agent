def agent_loop(max_iterations=3):
    logs = []

    for i in range(1, max_iterations + 1):
        # Step 1: Observe
        observation = f"Observation at iteration {i}"
        logs.append(observation)

        # Step 2: Decide
        action = f"Action selected at iteration {i}"
        logs.append(action)

        # Step 3: Execute
        result = f"Executed action at iteration {i}"
        logs.append(result)

        # Step 4: Check success
        if i == max_iterations:
            status = "SUCCESS"
            logs.append(f"Status: {status}")
            break
        else:
            logs.append("Status: CONTINUE")

    return logs


# Run the agent
full_log = agent_loop()

# Print the complete log
print("FULL AGENT LOG:")
for step in full_log:
    print(step)