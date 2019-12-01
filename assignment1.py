"""
Name: Nguyen Le Hoang
Date started: 29/11/2019
GitHub URL: https://github.com/jc578271/assignment1.git
"""


def main():
    """..."""
    print("Movies To Watch 1.0 - by <Nguyen Le Hoang>")
    in_file = open('movies.csv' ,'r+')
    movies = in_file.readlines()
    while True:
        print("Menu:")
        print(" L - List movies")
        print("A - Add new movie")
        print("W - Watch movie")
        print("Q - Quit")
        choiceInMenu = input("\t>>> ").upper()
        if choiceInMenu == "L":
            listMovie(movies)
        elif choiceInMenu == "W":
            watchingMovie(movies)
    in_file.close()

def listMovie(movies):
    # reach every movie
    index = 0
    countUnwatched = 0
    countWatched = 0
    # reach every element in each
    for movie in movies:
        elements = movie.split(',')
        print(index, end='. ')
        # check * for unwatched movies
        if 'u' in elements[3]:
            countUnwatched += 1
            print('* ', end='')
        elif 'w' in elements[3]:
            countWatched += 1
            print('  ', end='')
        print(elements[0], end= algin(movies,elements[0]))
        print(' - {0} ({1})'.format( elements[1], elements[2]))
        index += 1
    print()
    print('{0} movies watched, {1} movies still to watch'.format(countWatched, countUnwatched))

            
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


def watchingMovie(movies):
    choiceMovie = int(input("Enter the number of a movie to mark as watched \n\t>>> "))
    # Split elements by ','
    elements = movies[choiceMovie].split(',')
    if elements[3] == 'u\n':
        # replace 'u' by 'w'
        elements[3] = elements[3].replace('u\n','w\n')
        # join elements into movies
        movies[choiceMovie] = ','.join(elements)
        print('{} watched'.format(elements[0]))
    else:
        print('You have already watched {}'.format(elements[0]))
    

if __name__ == '__main__':
    main()
