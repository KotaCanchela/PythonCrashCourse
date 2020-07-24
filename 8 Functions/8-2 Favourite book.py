#  Write a function called favorite_book() that accepts one parameter, title.
#  The function should print a message, such as One of my favorite books is Alice in Wonderland.
#  Call the function, making sure to include a book title as an argument in the function call.


def favourite_book(title):
    """Prints user's favourite book."""
    print(f"My favourite book is {title.title()}")


favourite_book('le petit prince')

favourite_book('alice in wonderland')