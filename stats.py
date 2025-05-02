def word_count(text):
    #with open('books/frankenstein.txt') as frank:
    #    book_contents = frank.read()
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    
    print(f"Found {counter} total words")
    # print(words)


def char_count(text):
    dict = {}
    #with open('books/frankenstein.txt') as frank:
    #    book_contents = frank.read()
    #lower_book = book_contents.lower()
    text1 = text.lower()
    chars = list(text1)
    for char in chars:
        if char.isalpha():
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    sorted_list = []
    for key in dict:
        temp_dict = {"char": key , "num":dict[key] }
        sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key = sort_on)
    #print(sorted_list)
    
    for key in sorted_list:
        print(f"{key['char']}: {key['num']}")
    
    