__author__ = "Shivam Shekhar"
made_by = "MilkDragon-6"


from src.game import *


def main():
    db.init_db()
    isGameQuit = intro_screen()
    if not isGameQuit:
        intro_screen()


if __name__ == "__main__":
    main()