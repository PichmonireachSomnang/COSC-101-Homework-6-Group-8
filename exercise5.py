def backward_string_by_word(text: str) -> str:
    return " ".join([i[::-1] for i in text.split(" ")])


if __name__ == '__main__':
    print("your backword word is",backward_string_by_word('Hello World'))