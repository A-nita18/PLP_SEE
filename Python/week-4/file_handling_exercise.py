#start with the file
with open("input.txt", "w") as f:
    f.writelines([
        "Hello! This is a file\n",
        "Strawberries are not actually berries\n",
        "Bananas however, are berries\n",
        "There are a lot of such lies integrated into our lives\n",
        "Be on the lookout\n"
    ])

# read the contents
with open("input.txt", "r") as f:
    print(f.read())

#count the number of words in the file
with open("input.txt", "r") as f:
    text = f.read()
    words = text.split()
    print("Word count is:", len(words))

#write it in uppercase
with open("input.txt","r") as f:
    text_upper = f.read().upper()

with open("input.txt", "w") as f:
    f.write(text_upper)

#transferring it to new file
with open("output.txt", "w") as f:
    f.write("The processed text is: \n" + text_upper)
    f.write("\nThe word count is: " + str(len(words)))

    print("Successful creation!")