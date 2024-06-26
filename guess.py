#!/usr/bin/python3
from random import randrange, shuffle
from os import system, name


clear: str = 'cls' if name == 'nt' else 'clear'
score: int = 0


def guess(gstr: str):
    global score
    field = ['_']*len(gstr)
    sh_char = list(set(gstr))
    shuffle(sh_char)
    sh_w: str = ', '.join(sh_char[:int(len(gstr)/2)])
    wrong: set[str] = set()

    def print_table():
        system(clear)
        print(f'Очки: {score}')
        print(f'Подсказка: используемые буквы: {sh_w} ')
        if wrong:
            print(f'Не подходят: {", ".join(wrong)}')
        print(f'Слово: {str_field}')
    while True:
        str_field = ''.join(field)
        print_table()
        char = input('Введи букву или слово целиком> ')
        if char == gstr:
            if field.count('_') > 1:
                score += 5
                bonus = '+5 очков!'
            else:
                score += 1
                bonus = ''
            print_table()
            print(f'Отгадал! Это действительно было: {gstr} {bonus}')
            break
        for i, ch in enumerate(gstr):
            if ch == char:
                
                field[i] = ch
                if char not in sh_w:
                    sh_w += ', ' + char
                    score += 1
        if char not in gstr:
            wrong.add(char)
            score -= 1
        if '_' not in field:
            print_table()
            print(f'Отгадал! Слово было: {gstr}')
            break
        if score == 0:
            print_table()
            print(f'Очки закончились! Начинаем заново!')
            score = 10
            return


def main():
    global score
    with open('words.txt', mode='r', encoding='utf-8') as f:
        str_words = f.read()
        words = [w.strip() for w in str_words.split(',')]
    system(clear)
    score += 10
    while True:
        enter = input('Сыграем? Если да, нажми Enter')
        if enter == 'д' or enter == '':
            system(clear)
            guess(words[randrange(0, len(words))])
        else:
            return


if __name__ == '__main__':
    main()
