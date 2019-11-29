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

    print(in_file)


if __name__ == '__main__':
    main()
