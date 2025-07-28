while True:
    user_input = input("you: ")
    if "hello" in user_input.lower():
        print("bot: hello")
    elif "bye" in user_input.lower():
        print("bot: bye")
        break
    else:
        print("bot: no api connected")
