import wikipedia
import textwrap
def get_summary(topic, max_sentences=5):
    try:
        page = wikipedia.page(topic)
        content = page.content
        summary = wikipedia.summary(topic, sentences=max_sentences)
        wrapped_summary = textwrap.fill(summary, width=90)
        bullet_points = wrapped_summary.split('. ')
        print("\n Summary Points:\n")
        for i, point in enumerate(bullet_points):
            if point.strip():
                print(f"{i+1}. {point.strip()}.")
        return wrapped_summary
    except wikipedia.exceptions.DisambiguationError as e:
        print("This topic is ambiguous. Possible options:")
        for option in e.options[:5]:
            print(f"- {option}")
    except wikipedia.exceptions.PageError:
        print("Page not found. Try a different keyword.")
    except Exception as e:
        print("Unexpected error:", str(e))
def save_summary_to_file(text, filename="summary.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"\n Summary saved to {filename}")
def speak_summary(text):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
if __name__ == "__main__":
    topic = input("Enter a Wikipedia topic: ")
    summary = get_summary(topic)
    if summary:
        choice = input("\n Save summary to file? (y/n): ").lower()
        if choice == 'y':
            save_summary_to_file(summary)
        voice = input(" Want to hear it aloud? (y/n): ").lower()
        if voice == 'y':
            speak_summary(summary)
