import openai

openai.api_key = "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"  

messages = []

system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready! Type your query (type 'quit()' to exit)")

while True:
    message = input()
    if message.lower() == "quit()":
        print("Exiting chat...")
        break

    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
