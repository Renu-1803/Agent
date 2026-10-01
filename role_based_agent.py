# rule_based_agent.py

def rule_based_agent(user_input):
    user_input = user_input.lower()

    # Rule 1: Greeting
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    # Rule 2: Weather
    elif "weather" in user_input:
        return "Please provide your city name to check the weather."

    # Rule 3: Temperature
    elif "temperature" in user_input:
        return "The current temperature can be checked using a weather service."

    # Rule 4: Time
    elif "time" in user_input:
        return "The current time can be obtained from the system clock."

    # Rule 5: Exit
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day."

    # Default rule
    else:
        return "Sorry, I don't understand that request."


# Main program
print("Rule-Based Agent")
print("Type 'bye' or 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    response = rule_based_agent(user_input)

    print("Agent:", response)

    if "bye" in user_input.lower() or "exit" in user_input.lower():
        break