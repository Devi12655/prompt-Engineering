import google.generativeai as genai
import random

# Configure with your Gemini API key
genai.configure(api_key="AIzaSyArudHe55VcvsFbzDXyidiYm3Ju_KT8DSs")

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# Store feedback
feedback_log = []

# Prompt sets for each function with variations
question_prompts = [
    lambda q: f"You are a knowledgeable assistant. Please answer: {q}",
    lambda q: f"Answer this question concisely and clearly: {q}",
    lambda q: f"As an expert, provide detailed information on: {q}",
]

summary_prompts = [
    lambda text: f"Summarize this text briefly: {text}",
    lambda text: f"Provide a clear and concise summary: {text}",
    lambda text: f"Give a short overview of the following: {text}",
]

creative_prompts = [
    lambda topic: f"Write a short story about: {topic}",
    lambda topic: f"Create a creative and engaging story on this topic: {topic}",
    lambda topic: f"Generate a fictional tale involving: {topic}",
]


def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()


def ask_feedback():
    while True:
        feedback = input("Was this response helpful? (yes/no): ").strip().lower()
        if feedback in ["yes", "no"]:
            return feedback
        print("Please enter 'yes' or 'no'.")


def answer_question():
    q = input("Ask your question: ").strip()
    prompt_fn = random.choice(question_prompts)
    prompt = prompt_fn(q)
    resp = get_response(prompt)
    print("\nAssistant:", resp)
    fb = ask_feedback()
    feedback_log.append(
        {"function": "answer_question", "question": q, "response": resp, "feedback": fb}
    )


def summarize_text():
    text = input("Enter text to summarize: ").strip()
    prompt_fn = random.choice(summary_prompts)
    prompt = prompt_fn(text)
    resp = get_response(prompt)
    print("\nSummary:", resp)
    fb = ask_feedback()
    feedback_log.append(
        {"function": "summarize_text", "text": text, "response": resp, "feedback": fb}
    )


def generate_content():
    topic = input("Enter a topic for creative content: ").strip()
    prompt_fn = random.choice(creative_prompts)
    prompt = prompt_fn(topic)
    resp = get_response(prompt)
    print("\nStory:", resp)
    fb = ask_feedback()
    feedback_log.append(
        {
            "function": "generate_content",
            "topic": topic,
            "response": resp,
            "feedback": fb,
        }
    )


print("\nSelect a function:")
print("1. Answer a Question")
print("2. Summarize Text")
print("3. Generate Creative Content")
print("4. Exit")


def main():
    print("Welcome to Your Integrated AI Assistant!")
    while True:
        choice = input("Enter choice (1-4): ").strip()
        if choice == "1":
            answer_question()
        elif choice == "2":
            summarize_text()
        elif choice == "3":
            generate_content()
        elif choice == "4":
            print("\nThank you for using the AI Assistant. Goodbye!")
            # Optional: Print feedback summary or save it to a file here
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
