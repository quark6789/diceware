import random


def auto_gen():
    rand = random.SystemRandom()
    num_str = ""
    for i in range(5):
        num_str += str(rand.randint(1, 6))
    return int(num_str)


wordlist = {}
password = ""
num_words = 0

with open("eff_large_wordlist.txt") as file:
    for line in file:
        (num, word) = line.split()
        wordlist[int(num)] = word

while True:
    try:
        input_text = input("What are the 5 dice numbers? "
                "Type 'auto' to auto-generate or 'exit' to exit. ")
        if input_text.lower() == "exit":
            break
        if (input_text.lower() == "auto"):
            word_num = auto_gen()
        else:
            word_num = int(input_text)

        password += wordlist[word_num].capitalize()
        num_words += 1

        print()
        print(password)
        print("Length: ", num_words, "\tEntropy: ", (num_words * 12.9), " bits")

    except (KeyError, ValueError):
        print("That was not a valid number. Please try again.")
    except KeyboardInterrupt:
        break
