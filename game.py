import random


class Game:
    def __init__(self, gamer, computer):
        self.gamer = gamer
        self.computer = computer
        self.used_kegs = []

    def show_keg(self):
        keg = random.randrange(1, 91)
        while True:
            if keg in self.used_kegs:
                keg = random.randrange(1, 91)
                continue
            else:
                break
        self.used_kegs.append(keg)
        return keg

    @staticmethod
    def add_spaces(lst):
        for i in range(1, 5):
            lst.insert(random.randint(0, len(lst)), " ")
        return lst

    def insert_spaces(self, lst):
        part_one = lst[0:5]
        part_two = lst[5:10]
        part_three = lst[10:15]
        return self.add_spaces(part_one) + self.add_spaces(part_two) + self.add_spaces(part_three)

    def card(self):
        line = self.insert_spaces(sorted(random.sample(range(1, 91), 15)))
        return line

    @staticmethod
    def show_card(line, number):
        return f"-----Карточка №{number}-------\n" \
            f"{' '.join(map(str, line[0:9]))}\n" \
            f"{' '.join(map(str, (line[9:18])))}\n" \
            f"{' '.join(map(str, (line[18:27])))}\n" \
            f"-----------------------"

    @staticmethod
    def end_game():
        print("Игра завершена, вы проиграли")

    def start_game(self):
        self.gamer.add_card(self.card())
        self.computer.add_card(self.card())

        while True:
            if self.gamer.you_win() and self.computer.you_win():
                print("Оба билета выигрышные!")
                break
            elif self.computer.you_win():
                print("Выиграл компьютер!")
                break
            elif self.gamer.you_win():
                print("Вы выиграли!!!")
                break
            keg = self.show_keg()
            print(f"\nНовый бочонок: {keg} (осталось {90 - len(self.used_kegs)})\n")
            print(f"{self.show_card(self.gamer.get_card(), 1)}\n"
                  f"{self.show_card(self.computer.get_card(), 2)}")
            self.computer.remove_keg(keg)
            user_input = int(input("Введите 1 - зачеркнуть или 2 - продолжить: "))
            if user_input == 1:
                check = self.gamer.remove_keg(keg)
                if check:
                    continue
                else:
                    self.end_game()
                    break
            elif user_input == 2:
                check = self.gamer.check_keg(keg)
                if check:
                    continue
                else:
                    self.end_game()
                    break
            else:
                print("Неверный ввод, вы проиграли.")
                break


class Gamer:
    def __init__(self):
        self.card = []

    def add_card(self, card):
        self.card = card

    def get_card(self):
        return self.card

    def remove_keg(self, keg):
        if keg in self.card:
            index_keg = self.card.index(keg)
            self.card[index_keg] = "-"
            return True
        else:
            return False

    def check_keg(self, keg):
        if keg in self.card:
            return False
        else:
            return True

    def you_win(self):
        for item in self.card:
            if type(item) == int:
                return False
        return True


class Computer(Gamer):
    def remove_keg(self, keg):
        if keg in self.card:
            index_keg = self.card.index(keg)
            self.card[index_keg] = "-"


gamer1 = Gamer()
computer1 = Computer()
game = Game(gamer1, computer1)
game.start_game()
