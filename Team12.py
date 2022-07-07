

print("Enter the number of scripture volume would you like to serach? ")
print("Book of Mormon.1")
print("Doctrine and Covenants.2") 
print("Pearl of Great Price.3")
print("New Testament.4")
search_num = int(input("Old Testament.5? "))
search_vol = ""

# Not nessacery but I dont want to type out the books all the time
if search_num == 1:
    search_vol = "book of mormon"

elif search_num == 2:
    search_vol = "doctrine and covenants"

elif search_num == 3:
    search_vol = "pearl of great price"
    
elif search_num == 4:
    search_vol = "new testament"
    
elif search_num == 5:
    search_vol = "old testament"
    
max_chapter = 0
book_max = ""

search_max_chapter = 0
search_book_max = ""

with open("books_and_chapters.txt") as book_file:
    for line in book_file:

        book, chapters, scripture = line.strip().split(":")
        chapters = int(chapters)
        
        if chapters > max_chapter:
            max_chapter = chapters
            book_max = book

        if scripture.lower() == search_vol:
            print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")
            
            if chapters > search_max_chapter:
                search_max_chapter = chapters
                search_book_max = book

        
    print()
    print(f"{book_max} has {max_chapter} the most chaters in the scriptures.")
    print(f"{search_book_max} has {search_max_chapter} the most chaters in {search_vol}.")