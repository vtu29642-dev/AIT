import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Give me 3 ideas that i could build using openai apis"}
    ]
)

print(completion.choices[0].message.content)
