#!/usr/bin/python3
from random import randrange, shuffle
from os import system, name


clear:str = ''
score:int = 0
def guess(gstr: str):
    field = ['_']*len(gstr)
    sh_char = list(set(gstr))
    shuffle(sh_char)
    sh_w: str = ', '.join(sh_char[:int(len(gstr)/2)])
    wrong: set[str] = set()
    tries_max = len(gstr)+2
    tries = 1
    while True:
        str_field = ''.join(field)
        system(clear_os())
        print(f'Подсказка: используемые буквы: {sh_w} ')
        if wrong:
            print(f'Не подходят: {", ".join(wrong)}')
        print(f'Слово: {str_field}')
        char = input('Введи букву или слово целиком> ')
        if char == gstr:
            print(f'Отгадал! Это действительно было: {gstr}')
            break
        for i, ch in enumerate(gstr):
            if ch == char:
                field[i] = ch
        if char not in gstr:
            wrong.add(char)
        if '_' in field:
            tries += 1
            if tries == tries_max:
                print(f'Не отгадал! Загадано было: {gstr}')
                return
            continue
        else:
            print(f'Отгадал! Слово было: {gstr}')
            break

def clear_os():
    return 'cls' if name == 'nt' else 'clear'


def main():
    with open('words.txt', mode='r' , encoding='utf-8') as f:
        str_words = f.read()
        words = [w.strip() for w in str_words.split(',')]
    system(clear_os())
    while True:
        enter = input('Сыграем? Если да, нажми Enter')
        if enter == 'д' or enter == '':
            system(clear_os())
            guess(words[randrange(0, len(words))])
        else:
            return


if __name__ == '__main__':
    main()
