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
    book_path = 'books/frankenstein.txt' #book to be read needs to be in the books directory where the file is run
                                         #to change read book change frankenstein.txt to other book.txt
    text = get_book_text(book_path) # text is filed by opening the file in book_path from the get_book_text function below
    print(text)
    num_words = get_num_words(text)
    #print(f'The number of words in this book is {num_words}.')
    letters = get_letters(text)
    #print(letters)
    #temp_list = dict.items(letters)
    sorted_letters = letters_dict_to_sorted_list(letters)
    #print(sorted_letters)
    print(f'--- Begin report of {book_path} ---')
    print(f'The number of words in this book is {num_words}.\n\n')
    #print(dict.items(letters))
    for let in sorted_letters:
        print(f'The "{let["letter"]}" letter was found {let["num"]} times') 
    print(f'\n ---End Report---')

def get_book_text(path):
    with open(path) as f: # path is set to book_path in main
        return f.read()

def get_num_words(book_string): # book_string is set to text in main this is the data read from the path as a text string
    words = book_string.split() 
    return len(words)

def get_letters(characters_to_check): # characters_to_check is set to text in main this is the data read from the path as a text string
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
        temp_char[char] = characters.count(char) # updates the value for each key item in temp_char ie key "a" value of 0 should change to number of "a" in text 
    return temp_char

def sort_on(dict): #Just used as sorting key
    return dict["num"]

def letters_dict_to_sorted_list(number_characters_dictionary): #Changing dictionary to list and sorting by most used letter
    temp_sorted_list = []
    for letters in number_characters_dictionary:
        temp_sorted_list.append({'letter': letters, 'num': number_characters_dictionary[letters]})
    temp_sorted_list.sort(reverse=True, key=sort_on)
    return temp_sorted_list

main()