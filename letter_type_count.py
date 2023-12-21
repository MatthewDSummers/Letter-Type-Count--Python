def letter_type_count(s, vowels=False, consonants=False, all_letters=False, raw_count=False):
    if not isinstance(s, str):
        raise ValueError("Please provide a string input")

    vowels_dict = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0,
        "A": 0,
        "E": 0,
        "I": 0,
        "O": 0,
        "U": 0
    }

    consonants_dict = {}
    all_letters_dict = {}
    count = 0

    if all_letters:
        if not raw_count:
            for letter in s:
                if letter.isalpha():
                    if letter in all_letters_dict:
                        all_letters_dict[letter] += 1
                    else:
                        all_letters_dict[letter] = 1
        else:
            return len(s)
        return all_letters_dict

    elif vowels and not raw_count:
        for letter in s:
            if letter in vowels_dict:
                vowels_dict[letter] += 1

    elif consonants and not vowels:
        for letter in s:
            if letter.isalpha() and letter not in vowels_dict:
                if letter in consonants_dict:
                    consonants_dict[letter] += 1
                else:
                    consonants_dict[letter] = 1

    if raw_count:
        if vowels:
            for letter in s:
                if letter in vowels_dict:
                    count += 1
        elif consonants:
            for letter in s:
                if letter not in vowels_dict:
                    count += 1
    elif not raw_count:
        if vowels and not consonants:
            return vowels_dict

        elif consonants and not vowels:
            return consonants_dict

    return count

demo = letter_type_count("hello, this is a sentence. CAPITAL LETTERS", vowels=True)

for k, v in demo.items():
    print(f"{k}: {v}")

demo2 = letter_type_count("hello, this is a sentence. CAPITAL LETTERS", vowels=True, raw_count=True)
print(demo2)

demo3 = letter_type_count("apple", all_letters=True, raw_count=True)
print(demo3)