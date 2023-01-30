def is_verse_from_separated_line (text):
    text = text.strip()

    for i in range(len(text)-3):
        if text[i] == "\n":
            if text[i+1] == "\n" and text[i+2] == "\n" and text[i+3] == "\n":
                return True
            return False

    return False