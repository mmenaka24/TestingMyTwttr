def main():
    string = input("Input: ")
    output_string = shorten(string)
    print("Output: " + output_string)


def shorten(word):
    if not isinstance(word, str):
        raise TypeError

    output = ""

    vowels = ["a", "e", "i", "o", "u"]

    for char in word:
        if not char.lower() in vowels:
            output = output + char

    return output


if __name__ == "__main__":
    main()
