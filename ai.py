import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY", "")


def get_openai_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()


def main():
    prompt = "Hello from the AI!"
    answer = get_openai_response(prompt)
    print(answer)


if __name__ == "__main__":
    main()
