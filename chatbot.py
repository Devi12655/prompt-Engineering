import google.generativeai as genai

# 🔑 put your actual Gemini API key here
genai.configure(api_key="AIzaSyArudHe55VcvsFbzDXyidiYm3Ju_KT8DSs")

# load model
model = genai.GenerativeModel("gemini-1.5-flash")


def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text


print("Welcome to Conversational AI Chatbot (Google Gemini)!")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    reply = get_response(user_input)
    print(f"Chatbot: {reply}")
