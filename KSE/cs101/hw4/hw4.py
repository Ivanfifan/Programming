import random
import json

class Player:
    def __init__(self):
        self.moves = ['камінь', 'ножиці', 'папір']

    def make_move(self):
        while True:
            answer = input('Введіть свій хід: ').strip().lower()
            if answer in self.moves:
                return answer
            print('Спробуйте ще раз')

class Bot:
    def __init__(self):
        self.moves = ['камінь', 'ножиці', 'папір']

    def make_move(self):
        return random.choice(self.moves)


class FileLogger:
    def __init__(self, filename):
        self.filename = filename

    def write(self,result_dict: dict):
        try:
            with open(self.filename, 'a', encoding='utf-8') as f:
                f.write(json.dumps(result_dict, ensure_ascii=False) + "\n")
        except Exception as e:
            print('Помилка ',e)

    def leaderboard(self):
        games = 0
        bot_wins = 0
        player_wins = 0
        draw = 0

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line in f:
                    games +=1
                    result = json.loads(line)

                    if result['win'] == 'player':
                        player_wins += 1
                    elif result['win'] == "ai":
                        bot_wins += 1
                    else:
                        draw += 1
        except FileNotFoundError:
            return "Файл не знайдено"

        return f"""
Ігор: {games}
Гравець: {player_wins}
Бот: {bot_wins}
Нічия: {draw}
"""

class Game:
    def __init__(self, filename="results.txt"):
        self.player = Player()
        self.bot = Bot()
        self.logger = FileLogger(filename)
        self.moves = ['камінь', 'ножиці', 'папір']

    def play_round(self):
        player_move = self.player.make_move()
        ai_move = self.bot.make_move()

        if ai_move == player_move:
            winner = 'draw'
        elif player_move == 'камінь' and ai_move == 'ножиці':
            winner = 'player'
        elif player_move == 'ножиці' and ai_move == 'папір':
            winner = 'player'
        elif player_move == 'папір' and ai_move == 'камінь':
            winner = 'player'
        else:
            winner = 'ai'

        result = {
            'player': player_move,
            'ai': ai_move,
            'win': winner
        }

        self.logger.write(result)

        print(f'Ваш хід: {player_move}')
        print(f'Бот: {ai_move}')

        if winner == "player":
            print("Ви перемогли")
        elif winner == "ai":
            print("Бот переміг")
        else:
            print("Нічия")

    def result(self):
        print(self.logger.leaderboard())

    def run(self):
        while True:
            self.play_round()
            again = input('Зіграти ще раз (так/ні): ')
            if again == 'ні':
                break

        self.result()
if __name__ == "__main__":
    game = Game("gambling_dodep.txt")
    game.run()