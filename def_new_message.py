messages = ['hello', 'bye', 'new', 'time']
send_messages = []

def new_send_messages(messages, send_messages):
    while messages:
        send_message = messages.pop()
        print(f"Send message {send_message}")

        send_messages.append(send_message) 

def show_messsages(send_messages):
    try:
        for message in send_messages:
            print(f"Message: {message}")
    except TypeError:
        print("Something wrong!")

print(messages)
print(send_messages)

new_send_messages(messages[:], send_messages)

print(messages)
print(send_messages)

show_messsages(send_messages)

print(messages)
print(send_messages)