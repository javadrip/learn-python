# TODO: Create a letter using starting_letter.txt

# for each name in invited_names.txt
with open("input/Names/invited_names.txt") as names_file:
    name_list = names_file.readlines()

# Replace the [name] placeholder with the actual name.
with open("input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter_content.replace("[name]", stripped_name)
        with open(
            f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w"
        ) as completed_letter:
            completed_letter.write(new_letter)

# Save the letters in the folder "ReadyToSend".


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
