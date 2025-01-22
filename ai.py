from openai import OpenAI

MY_KEY = None

# Load the API key from a file
with open("OPENAI_API_KEY.txt", "r") as f:
    MY_KEY = f.read().strip()

client = OpenAI(
        api_key=MY_KEY,  # Your API key here
    )


def get_openai_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o",
    )
    return chat_completion.choices[0].message.content


def main():
    prompt = "Hello from the AI!"
    answer = get_openai_response(prompt)
    print(answer)


if __name__ == "__main__":
    main()
