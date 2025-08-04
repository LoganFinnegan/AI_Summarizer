import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Paste the text you'd like to summarize. Enter two blank lines to finish:")

lines = []
blank_line_count = 0

while True:
    line = input()
    if line.strip() == "":
        blank_line_count += 1
        if blank_line_count == 2:
            break
    else:
        blank_line_count = 0
        lines.append(line)

text_to_summarize = "\n".join(lines)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that summarizes text."},
        {"role": "user", "content": f"Please summarize the following text:\n{text_to_summarize}"}
    ],
    temperature=0.5,
    max_tokens=300
)

summary = response.choices[0].message.content

print("\n📄 Summary:\n")
print(summary)
