import openai
import dotenv
import os
import sys

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

path = sys.argv[-1]
prompt = "translate the above algorithm to python code and write only python code"

with open(path, "r") as f:
    prompt = f.read() + prompt

completion = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

python_code = completion.choices[0].text
print(python_code)
