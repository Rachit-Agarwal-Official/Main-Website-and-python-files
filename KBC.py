# Printing Starting lines of the program
a = input("!!Press Enter To Continue!!")
print("\nWelcome to the Kaun Banega Crorepati - Rachit's Edition\n")
print('''These are some points to remember while playing the game:-
1. All the answers can be either in uppercase or lowercase or capitalized
2. Use numbers in case you have to use
3. Check the spellings because mistakes will lead you to end
4. All the questions will give you a certain amount that will take place of your previous one
5. You'll only continue if the answer is correct otherwise you'll get the prize you have as your prize money and exit

And this Program is newly made so does not have all the correct answers so if you face any problem with it, please calm down we are still working on it...
''')
b = input("If you've read the points (Press Enter to continue)")


# Questions we have in the Quiz
questions = [
    ["How many Bits makes one Byte?", "", "8 bits", "", "", 2],
    ["Google is a Browser or a Search Engine?", "search engine", "", "", "", 1],
    ["Printer is the example of which types of device, Output or Input?", "", "", "", "", "output device"],
    ["What is the full form of RAM?", "", "", "", "",     "random access memory"],
    ["Who is the founder of Facebook?", "", "", "", "", "mark zuckerberg"],
    ["Which electronic component was used in first generation of computers?", "", "", "", "", "vaccum tubes"],
    ["All mathematical and logical functions in the computer are done by?", "", "", "", "", "central processing unit"],
    ["Attempts made by individuals to obtain confidential information from you by falsifying their identity are called?", "", "", "", "", "phising scams"],
    ["Who was the programmer of Ms-Dos operating system?", "", "", "", "", "bill gates"],
    ["Full form of VIRUS is?", "", "", "", "", "virtual information resource under seize."],
    ["1 Kilobyte is equal to how many bytes?", "", "", "", "", "1024 bytes"],
    ["Who is called Father of Computer?", "", "", "", "", "charles babbage"],
    ["When you purchase a product over a Mobile Phone, the transaction is called?", "", "", "", "", "m-commerce"],
    ["A formal language designed to communicate instructions to a machine, particularly a computer is called?", "", "", "", "", "programming language"],
    ["The man who built the first Mechanical Calculator was?", "", "", "", "", "blaise pascal"],
    ["What contains specific rules and words that express the logical steps of an algorithm?", "", "", "", "", "syntax"]
]

# Prizes for every question according to the index 
prize = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]

# Initializing the winning amount
money_won = 0

for i in range(0, len(questions)):
    ques = questions[i]
    print(f"\nQuestion for ₹{prize[i]}:")
    print(ques[0])
    print(f"a. {ques[1]}           b. {ques[2]}")
    print(f"c. {ques[3]}           d. {ques[4]}")

    ans = int(input("Enter the answer(1-4) or Enter 0 to exit: "))

    if ans == 0 and i > 0:
        money_won = prize[i-1]
        break
    elif ans == ques[-1]:
        print("Correct Answer!")
    else:
        print("Wrong Answer!")
        break

print(f"Your taking home amount is ₹{money_won}")