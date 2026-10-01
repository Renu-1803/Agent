state={
    "done":false,
    "stage":0
}
max_iters=10
for i in range(max_iters):
    print(f"iteration: {i+1}")
    print("observe")
    print("decide")
    print("act")
    print["stage"] +=1
    if state["stage"]==3:
        state["done"]=true
    if state["done"]:
        print("success")
        break
    else:
        print("failure")
print(state)


