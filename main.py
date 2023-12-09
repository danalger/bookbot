#print("Hello World")
# Book needs to be a txt file do not use pdf
# with open("books/frankenstein.txt") as f:
#    file_contents = f.read()
#
#print(file_contents)
# Above this line is original code for project where everything is hard coded
# 
# Below this line is code to use the program with variables
# Code does not verify that the file read is a txt string at the moment.  Code will error if other types of files are inputted
def main():
    book_path = "books/frankenstein.txt" #book to be read needs to be in the books directory where the file is run
                                         #to change read book change frankenstein.txt to other book.txt
    text = get_book_text(book_path) # text is filed by opening the file in book_path from the get_book_text function below
    print(text)
    num_words = get_num_words(text)
    print(f"The number of words in this book is {num_words}.")
    letters = get_letters(text)
    print(letters)

def get_book_text(path):
    with open(path) as f: # path is set to book_path in main
        return f.read()

def get_num_words(book_string): # book_string is set to text in main this is the data read from the path as a text string
    words = book_string.split() 
    return len(words)

def get_letters(characters_to_check):
    temp_char = {'a':0,
                 'b':0,
                 'c':0,
                 'd':0,
                 'e':0,
                 'f':0,
                 'g':0,
                 'h':0,
                 'i':0,
                 'j':0,
                 'k':0,
                 'l':0,
                 'm':0,
                 'k':0,
                 'l':0,
                 'm':0,
                 'n':0,
                 'o':0,
                 'p':0,
                 'q':0,
                 'r':0,
                 's':0,
                 't':0,
                 'u':0,
                 'v':0,
                 'w':0,
                 'x':0,
                 'y':0,
                 'z':0}
    characters = characters_to_check.lower()
    for char, number in temp_char.items():
        temp_char[char] = characters.count(char)
    return temp_char
    #for char in characters:

main()