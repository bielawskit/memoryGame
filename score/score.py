import json
from json import JSONDecodeError
from os import path


class Score:
    def __init__(self, name, game_time, start_time, end_time, game_type):
        self.game_time = game_time
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.filename = f'users_{game_type}.json'

    def add_person(self):
        # get username and send him message Name: time
        game_time = int(self.end_time - self.start_time)
        users = self.load_json_data()
        user = input("Give us your name : ").capitalize()
        if user not in users:
            users[user] = game_time
        else:
            if game_time < users[user]:
                users[user] = game_time
        print(f"{user} your time is : {game_time} ")
        # users[user] = game_time if user not in users else min(game_time, users[user])
        self.save_json_data(users)

    def load_json_data(self):
        if path.isfile(self.filename) is False:
            raise Exception("File not found")
        with open(self.filename) as fp:
            try:
                users = json.load(fp)
            except JSONDecodeError:
                users = {}
        return users

    def save_json_data(self, users):
        with open(self.filename, 'w') as json_file:
            json.dump(users, json_file,
                      indent=4)

    def print_top_10_users(self):
        results = {}
        users = self.load_json_data()
        # score = sorted(users.items(), key=lambda x: x[1])
        score = sorted(users, key=lambda x: users[x])
        print(score)
        user_time = sorted(list(users.values()))
        score = score[:10]
        print("Scoreboard:")
        for i in range(len(score)):
            results[int(i)] = score[i]
            print(f"{i + 1}: {score[i]} - {user_time[i]}s")

    # def view_list(self):
    #     with open("users_easy_game.json", "r") as file:
    #         score = Score(**json.loads(file.read()))
    #         print(score.name, score.game_time)
