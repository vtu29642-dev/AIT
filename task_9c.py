import openai
import gradio as gr

openai.api_key = "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"  

messages = [
    {"role": "system", "content": "You are a financial expert that specializes in real estate investment and negotiation"}
]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gr.Interface(
    fn=CustomChatGPT,
    inputs="text",
    outputs="text",
    title="INTELLIGENT CHATBOT"
)

demo.launch(share=True)
