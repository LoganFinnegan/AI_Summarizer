from transformers import pipeline

def main():
    summarizer = pipeline("summarization")

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

    text = "\n".join(lines)

    # Keep text short to stay within model input limits
    max_chunk = 1000
    if len(text) > max_chunk:
        text = text[:max_chunk] + "..."

    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']

    print("\n📄 Summary:\n")
    print(summary)

if __name__ == "__main__":
    main()
