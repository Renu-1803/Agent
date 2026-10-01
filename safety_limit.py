def agent_loop():
    max_iters=10
    for i in range(max_iters):
        observtion=observe()
        decision=decide(observation)
        if decision =="success":
            return"success"
        act(decision)
    return"failure"
    