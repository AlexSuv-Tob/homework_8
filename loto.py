import random
from math import ceil
import sys

class Data:

    def data(self):
        self.barrels = 90
        self.bar_game = random.sample(range(1, 91), 90)
        self.barrel = random.sample(bar_game)
        self.bar = random.sample(barrel, 1)
        self.string1 = random.sample(range(1, 91), 15) + list(' ' * 12)
        self.string2 = random.sample(range(1, 91), 15) + list(' ' * 12)
        self.b1 = 15
        self.b2 = 15

class CardGame(Data):
    def in_put(self):
        name = input('Введите имя игрока: ')
        q = 0
        if q == 0:
            print('-' * 3, 'карточка', name, '-' * 3)
            random.shuffle(self.string1)
            le = ceil(len(self.string1) / 3)
            res = [self.string1[le * i:le * (i + 1)] for i in range(len(self.string1))]
            res = list(filter(None, res))
            for i in res:
                print(*i, sep=' ')
        print('-' * 26)
        q += 1

        if q == 1:
            print('-' * 3, 'карточка Компьютера', '-' * 3)
            random.shuffle(self.string2)
            le = ceil(len(self.string2) / 3)
            res = [self.string2[le * i:le * (i + 1)] for i in range(len(self.string2))]
            res = list(filter(None, res))
            for i in res:
                print(*i, sep=' ')
        print('-' * 26)



class Motion(CardGame, Data):

    def my_motion(self):
        a = input('Зачеркнуть цифру? (y/n):')
        if a == 'y':
            if self.bar in self.string1:
                for i in self.string1:
                    i.insert(i.index(self.string1), '><')
                    i.pop(i.index(self.string1))
                print('OK')
                return 1
            else:
                print('Вы ошиблись. Игра Окончена!')
                sys.exit()

        if a == 'n':
            if self.bar in self.string1:
                print('Вы ошиблись. Игра Окончена!')
                sys.exit()
            else:
                print('OK')

    def com_motion(self):
        if self.bar in self.string2:
            for l in self.string2:
                l.insert(l.index(self.string1), '><')
                l.pop(l.index(self.string1))
            return 1

class Game(CardGame, Motion, Data):
    def start(self):
        data = Data()
        card = CardGame()
        data.data()
        card.in_put()
        for bar in self.barrel:
            self.barrels -= 1
            print(f'Новый баченок: {bar}, осталось баченков{self.barrels}')
            self.barrel.remove(bar)
            motion = Motion()
            motion.my_motion()
            motion.com_motion()
            if motion.my_motion() == 1:
                self.b1 -= 1
            if motion.com_motion() == 1:
                self.b2 -= 1
            if self.b1 == 0:
                print('Вы выиграли, Поздравляем!')
                sys.exit()
            if self.b2 == 0:
                print('выиграл компьютер. Вы проиграли')
                sys.exit()
            if self.barrels == 0:
                print('Ничья, никто не выиграл')
                sys.exit()

game = Game()
game.start()

