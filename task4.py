messages = ["Hi", "Welcome to the platform", "OK"]

for msg in messages:
    length = len(msg)

    print("Message:", msg)
    print("Length:", length)

    if length > 10:
        print("Status: Long message")
    else:
        print("Status: Short message")

    print("------")