from src.game import intro_screen, db

made_by = "TwoSeokTwoJu-3"


def main():
    db.init_db()
    is_game_quit = intro_screen()
    if not is_game_quit:
        intro_screen()


if __name__ == "__main__":
    main()
