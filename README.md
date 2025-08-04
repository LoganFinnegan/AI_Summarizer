# AI Summarizer (Hugging Face Edition)

A simple command-line Python script that summarizes long pieces of text using a pretrained Hugging Face model. Paste in any block of text, and get a clean, readable summary back in seconds.

---

## Features

- Uses Hugging Face's `transformers` library
- Supports free, open-source summarization (no API key needed)
- Runs locally in your terminal
- Automatically downloads and caches the model the first time

---

## Project Structure

ai_summarizer/
├── summarizer_hf.py # Main script
├── requirements.txt # List of dependencies
├── .gitignore # Prevents secrets/venv from being tracked
├── venv/ # Your local virtual environment (not tracked by Git)


---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/ai_summarizer.git
cd ai_summarizer
```

### 2. Create a virtual environment

```bash
# On Mac/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows:
.\venv\Scripts\activate
```

### 3. Install dependencies

```bash
 pip install -r requirements.txt
```
### 4. Run the summarizer

```bash 
python summarizer_hf.py
```

Paste or type your input text directly into the terminal. Press Enter twice to signal that you’re done typing. You’ll receive a summary in return.

### Example

Paste the text you'd like to summarize. Enter two blank lines to finish:

Astarion is a high elven vampire spawn...
(press Enter twice)

### Summary:

Astarion is a centuries-old vampire spawn who values appearance, hygiene, and style.

### Model Info

This script uses the sshleifer/distilbart-cnn-12-6 model — a distilled version of Facebook’s BART model trained to summarize news articles and other long-form content.

### FAQ

Q: Will this work without an internet connection?

Only after the model has been downloaded the first time. The model is cached locally after that.

Q: Can I summarize really long articles?

There’s a built-in 1000-character limit to keep things performant. You can chunk and summarize longer texts manually or modify the script to do so automatically.

### Security

This version does not require any API keys.
If you later add OpenAI integration, keep your API keys in a .env file and never commit it.

### License

MIT — free to use and modify.

### Author 
LoganFinnegan