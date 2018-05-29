import random


def auto_gen(num_digits):
    rand = random.SystemRandom()
    number_str = ""
    for i in range(num_digits):
        number_str += str(rand.randint(1, 6))
    return int(number_str)

    
# (Name, Filename, Number of dice required, Bits of entropy per word)
wordlists = [("Large list",   "eff_large_wordlist.txt",     5, 12.9),
             ("Short list 1", "eff_short_wordlist_1.txt",   4, 10.3),
             ("Short list 2", "eff_short_wordlist_2_0.txt", 4, 10.3)]
loaded_words = {}
password = ""
num_words = 0

print("Which list would you like to use?")
for i in range(len(wordlists)):
    print(str(i) + ":", wordlists[i][0])
selected_list = int(input())

with open(wordlists[selected_list][1]) as file:
    for line in file:
        (num, word) = line.split()
        loaded_words[int(num)] = word
       
while True:
    try:
        user_input = input("What are the " + str(wordlists[selected_list][2]) +
               " dice numbers? Type 'auto' to auto-generate or 'exit' to exit. ")
        if user_input.lower() == "exit":
            break
        if (user_input.lower() == "auto"):
            word_num = auto_gen(wordlists[selected_list][2])
        else:
            word_num = int(user_input)

        password += loaded_words[word_num].capitalize()
        num_words += 1

        print()
        print(password)
        print("Length: ", num_words, "\tEntropy: ",
                (num_words * wordlists[selected_list][3]), " bits")

    except (KeyError, ValueError):
        print("That was not a valid number. Please try again.")
    except KeyboardInterrupt:
        break