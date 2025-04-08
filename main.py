import os
import openai
from dotenv import load_dotenv

openai.api_key = os.getenv("OPENAI_API_KEY")
load_dotenv()

while True:

    prompt = input("\nIntroduce una pregunta:")
    if prompt.lower() == "exit":
        break

    complection = openai.completions.create(engine= "gpt-3.5-turbo",
                            prompt=prompt,
                            max_tokens="1000")

    print(complection.choices[0].text)