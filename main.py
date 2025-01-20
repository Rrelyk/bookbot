
def readbook(path):
    try:
        with open(path) as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        print("File not found at specified path.")
        return none

def countwords(book):
    wordcount = len(book.split())
    return wordcount

def countcharacter(book):
    lbook = book.lower()
    charcount = {}
    for char in lbook:
        if char not in charcount:
            charcount[char] = 0
        charcount[char] += 1
    
    return charcount

def sort_on(ccount):
    return ccount["num"]

def report(ccount):
    reportlist = []
    sortlist = []
    for key,value in ccount.items():
        if key.isalpha():
            sortlist.append({"char": key, "num": value})
            
    sortlist.sort(reverse=True, key=sort_on)
    for item in sortlist:
        reportlist.append(f"The '{item['char']}' character was found {item['num']} times")

    return reportlist

def main():
    path = "books/frankenstein.txt"
    book = readbook(path)
    words = countwords(book)
    ccount =countcharacter(book)
    export = report(ccount)
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    for item in export:
        print(item)
    print("--- End report ---")

if __name__ == '__main__':
    main()
