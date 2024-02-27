def main():
    text = input("Enter your text: ")
    no_vowels = remove_vowels(text)
    print ("Text withour vowels:", no_vowels)

def remove_vowels(text):
    vowels = "aeiuoAEIUO"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
        else:
            result += ''
    return result

if __name__ == "__main__":
    main()