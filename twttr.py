def main():
    string = input("Input: ")
    output_string = shorten(string)
    print("Output: " + output_string)


def shorten(word):
    # Remove all lowercase and uppercase vowels from the input string

    if not isinstance(word, str):
        raise TypeError

    vowels = ["a", "e", "i", "o", "u"]

    output = "".join(
        char for char in word if char.lower() not in vowels
    )  # This is more efficient than using for loop and iterative string concatenation

    return output


if __name__ == "__main__":
    main()
