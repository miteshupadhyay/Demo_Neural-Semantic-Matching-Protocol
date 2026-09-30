import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

def test_openai_connection():
    try:
        # Get API key
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            print("ERROR: OPENAI_API_KEY not found!")
            return

        # Initialize OpenAI client
        client = OpenAI(api_key=api_key.strip())

        print("OpenAI client initialized successfully.")

        # Send a test request
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": "Say 'OpenAI API connection successful'."
                }
            ],
            max_tokens=50,
            temperature=0
        )

        # Display response
        print("\nSUCCESS: OpenAI API connection established!")
        print("Model:", response.model)
        print("Response:", response.choices[0].message.content)

    except Exception as e:
        print("\nERROR: OpenAI API connection failed!")
        print("Error:", str(e))


if __name__ == "__main__":
    test_openai_connection()