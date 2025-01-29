def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    returned_dict = char_counter(file_contents)
    returned_dict = dict(sorted(returned_dict.items(), key=lambda item: item[1], reverse=True))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(file_contents.split())} words found in the document")
    print("")
    for k, v in returned_dict.items():
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

def char_counter(text):
    char_dict = {}
    for t in text.lower().strip():
        if t not in char_dict:
            char_dict[t] = 1
        else:
            char_dict[t] += 1
    return char_dict


main()