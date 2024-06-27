def find_text_from_file(text, file_name):
    with open(file_name, "r") as file:
        content = file.read().lower()
    return text.lower() in content

print(find_text_from_file("cat", "twinkle_poem.txt"))