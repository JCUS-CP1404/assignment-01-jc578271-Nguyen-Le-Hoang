"""
Name: Nguyen Le Hoang
Date started: 29/11/2019
GitHub URL: https://github.com/jc578271/assignment1.git
"""


def main():
    """..."""
    print("Movies To Watch 1.0 - by <Nguyen Le Hoang>")
    
    # Open file
    in_file = open('movies.csv' ,'r+')
    movies = in_file.readlines()
    print('{} movies loaded\n'.format(len(movies)))
    
    # Menu
    while True:
        print("Menu:")
        print("L - List movies")
        print("A - Add new movie")
        print("W - Watch movie")
        print("Q - Quit")
        choiceInMenu = input("  >>> ").upper()
        if choiceInMenu == "L":
            listMovie(movies)
        elif choiceInMenu == "W":
            watchingMovie(movies)
        elif choiceInMenu == "A":
            addMovie(movies)
        elif choiceInMenu == "Q":
            #find the beginning of file
            in_file.seek(0)
            # Input movies in file
            for movie in movies:
                in_file.write(movie)

            print('{} movies saved to movies.csv'.format(len(movies)))
            print('Have a nice day :))')
            break
        else:
            print("Invalid choice")
    # Close file
    in_file.close()


# =====================
# SHOW LIST OF MOVIES |
# =====================
def listMovie(movies):
    # reach every movie
    index = 1
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


#==================
# WATCHING MOVIES |
#==================
def watchingMovie(movies):
    while True:
        try:
            choiceMovie = int(input("Enter the number of a movie to mark as watched \n  >>> "))
            if choiceMovie not in range(1, len(movies)+1):
                raise KeyError('Out of range')
            # Split elements by ','
            elements = movies[choiceMovie-1].split(',')
            if 'u' in elements[3]:
                # replace 'u' by 'w'
                elements[3] = elements[3].replace('u','w')
                # join elements into movies
                movies[choiceMovie-1] = ','.join(elements)
                print('{} watched'.format(elements[0]))
                break
            else:
                raise Exception('already watched')
        except ValueError: 
            print('Invalid syntax. Try again!')
        except KeyError:
            print('Cannot find the movie')
        except Exception:
            print('You have already watched {}'.format(elements[0]))
            break
        

#=============
# ADD MOVIES |
#=============
def addMovie(movies):
    titleMovie = errorTextHandler('Title: ')
    yearMovie = errorNumberHandler('Year: ')
    categoryMovie = errorTextHandler('Category: ')
    #add new movie in movies
    newMovie = ('\n{},{},{},u'.format(titleMovie,yearMovie,categoryMovie))
    movies.append(newMovie)
    #print result
    print()
    print("{} ({} from {}) added to movie list".format(titleMovie,categoryMovie,yearMovie))


def errorTextHandler(element):
    while True:
        textInput = input(element)
        if textInput.strip() == '':
            print('{} cannot be blank'.format(element))
        else:
            break
    return textInput


def errorNumberHandler(element):
    while True:
        try:
            numberInput = int(input(element))
            if numberInput < 0:
                raise Exception('Number must be >= 0')
            else:
                break
        except ValueError:
            print('Invalid input')
        except Exception:
            print('{} must be greater than or equal to 0'.format(element))
    return numberInput    


if __name__ == '__main__':
    main()
