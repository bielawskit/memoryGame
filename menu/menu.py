from game import Game


def choose_option():
    print(
        "█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀ \n" +
        "▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄ \n" +
        "\n" +
        "▀█▀ █▀█ \n" +
        "░█░ █▄█ \n" +
        "\n" +
        "█▀▄▀█ █▀▀ █▀▄▀█ █▀█ █▀█ █▄█ \n" +
        "█░▀░█ ██▄ █░▀░█ █▄█ █▀▄ ░█░ \n" +
        "\n" +
        "█▀▀ ▄▀█ █▀▄▀█ █▀▀ █ █ █\n" +
        "█▄█ █▀█ █░▀░█ ██▄ ▄ ▄ ▄\n")
    print("Please choose your level: ")
    print("[1] Easy level: 4 randomly selected words to discover, 10 chances ")
    print("[2] Hard level: 8 randomly selected word pairs, 15 chances")
    print("[3] Exit the game.")


def check_user_input():
    # checking user input
    option = input("Enter your option: ")
    try:
        option = int(option)
    except ValueError:
        try:
            option = float(option)
            print("Input is a float number. Try one more.")
        except ValueError:
            print("Input is a string. Try one more.")
    return option


def load_game():
    # user has to choose one option
    choose_option()
    option = check_user_input()
    while True:
        if option == 1:
            game = Game(4, 2, 10, game_type="easy_game")

        elif option == 2:
            game = Game(8, 2, 15, game_type="hard_game")

        elif option == 3:
            print("Good bye.")
            break

        else:
            print("Invalid option")
            break
        game.load_words()
        game.drawn_board()
        game.random_words()
        game.hide_words()
        game.start_game()
        game.print_top_10_users()
        break
