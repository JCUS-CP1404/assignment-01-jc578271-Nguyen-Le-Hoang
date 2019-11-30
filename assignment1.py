"""
Name: Nguyen Le Hoang
Date started: 29/11/2019
GitHub URL: https://github.com/jc578271/assignment1.git
"""


def main():
    """..."""
    print("Movies To Watch 1.0 - by <Nguyen Le Hoang>")

    in_file = open('movies.csv' ,'r')

    while True:
        print("""
        Menu:
        L - List movies
        A - Add new movie
        W - Watch movie
        Q - Quit
        """)
        choiceInMenu = input(">>> ").upper()
        if choiceInMenu == "L":
            listMovie(in_file)

    in_file.close()


def listMovie(in_file):
    # reach every movie
    movies = in_file.read().split('\n')
    
    index = 0
    numberUnwatched = 0
    numberWatched = 0
    
    # reach every element in each
    for movie in movies:
        elements = movie.split(',')
        print(index, end='. ')

        # check * for unwatched movies
        if elements[3] == 'u':
            numberUnwatched += 1
            print('* ', end='')
        elif elements[3] == 'w':
            numberWatched += 1
            print('  ', end='')

        print(elements[0], end= algin(movies,elements[0]))
        print(' - {0} ({1})'.format( elements[1], elements[2]))
        index += 1
    print()
    print('{0} movies watched, {1} movies still to watch'.format(numberWatched, numberUnwatched))
            
def algin(movies,movieName):
    maxLength = 0
    space = ''
    for movie in movies:
        elements = movie.split(',')
        for element in elements:
            if maxLength < len(element):
                maxLength = len(element)
            else:
                continue
    for i in range(maxLength - len(movieName)):
        space += ' '
    return space


if __name__ == '__main__':
    main()
