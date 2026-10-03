def execute_action(action):
    valid_actions = ["move", "stop", "search"]

    # Check for invalid action
    if action not in valid_actions:
        return {
            "status": "error",
            "error": f"Invalid action: {action}",
            "valid_actions": valid_actions
        }

    # Execute valid action
    return {
        "status": "success",
        "action": action,
        "message": f"Action '{action}' executed successfully"
    }


# Test with an invalid action
result = execute_action("fly")

print(result)