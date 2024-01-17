def analyze_text(text: str) -> dict:
    details: dict = {
        "words": (words := text.split()),
        "word_count": len(words),
        "character_count": len(text),
    }
    return details


print(analyze_text("Hello, my name is Besma"))
