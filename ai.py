import google.generativeai as genai

# 🔑 Configure with your Gemini API key (from Google AI Studio)
genai.configure(api_key="AIzaSyArudHe55VcvsFbzDXyidiYm3Ju_KT8DSs")

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")


def answer_question():
    q = input("Ask your question: ")
    prompt = f"You are a knowledgeable assistant. {q}"
    response = model.generate_content(prompt)
    print("Assistant:", response.text.strip())


def summarize_text():
    text = input("Enter text to summarize: ")
    prompt = f"Summarize this: {text}"
    response = model.generate_content(prompt)
    print("Summary:", response.text.strip())


def generate_content():
    topic = input("Enter a topic for creative content: ")
    prompt = f"Write a short story about: {topic}"
    response = model.generate_content(prompt)
    print("Story:", response.text.strip())


print("\nAI Assistant Menu")
print("1. Answer a Question")
print("2. Summarize Text")
print("3. Generate Creative Content")
print("4. Exit")
while True:
    choice = input("Select an option: ")
    if choice == "1":
        answer_question()
    elif choice == "2":
        summarize_text()
    elif choice == "3":
        generate_content()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
