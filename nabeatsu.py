#!/usr/bin/python
# -*- coding: utf-8 -*-

# アホ数字か否か


def is_aho(i: int)-> bool:
    # Is string 3 in the number?
    if '3' in str(i):
        return True

    # Is the number dividable by 3?
    if i % 3 == 0:
        return True

    return False


# 3の倍数と3のつく数字の時だけアホになる。
def say_nabeatsu(i: int) -> str:
    limit = 10000
    is_nabeatsu = is_aho(i)

    ####
    if not is_nabeatsu:
        return str(i) + ''

    if i > limit:
        return 'アホ'

    # To generate Nabeatsu word
    nabeatsu_dic = {
        1: '',
        2: 'ニ',
        3: 'サァーン',
        4: 'ヨーン',
        5: 'ゴー',
        6: 'ローク',
        7: 'ナーナ',
        8: 'ハーチ',
        9: 'キュー',
        0: ''
    }

    nabeatsu_ten_dic = {
        1: 'ジュー',
        2: 'ニージュ',
        3: 'サァーンジュ',
        4: 'ヨーンジュ',
        5: 'ゴージュ',
        6: 'ロークジュ',
        7: 'ナーナジュ',
        8: 'ハーチジュ',
        9: 'キュージュ',
        0: ''
    }

    nabeatsu_end_dic = {
        1: 'イーチ',
        2: 'ニーッ',
        3: 'サァーン',
        4: 'シーッ',
        5: 'ゴーッ',
        6: 'ローク',
        7: 'シーチ',
        8: 'ハーチ',
        9: 'キュ-ッ',
        0: ''
    }
    nabeatsu_str = ''
    if i >= 1000:
        nabeatsu_str += nabeatsu_dic[int(i / 1000)] + 'セェーン'
    if i >= 100:
        tmp_i = i - (int(i / 1000) * 1000)
        nabeatsu_str += nabeatsu_dic[int(tmp_i / 100)] + 'ヒャク'
    if i >= 10:
        tmp_i = i - (int(i / 100) * 100)
        nabeatsu_str += nabeatsu_ten_dic[int(tmp_i / 10)]

    nabeatsu_str += nabeatsu_end_dic[i % 10] + '!'
    return nabeatsu_str


def main():
    end_num = 10000
    for x in range(1, end_num + 1):
        print(say_nabeatsu(x))


if __name__ == "__main__":
    main()
