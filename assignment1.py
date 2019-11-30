"""
Name: Nguyen Le Hoang
Date started: 29/11/2019
GitHub URL: https://github.com/jc578271/assignment1.git
"""


def main():
    """..."""
    print("Movies To Watch 1.0 - by <Nguyen Le Hoang>")

    print("""
    Menu:
    L - List movies
    A - Add new movie
    W - Watch movie
    Q - Quit
    """)
    while True:
        choiceInMenu = input(">>> ").upper()
        if choiceInMenu == "L":
            listMovie()


def listMovie():
    in_file = open('movies.csv' ,'r')
    movies = in_file.read().split('\n')
    maxLength = 0
    maxLengthTitle = ''
    for movie in movies:
        elements = movie.split(',')
        # print(elements[0], elements[1], elements[2], elements[3])
        for element in elements:
            if maxLength < len(element):
                maxLengthTitle = element
            else:
                maxLengthTitle = maxLengthTitle
    print(maxLengthTitle)
    in_file.close()
            
        
# def findingTheLongestTitle(elements):
#     maxLength = 0
#     for element in elements:
#         if maxLength < len(element):
#             maxLengthTitle = element
#         else:
#             continue
#         print(maxLengthTitle)


if __name__ == '__main__':
    main()
