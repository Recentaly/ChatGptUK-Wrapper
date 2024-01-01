from assets.src.api import API

Api = API()

messages = [
    {"role": "system", "content": "You are GPT-4. The most advanced chatbot in the world. You have web search capabilities, calculator, and web browser. You can also do translations, and much more."},
    {"role": "user", "content": "Hi, what's the weather like in Washington DC?"},
]

for chunk in Api.chat(
    messages=messages,
    model="gpt-4-1106-preview",
    temperature=1,
):
    
    print(chunk, end="", flush=True)

# output: gradually, words appear